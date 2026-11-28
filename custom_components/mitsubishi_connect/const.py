"""Constants for the Mitsubishi Connect Home Assistant integration."""

from __future__ import annotations

DOMAIN = "mitsubishi_connect"

CONF_REGION = "region"
CONF_EMAIL = "email"
CONF_PASSWORD = "password"
CONF_PIN = "pin"
CONF_SCAN_INTERVAL = "scan_interval"
CONF_TEMP_UNIT = "temperature_unit"

DEFAULT_REGION = "us"
DEFAULT_SCAN_INTERVAL_MINUTES = 60
MIN_SCAN_INTERVAL_MINUTES = 15
MAX_SCAN_INTERVAL_MINUTES = 360

# Minimum cooldown between active vehicle wake/force-refresh calls (seconds)
FORCE_REFRESH_COOLDOWN_SECONDS = 600

# Proactive access token refresh margin before expiration (seconds)
TOKEN_REFRESH_MARGIN_SECONDS = 300

STORAGE_VERSION = 1

PLATFORMS: list[str] = [
    "sensor",
    "binary_sensor",
    "switch",
    "number",
    "button",
    "device_tracker",
]
