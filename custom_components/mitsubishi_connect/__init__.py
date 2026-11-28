"""Mitsubishi Connect Home Assistant integration."""

from __future__ import annotations

import hashlib
import logging
from pathlib import Path

from homeassistant.components.frontend import add_extra_js_url
from homeassistant.components.http import StaticPathConfig
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.storage import Store
from homeassistant.helpers.typing import ConfigType

from .api import MitsubishiApiClient, MitsubishiAuthError, TokenBundle
from .const import (
    CONF_EMAIL,
    CONF_PASSWORD,
    CONF_REGION,
    DEFAULT_REGION,
    DOMAIN,
    PLATFORMS,
    STORAGE_VERSION,
)
from .coordinator import MitsubishiConnectCoordinator
from .regions import REGIONS

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = cv.config_entry_only_config_schema(DOMAIN)

CARDS_URL = f"/{DOMAIN}/mitsubishi-connect-cards.js"
CARDS_PATH = Path(__file__).parent / "frontend" / "mitsubishi-connect-cards.js"


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Serve the bundled Lovelace cards and load them on every dashboard."""
    digest = await hass.async_add_executor_job(
        lambda: hashlib.sha256(CARDS_PATH.read_bytes()).hexdigest()[:12]
    )
    await hass.http.async_register_static_paths(
        [StaticPathConfig(CARDS_URL, str(CARDS_PATH), True)]
    )
    # Keyed on the file content so browsers drop their cached copy whenever the cards change
    add_extra_js_url(hass, f"{CARDS_URL}?v={digest}")
    return True


def _token_store(hass: HomeAssistant, entry_id: str) -> Store[dict]:
    return Store(hass, STORAGE_VERSION, f"{DOMAIN}.{entry_id}.tokens")


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Mitsubishi Connect from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    region_key = entry.data.get(CONF_REGION, DEFAULT_REGION)
    profile = REGIONS.get(region_key, REGIONS[DEFAULT_REGION])

    store = _token_store(hass, entry.entry_id)
    stored = await store.async_load()
    tokens = TokenBundle.from_dict(stored) if isinstance(stored, dict) else TokenBundle.new()

    async def _save_tokens(bundle: TokenBundle) -> None:
        await store.async_save(bundle.to_dict())

    api = MitsubishiApiClient(
        session=async_get_clientsession(hass),
        profile=profile,
        tokens=tokens,
        on_tokens_updated=_save_tokens,
    )

    # Only perform initial login if we don't already have persisted tokens
    if not tokens.access_token and not tokens.refresh_token:
        try:
            await api.login(entry.data[CONF_EMAIL], entry.data[CONF_PASSWORD])
        except MitsubishiAuthError as err:
            raise ConfigEntryAuthFailed(str(err)) from err

    coordinator = MitsubishiConnectCoordinator(hass, entry, api)
    await coordinator.async_config_entry_first_refresh()

    hass.data[DOMAIN][entry.entry_id] = coordinator
    entry.async_on_unload(entry.add_update_listener(_async_update_listener))

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def _async_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload integration when options (poll interval, PIN, temp unit) change."""
    await hass.config_entries.async_reload(entry.entry_id)


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)
    return unload_ok


async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Clean up persisted session tokens when the integration is removed."""
    await _token_store(hass, entry.entry_id).async_remove()
