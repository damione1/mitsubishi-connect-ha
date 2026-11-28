"""Interactive CLI for Mitsubishi Motors Connected Services (Typer + Rich)."""

from __future__ import annotations

import asyncio
import json
from dataclasses import asdict, dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Annotated, Any

import typer
from mitsubishi_connect import (
    MitsubishiConnectError,
    MitsubishiConnectSDK,
    RegionConfig,
    SessionState,
    default_session_path,
    list_regions,
    load_region_config,
)
from mitsubishi_connect_api.models import HvacSettings
from mitsubishi_connect_api.types import UNSET
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()
err_console = Console(stderr=True)

app = typer.Typer(
    name="mitsubishi-connect",
    help="Interactive CLI for Mitsubishi Motors Connected Services (IDM & Kintaro API).",
    no_args_is_help=True,
    rich_markup_mode="rich",
)

config_app = typer.Typer(help="Inspect regional profiles and resolved configuration.", no_args_is_help=True)
auth_app = typer.Typer(help="Authentication, session handshake, and PIN verification.", no_args_is_help=True)
vehicle_app = typer.Typer(help="Vehicle discovery and available remote services.", no_args_is_help=True)
status_app = typer.Typer(help="Vehicle Status Report (VSR) and engine/HVAC state.", no_args_is_help=True)
remote_app = typer.Typer(help="Remote commands: engine, doors, location, horn, lights.", no_args_is_help=True)
alerts_app = typer.Typer(help="Inspect curfew, geofence, and speed alerts.", no_args_is_help=True)
phev_app = typer.Typer(help="PHEV / EV charging and electric climate endpoints.", no_args_is_help=True)

app.add_typer(config_app, name="config")
app.add_typer(auth_app, name="auth")
app.add_typer(vehicle_app, name="vehicle")
app.add_typer(status_app, name="status")
app.add_typer(remote_app, name="remote")
app.add_typer(alerts_app, name="alerts")
app.add_typer(phev_app, name="phev")


@dataclass
class CliContext:
    region: str | None
    config_path: Path | None
    country: str | None
    locale: str | None
    timezone: str | None
    session_path: Path
    vin: str | None
    as_json: bool


@app.callback()
def main_callback(
    ctx: typer.Context,
    region: Annotated[
        str | None,
        typer.Option("--region", "-r", envvar="MITSUBISHI_REGION", help="Region profile name from regions.toml (e.g. us, ca)."),
    ] = None,
    config_path: Annotated[
        Path | None,
        typer.Option("--config", "-c", envvar="MITSUBISHI_CONFIG", help="Path to custom TOML region config file."),
    ] = None,
    country: Annotated[
        str | None,
        typer.Option("--country", envvar="MITSUBISHI_COUNTRY", help="Override ISO-2 country code (e.g. US, CA)."),
    ] = None,
    locale: Annotated[
        str | None,
        typer.Option("--locale", envvar="MITSUBISHI_LOCALE", help="Override locale (e.g. en-US, en-CA, fr-CA)."),
    ] = None,
    timezone: Annotated[
        str | None,
        typer.Option("--timezone", envvar="MITSUBISHI_TIMEZONE", help="Override IANA timezone (e.g. America/New_York)."),
    ] = None,
    session_path: Annotated[
        Path | None,
        typer.Option("--session", "-s", envvar="MITSUBISHI_SESSION", help="Path to session token JSON file (chmod 600)."),
    ] = None,
    vin: Annotated[
        str | None,
        typer.Option("--vin", envvar="MITSUBISHI_VIN", help="Target 17-character VIN (defaults to saved/primary vehicle)."),
    ] = None,
    as_json: Annotated[
        bool,
        typer.Option("--json", help="Emit raw JSON output (ideal for scripting and jq)."),
    ] = False,
) -> None:
    ctx.obj = CliContext(
        region=region,
        config_path=config_path,
        country=country,
        locale=locale,
        timezone=timezone,
        session_path=session_path or default_session_path(),
        vin=vin,
        as_json=as_json,
    )


def _load_state(cli: CliContext) -> SessionState:
    if cli.session_path.is_file():
        return SessionState.load(cli.session_path)
    return SessionState.create_new(region=cli.region or "us")


def _resolve_config(cli: CliContext, state: SessionState | None = None) -> RegionConfig:
    region_name = cli.region or (state.region if state else None)
    return load_region_config(
        region_name,
        config_path=cli.config_path,
        country=cli.country,
        locale=cli.locale,
        timezone=cli.timezone,
    )


def _emit_json(data: Any) -> None:
    console.print_json(json.dumps(data, default=str))


def _require_logged_in(state: SessionState) -> None:
    if not state.access_token:
        err_console.print(
            "[bold red]Not authenticated.[/bold red] Run [cyan]mitsubishi-connect auth login[/cyan] first."
        )
        raise typer.Exit(code=2)


async def _pick_vehicle(
    sdk: MitsubishiConnectSDK, cli: CliContext
) -> tuple[str, str | None, dict[str, Any]]:
    vehicles = await sdk.get_vehicles()
    if not vehicles:
        raise MitsubishiConnectError("No vehicles found on this account.")
    target_vin = cli.vin or sdk.state.default_vin
    chosen = vehicles[0]
    if target_vin:
        matched = [v for v in vehicles if v.vin == target_vin]
        if not matched:
            raise MitsubishiConnectError(f"VIN '{target_vin}' not found on this account.")
        chosen = matched[0]
    sdk.set_vehicle_context(chosen)
    v_dict = chosen.to_dict()
    internal_vin = None if chosen.internal_vin is UNSET else chosen.internal_vin
    return chosen.vin, internal_vin, v_dict


def _run_async(coro: Any) -> Any:
    try:
        return asyncio.run(coro)
    except MitsubishiConnectError as exc:
        err_console.print(f"[bold red]API Error[/bold red] (code={exc.code}): {exc}")
        raise typer.Exit(code=1) from exc
    except ValueError as exc:
        err_console.print(f"[bold red]Configuration Error:[/bold red] {exc}")
        raise typer.Exit(code=2) from exc


# ============================================================================
# CONFIG COMMANDS
# ============================================================================


@config_app.command("regions")
def cmd_config_regions(ctx: typer.Context) -> None:
    """List available region profiles."""
    cli: CliContext = ctx.obj
    regions = list_regions(cli.config_path)
    if cli.as_json:
        _emit_json({"regions": regions})
        return
    table = Table(title="Available Region Profiles")
    table.add_column("Profile", style="cyan")
    table.add_column("Country")
    table.add_column("Locale")
    table.add_column("Timezone")
    table.add_column("Kintaro Base URL", style="dim")
    for name in regions:
        cfg = load_region_config(name, config_path=cli.config_path)
        table.add_row(name, cfg.country, cfg.locale, cfg.timezone, cfg.kintaro_base_url)
    console.print(table)


@config_app.command("show")
def cmd_config_show(ctx: typer.Context) -> None:
    """Display the currently resolved configuration (with secrets redacted)."""
    cli: CliContext = ctx.obj
    state = _load_state(cli)
    cfg = _resolve_config(cli, state)
    safe = asdict(cfg)
    for secret_key in ("idm_client_secret", "idm_aes_key", "kintaro_app_hash", "jwt_sign_key"):
        if safe.get(secret_key):
            safe[secret_key] = safe[secret_key][:4] + "…" + safe[secret_key][-4:]
    safe["session_path"] = str(cli.session_path)
    safe["authenticated"] = bool(state.access_token)
    safe["default_vin"] = state.default_vin
    if cli.as_json:
        _emit_json(safe)
        return
    table = Table(title=f"Resolved Configuration (region={cfg.name})")
    table.add_column("Key", style="cyan")
    table.add_column("Value")
    for k, v in safe.items():
        table.add_row(k, str(v))
    console.print(table)


# ============================================================================
# AUTH COMMANDS
# ============================================================================


@auth_app.command("handshake")
def cmd_auth_handshake(ctx: typer.Context) -> None:
    """Test unauthenticated connectivity (IDM /init + Kintaro /checkVersion)."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            key_index, pubkey = await sdk.idm_init()
            enc_key, sign_key = await sdk.handshake()
            return {
                "region": cfg.name,
                "idm_init": {"ok": True, "keyIndex": key_index, "publicKeyLen": len(pubkey)},
                "kintaro_handshake": {"ok": True, "encKeyLen": len(enc_key), "signKeyLen": len(sign_key)},
            }

    res = _run_async(_go())
    if cli.as_json:
        _emit_json(res)
    else:
        console.print(
            Panel.fit(
                f"[green]IDM /api/v1/init[/green] OK (keyIndex={res['idm_init']['keyIndex']})\n"
                f"[green]Kintaro /service/checkVersion[/green] OK "
                f"(encKey={res['kintaro_handshake']['encKeyLen']}B, signKey={res['kintaro_handshake']['signKeyLen']}B)",
                title=f"Handshake OK ({res['region']})",
            )
        )


@auth_app.command("login")
def cmd_auth_login(
    ctx: typer.Context,
    email: Annotated[str | None, typer.Option("--email", "-u", envvar="MITSUBISHI_EMAIL", help="Account email.")] = None,
    password: Annotated[str | None, typer.Option("--password", "-p", envvar="MITSUBISHI_PASSWORD", help="Account password (prompted securely if omitted).")] = None,
) -> None:
    """Authenticate via IDM and save session tokens securely (chmod 600)."""
    cli: CliContext = ctx.obj
    user_email = email or typer.prompt("Mitsubishi Connect email")
    user_pw = password or typer.prompt("Password", hide_input=True)

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        cfg = _resolve_config(cli, state)
        state.region = cfg.name
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            with console.status("Authenticating with IDM and Kintaro…"):
                tokens = await sdk.login(user_email, user_pw)
            sdk.state.save(cli.session_path)
            return {
                "authenticated": True,
                "region": cfg.name,
                "expiresIn": tokens.get("expiresIn"),
                "sessionPath": str(cli.session_path),
            }

    res = _run_async(_go())
    if cli.as_json:
        _emit_json(res)
    else:
        console.print(
            f"[bold green]Login successful![/bold green] "
            f"Session saved to [cyan]{res['sessionPath']}[/cyan] (chmod 600, expiresIn={res['expiresIn']}s)."
        )


@auth_app.command("refresh")
def cmd_auth_refresh(ctx: typer.Context) -> None:
    """Refresh the IDM access token using the stored refresh token."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            await sdk.refresh_token()
            sdk.state.save(cli.session_path)
            return {"refreshed": True, "sessionPath": str(cli.session_path)}

    res = _run_async(_go())
    if cli.as_json:
        _emit_json(res)
    else:
        console.print("[green]Access token refreshed and saved.[/green]")


@auth_app.command("logout")
def cmd_auth_logout(ctx: typer.Context) -> None:
    """Delete the local session token file."""
    cli: CliContext = ctx.obj
    if cli.session_path.is_file():
        cli.session_path.unlink()
        console.print(f"[yellow]Removed session file:[/yellow] {cli.session_path}")
    else:
        console.print("No local session file found.")


@auth_app.command("verify-pin")
def cmd_auth_verify_pin(
    ctx: typer.Context,
    pin: Annotated[str | None, typer.Option("--pin", envvar="MITSUBISHI_PIN", help="4-digit security PIN.")] = None,
) -> None:
    """Verify your 4-digit security PIN against the backend."""
    cli: CliContext = ctx.obj
    user_pin = pin or typer.prompt("4-digit PIN", hide_input=True)

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.verify_pin(vin, user_pin, ivin)
            sdk.state.save(cli.session_path)
            return res

    res = _run_async(_go())
    if cli.as_json:
        _emit_json(res)
    else:
        ok = res.get("isValidPIN")
        console.print("[bold green]PIN is valid.[/bold green]" if ok else "[bold red]PIN is invalid.[/bold red]")


# ============================================================================
# VEHICLE COMMANDS
# ============================================================================


@vehicle_app.command("list")
def cmd_vehicle_list(ctx: typer.Context) -> None:
    """List all vehicles registered on the account."""
    cli: CliContext = ctx.obj

    async def _go() -> list[dict[str, Any]]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vehicles = await sdk.get_vehicles()
            sdk.state.save(cli.session_path)
            return [v.to_dict() for v in vehicles]

    items = _run_async(_go())
    if cli.as_json:
        _emit_json(items)
        return
    table = Table(title="Registered Vehicles")
    table.add_column("VIN", style="cyan")
    table.add_column("Model")
    table.add_column("Year")
    table.add_column("Color")
    table.add_column("Country")
    table.add_column("State", style="green")
    for v in items:
        model = v.get("model") or {}
        color = v.get("exteriorColor") or {}
        conn = v.get("vehicleConnectivity") or {}
        table.add_row(
            str(v.get("vin", "")),
            str(model.get("bodyWork") or v.get("nickName") or ""),
            str(model.get("modelYear") or ""),
            str(color.get("description") or color.get("code") or ""),
            str(v.get("vehicleCountryCode") or ""),
            str(conn.get("state") or ""),
        )
    console.print(table)


@vehicle_app.command("use")
def cmd_vehicle_use(
    ctx: typer.Context,
    vin: Annotated[str, typer.Argument(help="17-character VIN to save as default.")],
) -> None:
    """Save a default VIN in the local session file."""
    cli: CliContext = ctx.obj
    state = _load_state(cli)
    state.default_vin = vin
    state.save(cli.session_path)
    console.print(f"[green]Default VIN set to[/green] [cyan]{vin}[/cyan].")
@vehicle_app.command("services")
def cmd_vehicle_services(ctx: typer.Context) -> None:
    """List active remote services on the vehicle subscription."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.get_available_services(vin, internal_vin=ivin)
            sdk.state.save(cli.session_path)
            return res

    res = _run_async(_go())
    if cli.as_json:
        _emit_json(res)
        return
    table = Table(title="Available Remote Services")
    table.add_column("Service ID", style="cyan")
    table.add_column("Active")
    table.add_column("Visible")
    table.add_column("Version")
    for s in res.get("services") or []:
        active = "[green]Yes[/green]" if s.get("isActive") else "[dim]No[/dim]"
        table.add_row(
            str(s.get("availableServiceId")),
            active,
            str(s.get("isUIVisible")),
            str(s.get("version") or ""),
        )
    console.print(table)

# ============================================================================
# STATUS & TELEMETRY COMMANDS
# ============================================================================


@status_app.command("summary")
def cmd_status_summary(ctx: typer.Context) -> None:
    """Fetch cached VSR telemetry + engine/HVAC state in a clean dashboard view."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, v_dict = await _pick_vehicle(sdk, cli)
            vsr, engine = await asyncio.gather(
                sdk.get_vsr(vin, ivin),
                sdk.get_engine_details(vin, ivin),
            )
            sdk.state.save(cli.session_path)
            return {"vehicle": v_dict, "vsr": vsr, "engine": engine}

    res = _run_async(_go())
    if cli.as_json:
        _emit_json(res)
        return

    vsr_data = (res.get("vsr") or {}).get("data") or {}
    diag = vsr_data.get("diagnostic") or {}
    vstatus = vsr_data.get("vehicleStatus") or {}
    engine = res.get("engine") or {}

    table = Table(title=f"Vehicle Status — {res['vehicle'].get('vin')}")
    table.add_column("Metric", style="cyan")
    table.add_column("Value")
    odo = (diag.get("odo") or {}).get("value")
    rng = (diag.get("availRange") or {}).get("value")
    unit = "km" if (diag.get("odos") or {}).get("displayMessage", "").endswith("km") else "mi"
    table.add_row("Odometer", f"{odo} {unit}" if odo is not None else "—")
    table.add_row("Available Range", f"{rng} {unit}" if rng is not None else "—")
    table.add_row("Engine Running", "[bold green]ON[/bold green]" if engine.get("isEngineOn") else "OFF")
    if engine.get("targetTemperature") is not None:
        table.add_row("Target Cabin Temp", f"{engine.get('targetTemperature')} °{engine.get('temperatureUnit', 'C')}")

    doors = (vstatus.get("doorStatus") or {}).get("doors") or []
    open_doors = [
        (d.get("position") or {}).get("displayMessage", "door")
        for d in doors
        if (d.get("state") or {}).get("value") not in (None, "0")
    ]
    table.add_row(
        "Doors / Hood / Trunk",
        "[bold red]" + ", ".join(open_doors) + "[/bold red]" if open_doors else f"[green]All closed ({len(doors)})[/green]",
    )
    windows = (vstatus.get("windowStatus") or {}).get("windows") or []
    if windows:
        open_win = [
            (w.get("position") or {}).get("displayMessage", "window")
            for w in windows
            if (w.get("state") or {}).get("value") not in (None, "0")
        ]
        table.add_row(
            "Windows",
            "[bold yellow]" + ", ".join(open_win) + "[/bold yellow]" if open_win else f"[green]All closed ({len(windows)})[/green]",
        )
    console.print(table)


@status_app.command("vsr")
def cmd_status_vsr(ctx: typer.Context) -> None:
    """Dump full cached Vehicle Status Report (VSR) JSON."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.get_vsr(vin, ivin)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))


@status_app.command("engine")
def cmd_status_engine(ctx: typer.Context) -> None:
    """Dump remote engine and HVAC settings."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.get_engine_details(vin, ivin)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))


@status_app.command("refresh")
def cmd_status_refresh(
    ctx: typer.Context,
    refresh_type: Annotated[int, typer.Option("--type", help="VSR refresh type code (default 1 = HomePullDown).")] = 1,
    no_wait: Annotated[bool, typer.Option("--no-wait", help="Return immediately without polling.")] = False,
) -> None:
    """Request a live VSR telemetry refresh from the vehicle."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            with console.status("Requesting live telemetry from vehicle…"):
                poll = await sdk.refresh_vsr(
                    vin, internal_vin=ivin, refresh_type=refresh_type, wait=not no_wait
                )
                vsr = await sdk.get_vsr(vin, ivin) if not no_wait else None
            sdk.state.save(cli.session_path)
            return {"refresh": poll, "vsr": vsr}

    _emit_json(_run_async(_go()))
# ============================================================================
# REMOTE COMMANDS
# ============================================================================


@remote_app.command("start-engine")
def cmd_remote_start_engine(
    ctx: typer.Context,
    temp: Annotated[float, typer.Option("--temp", "-t", help="Target cabin temperature.")] = 21.0,
    unit: Annotated[str, typer.Option("--unit", "-u", help="Temperature unit: C or F.")] = "C",
    front_defrost: Annotated[bool, typer.Option("--front-defrost", help="Enable front windshield defrost.")] = False,
    rear_defrost: Annotated[bool, typer.Option("--rear-defrost", help="Enable rear window defrost.")] = False,
    steering_heater: Annotated[bool, typer.Option("--steering-heater", help="Enable heated steering wheel.")] = False,
    seat_fl: Annotated[int | None, typer.Option("--seat-fl", min=0, max=3, help="Front-left heated seat level (0-3).")] = None,
    seat_fr: Annotated[int | None, typer.Option("--seat-fr", min=0, max=3, help="Front-right heated seat level (0-3).")] = None,
    seat_rl: Annotated[int | None, typer.Option("--seat-rl", min=0, max=3, help="Rear-left heated seat level (0-3).")] = None,
    seat_rr: Annotated[int | None, typer.Option("--seat-rr", min=0, max=3, help="Rear-right heated seat level (0-3).")] = None,
    pin: Annotated[str | None, typer.Option("--pin", envvar="MITSUBISHI_PIN", help="4-digit PIN (prompted securely if omitted).")] = None,
    yes: Annotated[bool, typer.Option("--yes", "-y", help="Confirm vehicle is in an open/ventilated area (skip safety prompt).")] = False,
    no_wait: Annotated[bool, typer.Option("--no-wait", help="Return immediately without polling.")] = False,
) -> None:
    """Start the engine remotely (requires PIN)."""
    cli: CliContext = ctx.obj
    if not yes:
        typer.confirm(
            "Safety check: confirm the vehicle is parked in an open, ventilated area (never in a closed garage). Proceed?",
            abort=True,
        )
    user_pin = pin or typer.prompt("4-digit PIN", hide_input=True)

    hvac: HvacSettings | None = None
    if any(
        x not in (False, None)
        for x in (front_defrost, rear_defrost, steering_heater, seat_fl, seat_fr, seat_rl, seat_rr)
    ):
        hvac = HvacSettings(
            front_defrost_status=1 if front_defrost else 0,
            rear_defrost_status=1 if rear_defrost else 0,
            steering_heater_status=1 if steering_heater else 0,
            front_left_seat_status=seat_fl if seat_fl is not None else 0,
            front_right_seat_status=seat_fr if seat_fr is not None else 0,
            rear_left_seat_status=seat_rl if seat_rl is not None else 0,
            rear_right_seat_status=seat_rr if seat_rr is not None else 0,
        )

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            with console.status("Starting engine and polling vehicle response…"):
                res = await sdk.start_engine(
                    vin,
                    pin=user_pin,
                    target_temperature=temp,
                    temperature_unit=unit,
                    hvac_settings=hvac,
                    internal_vin=ivin,
                    wait=not no_wait,
                )
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))


@remote_app.command("stop-engine")
def cmd_remote_stop_engine(
    ctx: typer.Context,
    pin: Annotated[str | None, typer.Option("--pin", envvar="MITSUBISHI_PIN", help="Optional 4-digit PIN (not required on most trims).")] = None,
    no_wait: Annotated[bool, typer.Option("--no-wait", help="Return immediately without polling.")] = False,
) -> None:
    """Stop a remote-started engine."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            with console.status("Stopping engine and polling vehicle response…"):
                res = await sdk.stop_engine(vin, pin=pin, internal_vin=ivin, wait=not no_wait)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))


@remote_app.command("lock")
def cmd_remote_lock(
    ctx: typer.Context,
    pin: Annotated[str | None, typer.Option("--pin", envvar="MITSUBISHI_PIN", help="Optional 4-digit PIN.")] = None,
    no_wait: Annotated[bool, typer.Option("--no-wait", help="Return immediately without polling.")] = False,
) -> None:
    """Lock the doors remotely."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            with console.status("Locking doors…"):
                res = await sdk.lock_door(vin, pin=pin, internal_vin=ivin, wait=not no_wait)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))


@remote_app.command("unlock")
def cmd_remote_unlock(
    ctx: typer.Context,
    pin: Annotated[str | None, typer.Option("--pin", envvar="MITSUBISHI_PIN", help="4-digit PIN (prompted securely if omitted).")] = None,
    no_wait: Annotated[bool, typer.Option("--no-wait", help="Return immediately without polling.")] = False,
) -> None:
    """Unlock the doors remotely (requires PIN)."""
    cli: CliContext = ctx.obj
    user_pin = pin or typer.prompt("4-digit PIN", hide_input=True)

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            with console.status("Unlocking doors…"):
                res = await sdk.unlock_door(vin, pin=user_pin, internal_vin=ivin, wait=not no_wait)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))


@remote_app.command("location")
def cmd_remote_location(
    ctx: typer.Context,
    pin: Annotated[str | None, typer.Option("--pin", envvar="MITSUBISHI_PIN", help="Optional 4-digit PIN.")] = None,
) -> None:
    """Fetch vehicle GPS location (Find My Car)."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.get_location(vin, pin=pin, internal_vin=ivin)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))


@remote_app.command("horn")
def cmd_remote_horn(
    ctx: typer.Context,
    pin: Annotated[str | None, typer.Option("--pin", envvar="MITSUBISHI_PIN", help="Optional 4-digit PIN.")] = None,
    no_wait: Annotated[bool, typer.Option("--no-wait", help="Return immediately without polling.")] = False,
) -> None:
    """Sound the horn remotely."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.start_horn(vin, pin=pin, internal_vin=ivin, wait=not no_wait)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))


@remote_app.command("lights")
def cmd_remote_lights(
    ctx: typer.Context,
    pin: Annotated[str | None, typer.Option("--pin", envvar="MITSUBISHI_PIN", help="Optional 4-digit PIN.")] = None,
    no_wait: Annotated[bool, typer.Option("--no-wait", help="Return immediately without polling.")] = False,
) -> None:
    """Flash headlights remotely."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.start_light(vin, pin=pin, internal_vin=ivin, wait=not no_wait)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))

@remote_app.command("poll")
def cmd_remote_poll(
    ctx: typer.Context,
    request_id: Annotated[str, typer.Argument(help="Request ID returned by an async remote command.")],
) -> None:
    """Poll status of an existing remote command requestId."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            res = await sdk.poll_request(request_id)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))


# ============================================================================
# ALERTS COMMANDS
# ============================================================================


@alerts_app.command("curfew")
def cmd_alerts_curfew(ctx: typer.Context) -> None:
    """List configured curfew alerts."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.get_curfew_alert(vin, ivin)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))


@alerts_app.command("geofence")
def cmd_alerts_geofence(ctx: typer.Context) -> None:
    """List configured geofence alerts."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.get_geofence_alert(vin, ivin)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))


@alerts_app.command("speed")
def cmd_alerts_speed(ctx: typer.Context) -> None:
    """List configured speed alerts."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.get_speed_alert(vin, ivin)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))


# ============================================================================
# PHEV / EV COMMANDS
# ============================================================================


@phev_app.command("charge-details")
def cmd_phev_charge_details(ctx: typer.Context) -> None:
    """Get battery and charging status (PHEV/EV models)."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.get_charge_details(vin, internal_vin=ivin)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))


@phev_app.command("start-charge")
def cmd_phev_start_charge(
    ctx: typer.Context,
    pin: Annotated[str | None, typer.Option("--pin", envvar="MITSUBISHI_PIN")] = None,
    no_wait: Annotated[bool, typer.Option("--no-wait")] = False,
) -> None:
    """Start charging (PHEV/EV models)."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.start_charge(vin, pin=pin, internal_vin=ivin, wait=not no_wait)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))


@phev_app.command("stop-charge")
def cmd_phev_stop_charge(
    ctx: typer.Context,
    pin: Annotated[str | None, typer.Option("--pin", envvar="MITSUBISHI_PIN")] = None,
    no_wait: Annotated[bool, typer.Option("--no-wait")] = False,
) -> None:
    """Stop charging (PHEV/EV models)."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.stop_charge(vin, pin=pin, internal_vin=ivin, wait=not no_wait)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))


@phev_app.command("start-climate")
def cmd_phev_start_climate(
    ctx: typer.Context,
    temp: Annotated[float, typer.Option("--temp", "-t")] = 21.0,
    unit: Annotated[str, typer.Option("--unit", "-u")] = "C",
    pin: Annotated[str | None, typer.Option("--pin", envvar="MITSUBISHI_PIN")] = None,
    no_wait: Annotated[bool, typer.Option("--no-wait")] = False,
) -> None:
    """Start electric climate control (PHEV/EV models)."""
    cli: CliContext = ctx.obj
    user_pin = pin or typer.prompt("4-digit PIN", hide_input=True)

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.start_climate(
                vin,
                pin=user_pin,
                target_temperature=temp,
                temperature_unit=unit,
                internal_vin=ivin,
                wait=not no_wait,
            )
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))


@phev_app.command("stop-climate")
def cmd_phev_stop_climate(
    ctx: typer.Context,
    pin: Annotated[str | None, typer.Option("--pin", envvar="MITSUBISHI_PIN")] = None,
    no_wait: Annotated[bool, typer.Option("--no-wait")] = False,
) -> None:
    """Stop electric climate control (PHEV/EV models)."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.stop_climate(vin, pin=pin, internal_vin=ivin, wait=not no_wait)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))



@phev_app.command("climate-details")
def cmd_phev_climate_details(ctx: typer.Context) -> None:
    """Get electric climate preconditioning status (PHEV/EV models)."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.get_climate_details(vin, internal_vin=ivin)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))

@phev_app.command("soc")
def cmd_phev_soc(ctx: typer.Context) -> None:
    """Get the charge limit and notification thresholds (PHEV/EV models)."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.get_soc_setting(vin, internal_vin=ivin)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))

@phev_app.command("set-soc")
def cmd_phev_set_soc(
    ctx: typer.Context,
    limit: Annotated[
        str | None, typer.Option("--limit", help="Charging limit threshold, e.g. 80.")
    ] = None,
    notify: Annotated[
        str | None,
        typer.Option("--notify", help="Charging notification threshold, e.g. 80."),
    ] = None,
) -> None:
    """Set the charge limit and notification thresholds (PHEV/EV models)."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.set_soc_setting(
                vin, charging_limit=limit, charging_notification=notify, internal_vin=ivin
            )
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))

@phev_app.command("schedule-charge")
def cmd_phev_schedule_charge(ctx: typer.Context) -> None:
    """Get the charging schedule (PHEV/EV models)."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.get_charge_schedule(vin, internal_vin=ivin)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))

@phev_app.command("schedule-climate")
def cmd_phev_schedule_climate(ctx: typer.Context) -> None:
    """Get the climate schedule (PHEV/EV models)."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.get_climate_schedule(vin, internal_vin=ivin)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))

@phev_app.command("schedule-charge-climate")
def cmd_phev_schedule_charge_climate(ctx: typer.Context) -> None:
    """Get the combined charge and climate schedule (PHEV/EV models)."""
    cli: CliContext = ctx.obj

    async def _go() -> dict[str, Any]:
        state = _load_state(cli)
        _require_logged_in(state)
        cfg = _resolve_config(cli, state)
        async with MitsubishiConnectSDK(cfg, state) as sdk:
            vin, ivin, _ = await _pick_vehicle(sdk, cli)
            res = await sdk.get_charge_climate_schedule(vin, internal_vin=ivin)
            sdk.state.save(cli.session_path)
            return res

    _emit_json(_run_async(_go()))
