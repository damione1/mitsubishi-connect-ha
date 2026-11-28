from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vehicle_cruising_range_entity import VehicleCruisingRangeEntity
    from ..models.vehicle_tire_status_entity import VehicleTireStatusEntity
    from ..models.vsr_metric import VsrMetric


T = TypeVar("T", bound="VsrDiagnostic")


@_attrs_define
class VsrDiagnostic:
    """
    Attributes:
        abs_warn (VsrMetric | Unset):
        afu_failure (VsrMetric | Unset):
        airbag_warn (VsrMetric | Unset):
        avail_range (VsrMetric | Unset):
        battery_high_warning (VsrMetric | Unset):
        battery_life (VsrMetric | Unset):
        battery_low_warning (VsrMetric | Unset):
        break_warn (VsrMetric | Unset):
        cruising_range_first (VehicleCruisingRangeEntity | Unset):
        cruising_range_second (VehicleCruisingRangeEntity | Unset):
        digsts (None | str | Unset):
        dtc_status (VsrMetric | Unset):
        emergency_braking_warning (VsrMetric | Unset):
        engine_oil_warn (VsrMetric | Unset):
        ev_alert_crbs_failure_display (VsrMetric | Unset):
        ev_battery_level_warning (VsrMetric | Unset):
        event_timestamp (VsrMetric | Unset):
        fuel_level (VsrMetric | Unset):
        igst (VsrMetric | Unset):
        mil_status (VsrMetric | Unset):
        odo (VsrMetric | Unset):
        odos (VsrMetric | Unset):
        power_limitation_alert (VsrMetric | Unset):
        power_steering_warning (VsrMetric | Unset):
        spd (VsrMetric | Unset):
        tire_status (VehicleTireStatusEntity | Unset):
        v_2l_system_status_display (VsrMetric | Unset):
        washer_warn (VsrMetric | Unset):
    """

    abs_warn: VsrMetric | Unset = UNSET
    afu_failure: VsrMetric | Unset = UNSET
    airbag_warn: VsrMetric | Unset = UNSET
    avail_range: VsrMetric | Unset = UNSET
    battery_high_warning: VsrMetric | Unset = UNSET
    battery_life: VsrMetric | Unset = UNSET
    battery_low_warning: VsrMetric | Unset = UNSET
    break_warn: VsrMetric | Unset = UNSET
    cruising_range_first: VehicleCruisingRangeEntity | Unset = UNSET
    cruising_range_second: VehicleCruisingRangeEntity | Unset = UNSET
    digsts: None | str | Unset = UNSET
    dtc_status: VsrMetric | Unset = UNSET
    emergency_braking_warning: VsrMetric | Unset = UNSET
    engine_oil_warn: VsrMetric | Unset = UNSET
    ev_alert_crbs_failure_display: VsrMetric | Unset = UNSET
    ev_battery_level_warning: VsrMetric | Unset = UNSET
    event_timestamp: VsrMetric | Unset = UNSET
    fuel_level: VsrMetric | Unset = UNSET
    igst: VsrMetric | Unset = UNSET
    mil_status: VsrMetric | Unset = UNSET
    odo: VsrMetric | Unset = UNSET
    odos: VsrMetric | Unset = UNSET
    power_limitation_alert: VsrMetric | Unset = UNSET
    power_steering_warning: VsrMetric | Unset = UNSET
    spd: VsrMetric | Unset = UNSET
    tire_status: VehicleTireStatusEntity | Unset = UNSET
    v_2l_system_status_display: VsrMetric | Unset = UNSET
    washer_warn: VsrMetric | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        abs_warn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.abs_warn, Unset):
            abs_warn = self.abs_warn.to_dict()

        afu_failure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.afu_failure, Unset):
            afu_failure = self.afu_failure.to_dict()

        airbag_warn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.airbag_warn, Unset):
            airbag_warn = self.airbag_warn.to_dict()

        avail_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avail_range, Unset):
            avail_range = self.avail_range.to_dict()

        battery_high_warning: dict[str, Any] | Unset = UNSET
        if not isinstance(self.battery_high_warning, Unset):
            battery_high_warning = self.battery_high_warning.to_dict()

        battery_life: dict[str, Any] | Unset = UNSET
        if not isinstance(self.battery_life, Unset):
            battery_life = self.battery_life.to_dict()

        battery_low_warning: dict[str, Any] | Unset = UNSET
        if not isinstance(self.battery_low_warning, Unset):
            battery_low_warning = self.battery_low_warning.to_dict()

        break_warn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.break_warn, Unset):
            break_warn = self.break_warn.to_dict()

        cruising_range_first: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cruising_range_first, Unset):
            cruising_range_first = self.cruising_range_first.to_dict()

        cruising_range_second: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cruising_range_second, Unset):
            cruising_range_second = self.cruising_range_second.to_dict()

        digsts: None | str | Unset
        if isinstance(self.digsts, Unset):
            digsts = UNSET
        else:
            digsts = self.digsts

        dtc_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dtc_status, Unset):
            dtc_status = self.dtc_status.to_dict()

        emergency_braking_warning: dict[str, Any] | Unset = UNSET
        if not isinstance(self.emergency_braking_warning, Unset):
            emergency_braking_warning = self.emergency_braking_warning.to_dict()

        engine_oil_warn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.engine_oil_warn, Unset):
            engine_oil_warn = self.engine_oil_warn.to_dict()

        ev_alert_crbs_failure_display: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ev_alert_crbs_failure_display, Unset):
            ev_alert_crbs_failure_display = self.ev_alert_crbs_failure_display.to_dict()

        ev_battery_level_warning: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ev_battery_level_warning, Unset):
            ev_battery_level_warning = self.ev_battery_level_warning.to_dict()

        event_timestamp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event_timestamp, Unset):
            event_timestamp = self.event_timestamp.to_dict()

        fuel_level: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fuel_level, Unset):
            fuel_level = self.fuel_level.to_dict()

        igst: dict[str, Any] | Unset = UNSET
        if not isinstance(self.igst, Unset):
            igst = self.igst.to_dict()

        mil_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mil_status, Unset):
            mil_status = self.mil_status.to_dict()

        odo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.odo, Unset):
            odo = self.odo.to_dict()

        odos: dict[str, Any] | Unset = UNSET
        if not isinstance(self.odos, Unset):
            odos = self.odos.to_dict()

        power_limitation_alert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.power_limitation_alert, Unset):
            power_limitation_alert = self.power_limitation_alert.to_dict()

        power_steering_warning: dict[str, Any] | Unset = UNSET
        if not isinstance(self.power_steering_warning, Unset):
            power_steering_warning = self.power_steering_warning.to_dict()

        spd: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spd, Unset):
            spd = self.spd.to_dict()

        tire_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tire_status, Unset):
            tire_status = self.tire_status.to_dict()

        v_2l_system_status_display: dict[str, Any] | Unset = UNSET
        if not isinstance(self.v_2l_system_status_display, Unset):
            v_2l_system_status_display = self.v_2l_system_status_display.to_dict()

        washer_warn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.washer_warn, Unset):
            washer_warn = self.washer_warn.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if abs_warn is not UNSET:
            field_dict["absWarn"] = abs_warn
        if afu_failure is not UNSET:
            field_dict["afuFailure"] = afu_failure
        if airbag_warn is not UNSET:
            field_dict["airbagWarn"] = airbag_warn
        if avail_range is not UNSET:
            field_dict["availRange"] = avail_range
        if battery_high_warning is not UNSET:
            field_dict["batteryHighWarning"] = battery_high_warning
        if battery_life is not UNSET:
            field_dict["batteryLife"] = battery_life
        if battery_low_warning is not UNSET:
            field_dict["batteryLowWarning"] = battery_low_warning
        if break_warn is not UNSET:
            field_dict["breakWarn"] = break_warn
        if cruising_range_first is not UNSET:
            field_dict["cruisingRangeFirst"] = cruising_range_first
        if cruising_range_second is not UNSET:
            field_dict["cruisingRangeSecond"] = cruising_range_second
        if digsts is not UNSET:
            field_dict["digsts"] = digsts
        if dtc_status is not UNSET:
            field_dict["dtcStatus"] = dtc_status
        if emergency_braking_warning is not UNSET:
            field_dict["emergencyBrakingWarning"] = emergency_braking_warning
        if engine_oil_warn is not UNSET:
            field_dict["engineOilWarn"] = engine_oil_warn
        if ev_alert_crbs_failure_display is not UNSET:
            field_dict["evAlertCrbsFailureDisplay"] = ev_alert_crbs_failure_display
        if ev_battery_level_warning is not UNSET:
            field_dict["evBatteryLevelWarning"] = ev_battery_level_warning
        if event_timestamp is not UNSET:
            field_dict["eventTimestamp"] = event_timestamp
        if fuel_level is not UNSET:
            field_dict["fuelLevel"] = fuel_level
        if igst is not UNSET:
            field_dict["igst"] = igst
        if mil_status is not UNSET:
            field_dict["milStatus"] = mil_status
        if odo is not UNSET:
            field_dict["odo"] = odo
        if odos is not UNSET:
            field_dict["odos"] = odos
        if power_limitation_alert is not UNSET:
            field_dict["powerLimitationAlert"] = power_limitation_alert
        if power_steering_warning is not UNSET:
            field_dict["powerSteeringWarning"] = power_steering_warning
        if spd is not UNSET:
            field_dict["spd"] = spd
        if tire_status is not UNSET:
            field_dict["tireStatus"] = tire_status
        if v_2l_system_status_display is not UNSET:
            field_dict["v2LSystemStatusDisplay"] = v_2l_system_status_display
        if washer_warn is not UNSET:
            field_dict["washerWarn"] = washer_warn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vehicle_cruising_range_entity import VehicleCruisingRangeEntity  # noqa: PLC0415
        from ..models.vehicle_tire_status_entity import VehicleTireStatusEntity  # noqa: PLC0415
        from ..models.vsr_metric import VsrMetric  # noqa: PLC0415

        d = dict(src_dict)
        _abs_warn = d.pop("absWarn", UNSET)
        abs_warn: VsrMetric | Unset
        if isinstance(_abs_warn, Unset):
            abs_warn = UNSET
        else:
            abs_warn = VsrMetric.from_dict(_abs_warn)

        _afu_failure = d.pop("afuFailure", UNSET)
        afu_failure: VsrMetric | Unset
        if isinstance(_afu_failure, Unset):
            afu_failure = UNSET
        else:
            afu_failure = VsrMetric.from_dict(_afu_failure)

        _airbag_warn = d.pop("airbagWarn", UNSET)
        airbag_warn: VsrMetric | Unset
        if isinstance(_airbag_warn, Unset):
            airbag_warn = UNSET
        else:
            airbag_warn = VsrMetric.from_dict(_airbag_warn)

        _avail_range = d.pop("availRange", UNSET)
        avail_range: VsrMetric | Unset
        if isinstance(_avail_range, Unset):
            avail_range = UNSET
        else:
            avail_range = VsrMetric.from_dict(_avail_range)

        _battery_high_warning = d.pop("batteryHighWarning", UNSET)
        battery_high_warning: VsrMetric | Unset
        if isinstance(_battery_high_warning, Unset):
            battery_high_warning = UNSET
        else:
            battery_high_warning = VsrMetric.from_dict(_battery_high_warning)

        _battery_life = d.pop("batteryLife", UNSET)
        battery_life: VsrMetric | Unset
        if isinstance(_battery_life, Unset):
            battery_life = UNSET
        else:
            battery_life = VsrMetric.from_dict(_battery_life)

        _battery_low_warning = d.pop("batteryLowWarning", UNSET)
        battery_low_warning: VsrMetric | Unset
        if isinstance(_battery_low_warning, Unset):
            battery_low_warning = UNSET
        else:
            battery_low_warning = VsrMetric.from_dict(_battery_low_warning)

        _break_warn = d.pop("breakWarn", UNSET)
        break_warn: VsrMetric | Unset
        if isinstance(_break_warn, Unset):
            break_warn = UNSET
        else:
            break_warn = VsrMetric.from_dict(_break_warn)

        _cruising_range_first = d.pop("cruisingRangeFirst", UNSET)
        cruising_range_first: VehicleCruisingRangeEntity | Unset
        if isinstance(_cruising_range_first, Unset):
            cruising_range_first = UNSET
        else:
            cruising_range_first = VehicleCruisingRangeEntity.from_dict(_cruising_range_first)

        _cruising_range_second = d.pop("cruisingRangeSecond", UNSET)
        cruising_range_second: VehicleCruisingRangeEntity | Unset
        if isinstance(_cruising_range_second, Unset):
            cruising_range_second = UNSET
        else:
            cruising_range_second = VehicleCruisingRangeEntity.from_dict(_cruising_range_second)

        def _parse_digsts(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        digsts = _parse_digsts(d.pop("digsts", UNSET))

        _dtc_status = d.pop("dtcStatus", UNSET)
        dtc_status: VsrMetric | Unset
        if isinstance(_dtc_status, Unset):
            dtc_status = UNSET
        else:
            dtc_status = VsrMetric.from_dict(_dtc_status)

        _emergency_braking_warning = d.pop("emergencyBrakingWarning", UNSET)
        emergency_braking_warning: VsrMetric | Unset
        if isinstance(_emergency_braking_warning, Unset):
            emergency_braking_warning = UNSET
        else:
            emergency_braking_warning = VsrMetric.from_dict(_emergency_braking_warning)

        _engine_oil_warn = d.pop("engineOilWarn", UNSET)
        engine_oil_warn: VsrMetric | Unset
        if isinstance(_engine_oil_warn, Unset):
            engine_oil_warn = UNSET
        else:
            engine_oil_warn = VsrMetric.from_dict(_engine_oil_warn)

        _ev_alert_crbs_failure_display = d.pop("evAlertCrbsFailureDisplay", UNSET)
        ev_alert_crbs_failure_display: VsrMetric | Unset
        if isinstance(_ev_alert_crbs_failure_display, Unset):
            ev_alert_crbs_failure_display = UNSET
        else:
            ev_alert_crbs_failure_display = VsrMetric.from_dict(_ev_alert_crbs_failure_display)

        _ev_battery_level_warning = d.pop("evBatteryLevelWarning", UNSET)
        ev_battery_level_warning: VsrMetric | Unset
        if isinstance(_ev_battery_level_warning, Unset):
            ev_battery_level_warning = UNSET
        else:
            ev_battery_level_warning = VsrMetric.from_dict(_ev_battery_level_warning)

        _event_timestamp = d.pop("eventTimestamp", UNSET)
        event_timestamp: VsrMetric | Unset
        if isinstance(_event_timestamp, Unset):
            event_timestamp = UNSET
        else:
            event_timestamp = VsrMetric.from_dict(_event_timestamp)

        _fuel_level = d.pop("fuelLevel", UNSET)
        fuel_level: VsrMetric | Unset
        if isinstance(_fuel_level, Unset):
            fuel_level = UNSET
        else:
            fuel_level = VsrMetric.from_dict(_fuel_level)

        _igst = d.pop("igst", UNSET)
        igst: VsrMetric | Unset
        if isinstance(_igst, Unset):
            igst = UNSET
        else:
            igst = VsrMetric.from_dict(_igst)

        _mil_status = d.pop("milStatus", UNSET)
        mil_status: VsrMetric | Unset
        if isinstance(_mil_status, Unset):
            mil_status = UNSET
        else:
            mil_status = VsrMetric.from_dict(_mil_status)

        _odo = d.pop("odo", UNSET)
        odo: VsrMetric | Unset
        if isinstance(_odo, Unset):
            odo = UNSET
        else:
            odo = VsrMetric.from_dict(_odo)

        _odos = d.pop("odos", UNSET)
        odos: VsrMetric | Unset
        if isinstance(_odos, Unset):
            odos = UNSET
        else:
            odos = VsrMetric.from_dict(_odos)

        _power_limitation_alert = d.pop("powerLimitationAlert", UNSET)
        power_limitation_alert: VsrMetric | Unset
        if isinstance(_power_limitation_alert, Unset):
            power_limitation_alert = UNSET
        else:
            power_limitation_alert = VsrMetric.from_dict(_power_limitation_alert)

        _power_steering_warning = d.pop("powerSteeringWarning", UNSET)
        power_steering_warning: VsrMetric | Unset
        if isinstance(_power_steering_warning, Unset):
            power_steering_warning = UNSET
        else:
            power_steering_warning = VsrMetric.from_dict(_power_steering_warning)

        _spd = d.pop("spd", UNSET)
        spd: VsrMetric | Unset
        if isinstance(_spd, Unset):
            spd = UNSET
        else:
            spd = VsrMetric.from_dict(_spd)

        _tire_status = d.pop("tireStatus", UNSET)
        tire_status: VehicleTireStatusEntity | Unset
        if isinstance(_tire_status, Unset):
            tire_status = UNSET
        else:
            tire_status = VehicleTireStatusEntity.from_dict(_tire_status)

        _v_2l_system_status_display = d.pop("v2LSystemStatusDisplay", UNSET)
        v_2l_system_status_display: VsrMetric | Unset
        if isinstance(_v_2l_system_status_display, Unset):
            v_2l_system_status_display = UNSET
        else:
            v_2l_system_status_display = VsrMetric.from_dict(_v_2l_system_status_display)

        _washer_warn = d.pop("washerWarn", UNSET)
        washer_warn: VsrMetric | Unset
        if isinstance(_washer_warn, Unset):
            washer_warn = UNSET
        else:
            washer_warn = VsrMetric.from_dict(_washer_warn)

        vsr_diagnostic = cls(
            abs_warn=abs_warn,
            afu_failure=afu_failure,
            airbag_warn=airbag_warn,
            avail_range=avail_range,
            battery_high_warning=battery_high_warning,
            battery_life=battery_life,
            battery_low_warning=battery_low_warning,
            break_warn=break_warn,
            cruising_range_first=cruising_range_first,
            cruising_range_second=cruising_range_second,
            digsts=digsts,
            dtc_status=dtc_status,
            emergency_braking_warning=emergency_braking_warning,
            engine_oil_warn=engine_oil_warn,
            ev_alert_crbs_failure_display=ev_alert_crbs_failure_display,
            ev_battery_level_warning=ev_battery_level_warning,
            event_timestamp=event_timestamp,
            fuel_level=fuel_level,
            igst=igst,
            mil_status=mil_status,
            odo=odo,
            odos=odos,
            power_limitation_alert=power_limitation_alert,
            power_steering_warning=power_steering_warning,
            spd=spd,
            tire_status=tire_status,
            v_2l_system_status_display=v_2l_system_status_display,
            washer_warn=washer_warn,
        )

        vsr_diagnostic.additional_properties = d
        return vsr_diagnostic

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
