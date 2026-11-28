from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.soc_entity import SOCEntity


T = TypeVar("T", bound="MetaDataEntity")


@_attrs_define
class MetaDataEntity:
    """
    Attributes:
        fetch_legal_config_flag (None | str | Unset):
        guest_mode_data (None | str | Unset):
        hide_parental_control_name_flag (None | str | Unset):
        scan_car_attributes (None | str | Unset):
        scan_car_base_url (None | str | Unset):
        soc (SOCEntity | Unset):
        support_charge_schedule_limit (None | str | Unset):
        support_charge_schedule_unique_id_flag (None | str | Unset):
        support_climate_schedule_limit (None | str | Unset):
        support_climate_schedule_unique_id_flag (None | str | Unset):
        support_curfew_alert_maximum (None | str | Unset):
        support_geofence_alert_maximum (None | str | Unset):
        support_guest_mode_flag (None | str | Unset):
        support_polling_flag (None | str | Unset): When `true`, the server returns a `requestId` to poll with
            `getBatchRequestStatus`. Default: '0'.
        support_privacy_mode_flag (None | str | Unset):  Default: '0'.
        support_smart_route_weather_flag (None | str | Unset):
    """

    fetch_legal_config_flag: None | str | Unset = UNSET
    guest_mode_data: None | str | Unset = UNSET
    hide_parental_control_name_flag: None | str | Unset = UNSET
    scan_car_attributes: None | str | Unset = UNSET
    scan_car_base_url: None | str | Unset = UNSET
    soc: SOCEntity | Unset = UNSET
    support_charge_schedule_limit: None | str | Unset = UNSET
    support_charge_schedule_unique_id_flag: None | str | Unset = UNSET
    support_climate_schedule_limit: None | str | Unset = UNSET
    support_climate_schedule_unique_id_flag: None | str | Unset = UNSET
    support_curfew_alert_maximum: None | str | Unset = UNSET
    support_geofence_alert_maximum: None | str | Unset = UNSET
    support_guest_mode_flag: None | str | Unset = UNSET
    support_polling_flag: None | str | Unset = "0"
    support_privacy_mode_flag: None | str | Unset = "0"
    support_smart_route_weather_flag: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fetch_legal_config_flag: None | str | Unset
        if isinstance(self.fetch_legal_config_flag, Unset):
            fetch_legal_config_flag = UNSET
        else:
            fetch_legal_config_flag = self.fetch_legal_config_flag

        guest_mode_data: None | str | Unset
        if isinstance(self.guest_mode_data, Unset):
            guest_mode_data = UNSET
        else:
            guest_mode_data = self.guest_mode_data

        hide_parental_control_name_flag: None | str | Unset
        if isinstance(self.hide_parental_control_name_flag, Unset):
            hide_parental_control_name_flag = UNSET
        else:
            hide_parental_control_name_flag = self.hide_parental_control_name_flag

        scan_car_attributes: None | str | Unset
        if isinstance(self.scan_car_attributes, Unset):
            scan_car_attributes = UNSET
        else:
            scan_car_attributes = self.scan_car_attributes

        scan_car_base_url: None | str | Unset
        if isinstance(self.scan_car_base_url, Unset):
            scan_car_base_url = UNSET
        else:
            scan_car_base_url = self.scan_car_base_url

        soc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.soc, Unset):
            soc = self.soc.to_dict()

        support_charge_schedule_limit: None | str | Unset
        if isinstance(self.support_charge_schedule_limit, Unset):
            support_charge_schedule_limit = UNSET
        else:
            support_charge_schedule_limit = self.support_charge_schedule_limit

        support_charge_schedule_unique_id_flag: None | str | Unset
        if isinstance(self.support_charge_schedule_unique_id_flag, Unset):
            support_charge_schedule_unique_id_flag = UNSET
        else:
            support_charge_schedule_unique_id_flag = self.support_charge_schedule_unique_id_flag

        support_climate_schedule_limit: None | str | Unset
        if isinstance(self.support_climate_schedule_limit, Unset):
            support_climate_schedule_limit = UNSET
        else:
            support_climate_schedule_limit = self.support_climate_schedule_limit

        support_climate_schedule_unique_id_flag: None | str | Unset
        if isinstance(self.support_climate_schedule_unique_id_flag, Unset):
            support_climate_schedule_unique_id_flag = UNSET
        else:
            support_climate_schedule_unique_id_flag = self.support_climate_schedule_unique_id_flag

        support_curfew_alert_maximum: None | str | Unset
        if isinstance(self.support_curfew_alert_maximum, Unset):
            support_curfew_alert_maximum = UNSET
        else:
            support_curfew_alert_maximum = self.support_curfew_alert_maximum

        support_geofence_alert_maximum: None | str | Unset
        if isinstance(self.support_geofence_alert_maximum, Unset):
            support_geofence_alert_maximum = UNSET
        else:
            support_geofence_alert_maximum = self.support_geofence_alert_maximum

        support_guest_mode_flag: None | str | Unset
        if isinstance(self.support_guest_mode_flag, Unset):
            support_guest_mode_flag = UNSET
        else:
            support_guest_mode_flag = self.support_guest_mode_flag

        support_polling_flag: None | str | Unset
        if isinstance(self.support_polling_flag, Unset):
            support_polling_flag = UNSET
        else:
            support_polling_flag = self.support_polling_flag

        support_privacy_mode_flag: None | str | Unset
        if isinstance(self.support_privacy_mode_flag, Unset):
            support_privacy_mode_flag = UNSET
        else:
            support_privacy_mode_flag = self.support_privacy_mode_flag

        support_smart_route_weather_flag: None | str | Unset
        if isinstance(self.support_smart_route_weather_flag, Unset):
            support_smart_route_weather_flag = UNSET
        else:
            support_smart_route_weather_flag = self.support_smart_route_weather_flag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fetch_legal_config_flag is not UNSET:
            field_dict["fetchLegalConfigFlag"] = fetch_legal_config_flag
        if guest_mode_data is not UNSET:
            field_dict["guestModeData"] = guest_mode_data
        if hide_parental_control_name_flag is not UNSET:
            field_dict["hideParentalControlNameFlag"] = hide_parental_control_name_flag
        if scan_car_attributes is not UNSET:
            field_dict["scanCarAttributes"] = scan_car_attributes
        if scan_car_base_url is not UNSET:
            field_dict["scanCarBaseUrl"] = scan_car_base_url
        if soc is not UNSET:
            field_dict["soc"] = soc
        if support_charge_schedule_limit is not UNSET:
            field_dict["supportChargeScheduleLimit"] = support_charge_schedule_limit
        if support_charge_schedule_unique_id_flag is not UNSET:
            field_dict["supportChargeScheduleUniqueIdFlag"] = support_charge_schedule_unique_id_flag
        if support_climate_schedule_limit is not UNSET:
            field_dict["supportClimateScheduleLimit"] = support_climate_schedule_limit
        if support_climate_schedule_unique_id_flag is not UNSET:
            field_dict["supportClimateScheduleUniqueIdFlag"] = support_climate_schedule_unique_id_flag
        if support_curfew_alert_maximum is not UNSET:
            field_dict["supportCurfewAlertMaximum"] = support_curfew_alert_maximum
        if support_geofence_alert_maximum is not UNSET:
            field_dict["supportGeofenceAlertMaximum"] = support_geofence_alert_maximum
        if support_guest_mode_flag is not UNSET:
            field_dict["supportGuestModeFlag"] = support_guest_mode_flag
        if support_polling_flag is not UNSET:
            field_dict["supportPollingFlag"] = support_polling_flag
        if support_privacy_mode_flag is not UNSET:
            field_dict["supportPrivacyModeFlag"] = support_privacy_mode_flag
        if support_smart_route_weather_flag is not UNSET:
            field_dict["supportSmartRouteWeatherFlag"] = support_smart_route_weather_flag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.soc_entity import SOCEntity  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_fetch_legal_config_flag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fetch_legal_config_flag = _parse_fetch_legal_config_flag(d.pop("fetchLegalConfigFlag", UNSET))

        def _parse_guest_mode_data(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_mode_data = _parse_guest_mode_data(d.pop("guestModeData", UNSET))

        def _parse_hide_parental_control_name_flag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hide_parental_control_name_flag = _parse_hide_parental_control_name_flag(
            d.pop("hideParentalControlNameFlag", UNSET)
        )

        def _parse_scan_car_attributes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scan_car_attributes = _parse_scan_car_attributes(d.pop("scanCarAttributes", UNSET))

        def _parse_scan_car_base_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scan_car_base_url = _parse_scan_car_base_url(d.pop("scanCarBaseUrl", UNSET))

        _soc = d.pop("soc", UNSET)
        soc: SOCEntity | Unset
        if isinstance(_soc, Unset):
            soc = UNSET
        else:
            soc = SOCEntity.from_dict(_soc)

        def _parse_support_charge_schedule_limit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_charge_schedule_limit = _parse_support_charge_schedule_limit(d.pop("supportChargeScheduleLimit", UNSET))

        def _parse_support_charge_schedule_unique_id_flag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_charge_schedule_unique_id_flag = _parse_support_charge_schedule_unique_id_flag(
            d.pop("supportChargeScheduleUniqueIdFlag", UNSET)
        )

        def _parse_support_climate_schedule_limit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_climate_schedule_limit = _parse_support_climate_schedule_limit(
            d.pop("supportClimateScheduleLimit", UNSET)
        )

        def _parse_support_climate_schedule_unique_id_flag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_climate_schedule_unique_id_flag = _parse_support_climate_schedule_unique_id_flag(
            d.pop("supportClimateScheduleUniqueIdFlag", UNSET)
        )

        def _parse_support_curfew_alert_maximum(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_curfew_alert_maximum = _parse_support_curfew_alert_maximum(d.pop("supportCurfewAlertMaximum", UNSET))

        def _parse_support_geofence_alert_maximum(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_geofence_alert_maximum = _parse_support_geofence_alert_maximum(
            d.pop("supportGeofenceAlertMaximum", UNSET)
        )

        def _parse_support_guest_mode_flag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_guest_mode_flag = _parse_support_guest_mode_flag(d.pop("supportGuestModeFlag", UNSET))

        def _parse_support_polling_flag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_polling_flag = _parse_support_polling_flag(d.pop("supportPollingFlag", UNSET))

        def _parse_support_privacy_mode_flag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_privacy_mode_flag = _parse_support_privacy_mode_flag(d.pop("supportPrivacyModeFlag", UNSET))

        def _parse_support_smart_route_weather_flag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_smart_route_weather_flag = _parse_support_smart_route_weather_flag(
            d.pop("supportSmartRouteWeatherFlag", UNSET)
        )

        meta_data_entity = cls(
            fetch_legal_config_flag=fetch_legal_config_flag,
            guest_mode_data=guest_mode_data,
            hide_parental_control_name_flag=hide_parental_control_name_flag,
            scan_car_attributes=scan_car_attributes,
            scan_car_base_url=scan_car_base_url,
            soc=soc,
            support_charge_schedule_limit=support_charge_schedule_limit,
            support_charge_schedule_unique_id_flag=support_charge_schedule_unique_id_flag,
            support_climate_schedule_limit=support_climate_schedule_limit,
            support_climate_schedule_unique_id_flag=support_climate_schedule_unique_id_flag,
            support_curfew_alert_maximum=support_curfew_alert_maximum,
            support_geofence_alert_maximum=support_geofence_alert_maximum,
            support_guest_mode_flag=support_guest_mode_flag,
            support_polling_flag=support_polling_flag,
            support_privacy_mode_flag=support_privacy_mode_flag,
            support_smart_route_weather_flag=support_smart_route_weather_flag,
        )

        meta_data_entity.additional_properties = d
        return meta_data_entity

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
