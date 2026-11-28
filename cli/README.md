# Mitsubishi Connect CLI

Interactive command-line interface for **Mitsubishi Motors Connected Services** (IDM & Kintaro API), built with [Typer](https://typer.tiangolo.com/) and [Rich](https://rich.readthedocs.io/) on top of the OpenAPI-generated Python client.

## Requirements

- Python 3.11+
- [`uv`](https://docs.astral.sh/uv/) (recommended)

## Installation

From the repository root:

```bash
uv sync
```

You can then invoke the CLI with:

```bash
uv run mitsubishi-connect --help
```

## Region & Configuration

Nothing region-specific or personal is hardcoded in the CLI. Regional backends, locales, timezones, and IDM/Kintaro parameters live in `../config/regions.toml`.

Built-in region profiles:
- `us` (default) — United States (`en-US`, `America/New_York`)
- `ca` — Canada (`en-CA`, `America/Toronto`)

You can select or override settings in three ways (highest priority first):

1. **CLI flags**:
   ```bash
   uv run mitsubishi-connect --region ca --timezone America/Vancouver status summary
   ```
2. **Environment variables**:
   - `MITSUBISHI_REGION` (e.g. `ca`, `us`)
   - `MITSUBISHI_CONFIG` (path to a custom TOML file)
   - `MITSUBISHI_COUNTRY`, `MITSUBISHI_LOCALE`, `MITSUBISHI_TIMEZONE`, `MITSUBISHI_TIMEZONE_OFFSET`
   - `MITSUBISHI_IDM_BASE_URL`, `MITSUBISHI_KINTARO_BASE_URL`
   - `MITSUBISHI_SESSION` (default: `~/.config/mitsubishi-connect/session.json`, `chmod 600`)
   - `MITSUBISHI_VIN`
   - `MITSUBISHI_EMAIL`, `MITSUBISHI_PASSWORD`, `MITSUBISHI_PIN` (optional; prompted securely if omitted)
3. **User config file** at `~/.config/mitsubishi-connect/config.toml` (merged on top of `config/regions.toml`):
   ```toml
   default_region = "us"

   [regions.us]
   locale = "en-US"
   timezone = "America/Chicago"
   ```

Inspect your active config at any time:

```bash
uv run mitsubishi-connect config regions
uv run mitsubishi-connect --region ca config show
```

## Quick Start

### 1. Test connectivity (no credentials required)

```bash
uv run mitsubishi-connect --region ca auth handshake
```

### 2. Log in

> **Tip**: Create a **secondary driver** account (with its own email/password) in the official Mitsubishi Motors app and use it here — otherwise, logging in with your primary account will sign you out of the mobile app for security reasons.

```bash
uv run mitsubishi-connect --region ca auth login
```

Your email and password are prompted interactively (password input is hidden), and tokens are saved to `~/.config/mitsubishi-connect/session.json` with `0600` permissions.

### 3. List vehicles & optionally set a default VIN

```bash
uv run mitsubishi-connect vehicle list
uv run mitsubishi-connect vehicle use JA4XXXXXXXXXXXXXX
```

### 4. Read vehicle telemetry (read-only)

```bash
uv run mitsubishi-connect status summary
uv run mitsubishi-connect status vsr
uv run mitsubishi-connect status engine
uv run mitsubishi-connect status refresh      # wakes vehicle for fresh telemetry
```

Add `--json` before any subcommand for machine-readable output (e.g. with `jq`):

```bash
uv run mitsubishi-connect --json status summary | jq '.vsr.data.diagnostic.odo'
```

## Command Reference

| Group | Commands | Description |
|---|---|---|
| `config` | `regions`, `show` | List region profiles and inspect active configuration |
| `auth` | `handshake`, `login`, `refresh`, `logout`, `verify-pin` | Connectivity check, login, token refresh, PIN validation |
| `vehicle` | `list`, `use`, `services` | Vehicle discovery and available remote services |
| `status` | `summary`, `vsr`, `engine`, `refresh` | Telemetry dashboard, raw VSR, engine/HVAC |
| `remote` | `start-engine`, `stop-engine`, `lock`, `unlock`, `location`, `horn`, `lights`, `poll` | Remote vehicle control and GPS |
| `alerts` | `curfew`, `geofence`, `speed` | Read configured vehicle alerts |
| `phev` | `charge-details`, `climate-details`, `soc`, `set-soc`, `start-charge`, `stop-charge`, `start-climate`, `stop-climate`, `schedule-charge`, `schedule-climate`, `schedule-charge-climate` | PHEV / EV charging, electric climate and schedules |

## Remote Command Examples

```bash
# Lock / unlock doors
uv run mitsubishi-connect remote lock
uv run mitsubishi-connect remote unlock

# Remote engine start with winter HVAC options (asks for safety confirmation + PIN)
uv run mitsubishi-connect remote start-engine \
  --temp 22 --unit C \
  --front-defrost --rear-defrost --steering-heater \
  --seat-fl 2

# Stop remote-started engine
uv run mitsubishi-connect remote stop-engine

# Find My Car (GPS location)
uv run mitsubishi-connect remote location
```

> **Safety warning**: Never run `remote start-engine` while the vehicle is parked in a closed or unventilated garage (carbon monoxide hazard).
