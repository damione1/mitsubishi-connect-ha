"""Config flow, options flow, and reauthentication flow for Mitsubishi Connect."""

from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.selector import (
    NumberSelector,
    NumberSelectorConfig,
    NumberSelectorMode,
    SelectSelector,
    SelectSelectorConfig,
    SelectSelectorMode,
    TextSelector,
    TextSelectorConfig,
    TextSelectorType,
)
from homeassistant.helpers.storage import Store

from .api import MitsubishiApiClient, MitsubishiApiError, MitsubishiAuthError, TokenBundle
from .const import (
    CONF_EMAIL,
    CONF_PASSWORD,
    CONF_PIN,
    CONF_REGION,
    CONF_SCAN_INTERVAL,
    CONF_TEMP_UNIT,
    DEFAULT_REGION,
    DEFAULT_SCAN_INTERVAL_MINUTES,
    DOMAIN,
    MAX_SCAN_INTERVAL_MINUTES,
    MIN_SCAN_INTERVAL_MINUTES,
    STORAGE_VERSION,
)
from .regions import REGIONS

_LOGGER = logging.getLogger(__name__)


class MitsubishiConnectConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Mitsubishi Connect."""

    VERSION = 1

    def __init__(self) -> None:
        self._reauth_entry: config_entries.ConfigEntry | None = None

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        errors: dict[str, str] = {}

        if user_input is not None:
            email = user_input[CONF_EMAIL].strip().lower()
            region = user_input[CONF_REGION]
            password = user_input[CONF_PASSWORD]
            pin = (user_input.get(CONF_PIN) or "").strip()

            await self.async_set_unique_id(f"{region}_{email}")
            self._abort_if_unique_id_configured()

            profile = REGIONS[region]
            tokens = TokenBundle.new()
            api = MitsubishiApiClient(
                session=async_get_clientsession(self.hass),
                profile=profile,
                tokens=tokens,
            )
            try:
                await api.login(email, password)
                await api.get_vehicles()
            except MitsubishiAuthError:
                errors["base"] = "invalid_auth"
            except MitsubishiApiError:
                errors["base"] = "cannot_connect"
            except Exception:  # noqa: BLE001
                _LOGGER.exception("Unexpected error during Mitsubishi Connect login")
                errors["base"] = "unknown"
            else:
                data = {
                    CONF_REGION: region,
                    CONF_EMAIL: email,
                    CONF_PASSWORD: password,
                    CONF_PIN: pin,
                    CONF_SCAN_INTERVAL: int(
                        user_input.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL_MINUTES)
                    ),
                    CONF_TEMP_UNIT: "C" if region == "ca" else "F",
                }
                return self.async_create_entry(
                    title=f"Mitsubishi Connect ({email})",
                    data=data,
                )

        region_options = [{"value": k, "label": v.label} for k, v in REGIONS.items()]
        schema = vol.Schema(
            {
                vol.Required(CONF_REGION, default=DEFAULT_REGION): SelectSelector(
                    SelectSelectorConfig(
                        options=region_options, mode=SelectSelectorMode.DROPDOWN
                    )
                ),
                vol.Required(CONF_EMAIL): TextSelector(
                    TextSelectorConfig(type=TextSelectorType.EMAIL)
                ),
                vol.Required(CONF_PASSWORD): TextSelector(
                    TextSelectorConfig(type=TextSelectorType.PASSWORD)
                ),
                vol.Optional(CONF_PIN, default=""): TextSelector(
                    TextSelectorConfig(type=TextSelectorType.PASSWORD)
                ),
                vol.Optional(
                    CONF_SCAN_INTERVAL, default=DEFAULT_SCAN_INTERVAL_MINUTES
                ): NumberSelector(
                    NumberSelectorConfig(
                        min=MIN_SCAN_INTERVAL_MINUTES,
                        max=MAX_SCAN_INTERVAL_MINUTES,
                        step=5,
                        unit_of_measurement="min",
                        mode=NumberSelectorMode.BOX,
                    )
                ),
            }
        )
        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)

    async def async_step_reauth(self, entry_data: dict[str, Any]) -> FlowResult:
        """Handle reauthentication when tokens expire or are revoked."""
        self._reauth_entry = self.hass.config_entries.async_get_entry(
            self.context["entry_id"]
        )
        return await self.async_step_reauth_confirm()

    async def async_step_reauth_confirm(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        errors: dict[str, str] = {}
        assert self._reauth_entry is not None
        region = self._reauth_entry.data.get(CONF_REGION, DEFAULT_REGION)
        email = self._reauth_entry.data[CONF_EMAIL]

        if user_input is not None:
            password = user_input[CONF_PASSWORD]
            profile = REGIONS[region]
            store: Store[dict] = Store(
                self.hass, STORAGE_VERSION, f"{DOMAIN}.{self._reauth_entry.entry_id}.tokens"
            )
            stored = await store.async_load()
            tokens = TokenBundle.from_dict(stored) if isinstance(stored, dict) else TokenBundle.new()

            api = MitsubishiApiClient(
                session=async_get_clientsession(self.hass),
                profile=profile,
                tokens=tokens,
            )
            try:
                await api.login(email, password)
            except MitsubishiAuthError:
                errors["base"] = "invalid_auth"
            except MitsubishiApiError:
                errors["base"] = "cannot_connect"
            else:
                await store.async_save(api.tokens.to_dict())
                new_data = {**self._reauth_entry.data, CONF_PASSWORD: password}
                self.hass.config_entries.async_update_entry(self._reauth_entry, data=new_data)
                await self.hass.config_entries.async_reload(self._reauth_entry.entry_id)
                return self.async_abort(reason="reauth_successful")

        schema = vol.Schema(
            {
                vol.Required(CONF_PASSWORD): TextSelector(
                    TextSelectorConfig(type=TextSelectorType.PASSWORD)
                )
            }
        )
        return self.async_show_form(
            step_id="reauth_confirm",
            data_schema=schema,
            description_placeholders={"email": email},
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> MitsubishiConnectOptionsFlow:
        return MitsubishiConnectOptionsFlow(config_entry)


class MitsubishiConnectOptionsFlow(config_entries.OptionsFlow):
    """Options flow for poll interval, PIN, and temperature unit."""

    def __init__(self, entry: config_entries.ConfigEntry) -> None:
        self._entry = entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        if user_input is not None:
            return self.async_create_entry(
                title="",
                data={
                    CONF_PIN: (user_input.get(CONF_PIN) or "").strip(),
                    CONF_SCAN_INTERVAL: int(user_input[CONF_SCAN_INTERVAL]),
                    CONF_TEMP_UNIT: user_input[CONF_TEMP_UNIT],
                },
            )

        current_pin = self._entry.options.get(
            CONF_PIN, self._entry.data.get(CONF_PIN, "")
        )
        current_interval = self._entry.options.get(
            CONF_SCAN_INTERVAL,
            self._entry.data.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL_MINUTES),
        )
        current_unit = self._entry.options.get(
            CONF_TEMP_UNIT, self._entry.data.get(CONF_TEMP_UNIT, "C")
        )

        schema = vol.Schema(
            {
                vol.Optional(CONF_PIN, default=current_pin): TextSelector(
                    TextSelectorConfig(type=TextSelectorType.PASSWORD)
                ),
                vol.Required(CONF_SCAN_INTERVAL, default=current_interval): NumberSelector(
                    NumberSelectorConfig(
                        min=MIN_SCAN_INTERVAL_MINUTES,
                        max=MAX_SCAN_INTERVAL_MINUTES,
                        step=5,
                        unit_of_measurement="min",
                        mode=NumberSelectorMode.BOX,
                    )
                ),
                vol.Required(CONF_TEMP_UNIT, default=current_unit): SelectSelector(
                    SelectSelectorConfig(
                        options=[
                            {"value": "C", "label": "Celsius (°C)"},
                            {"value": "F", "label": "Fahrenheit (°F)"},
                        ],
                        mode=SelectSelectorMode.DROPDOWN,
                    )
                ),
            }
        )
        return self.async_show_form(step_id="init", data_schema=schema)
