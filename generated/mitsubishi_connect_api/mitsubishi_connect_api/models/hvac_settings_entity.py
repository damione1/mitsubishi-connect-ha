from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HVACSettingsEntity")


@_attrs_define
class HVACSettingsEntity:
    """
    Attributes:
        is_delay_cancel_ui_visible (bool | None | Unset):
        is_fan_ui_visible (bool | None | Unset):
        is_front_defrost_ui_visible (bool | None | Unset):
        is_front_left_seat_cooler_ui_visible (bool | None | Unset):
        is_front_left_seat_heater_ui_visible (bool | None | Unset):
        is_front_right_seat_cooler_ui_visible (bool | None | Unset):
        is_front_right_seat_heater_ui_visible (bool | None | Unset):
        is_max_defrost_ui_visible (bool | None | Unset):
        is_rear_center_seat_cooler_ui_visible (bool | None | Unset):
        is_rear_center_seat_heater_ui_visible (bool | None | Unset):
        is_rear_defrost_ui_visible (bool | None | Unset):
        is_rear_left_seat_cooler_ui_visible (bool | None | Unset):
        is_rear_left_seat_heater_ui_visible (bool | None | Unset):
        is_rear_right_seat_cooler_ui_visible (bool | None | Unset):
        is_rear_right_seat_heater_ui_visible (bool | None | Unset):
        is_steering_heater_ui_visible (bool | None | Unset):
        is_temperature_setting_ui_visible (bool | None | Unset):
    """

    is_delay_cancel_ui_visible: bool | None | Unset = UNSET
    is_fan_ui_visible: bool | None | Unset = UNSET
    is_front_defrost_ui_visible: bool | None | Unset = UNSET
    is_front_left_seat_cooler_ui_visible: bool | None | Unset = UNSET
    is_front_left_seat_heater_ui_visible: bool | None | Unset = UNSET
    is_front_right_seat_cooler_ui_visible: bool | None | Unset = UNSET
    is_front_right_seat_heater_ui_visible: bool | None | Unset = UNSET
    is_max_defrost_ui_visible: bool | None | Unset = UNSET
    is_rear_center_seat_cooler_ui_visible: bool | None | Unset = UNSET
    is_rear_center_seat_heater_ui_visible: bool | None | Unset = UNSET
    is_rear_defrost_ui_visible: bool | None | Unset = UNSET
    is_rear_left_seat_cooler_ui_visible: bool | None | Unset = UNSET
    is_rear_left_seat_heater_ui_visible: bool | None | Unset = UNSET
    is_rear_right_seat_cooler_ui_visible: bool | None | Unset = UNSET
    is_rear_right_seat_heater_ui_visible: bool | None | Unset = UNSET
    is_steering_heater_ui_visible: bool | None | Unset = UNSET
    is_temperature_setting_ui_visible: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_delay_cancel_ui_visible: bool | None | Unset
        if isinstance(self.is_delay_cancel_ui_visible, Unset):
            is_delay_cancel_ui_visible = UNSET
        else:
            is_delay_cancel_ui_visible = self.is_delay_cancel_ui_visible

        is_fan_ui_visible: bool | None | Unset
        if isinstance(self.is_fan_ui_visible, Unset):
            is_fan_ui_visible = UNSET
        else:
            is_fan_ui_visible = self.is_fan_ui_visible

        is_front_defrost_ui_visible: bool | None | Unset
        if isinstance(self.is_front_defrost_ui_visible, Unset):
            is_front_defrost_ui_visible = UNSET
        else:
            is_front_defrost_ui_visible = self.is_front_defrost_ui_visible

        is_front_left_seat_cooler_ui_visible: bool | None | Unset
        if isinstance(self.is_front_left_seat_cooler_ui_visible, Unset):
            is_front_left_seat_cooler_ui_visible = UNSET
        else:
            is_front_left_seat_cooler_ui_visible = self.is_front_left_seat_cooler_ui_visible

        is_front_left_seat_heater_ui_visible: bool | None | Unset
        if isinstance(self.is_front_left_seat_heater_ui_visible, Unset):
            is_front_left_seat_heater_ui_visible = UNSET
        else:
            is_front_left_seat_heater_ui_visible = self.is_front_left_seat_heater_ui_visible

        is_front_right_seat_cooler_ui_visible: bool | None | Unset
        if isinstance(self.is_front_right_seat_cooler_ui_visible, Unset):
            is_front_right_seat_cooler_ui_visible = UNSET
        else:
            is_front_right_seat_cooler_ui_visible = self.is_front_right_seat_cooler_ui_visible

        is_front_right_seat_heater_ui_visible: bool | None | Unset
        if isinstance(self.is_front_right_seat_heater_ui_visible, Unset):
            is_front_right_seat_heater_ui_visible = UNSET
        else:
            is_front_right_seat_heater_ui_visible = self.is_front_right_seat_heater_ui_visible

        is_max_defrost_ui_visible: bool | None | Unset
        if isinstance(self.is_max_defrost_ui_visible, Unset):
            is_max_defrost_ui_visible = UNSET
        else:
            is_max_defrost_ui_visible = self.is_max_defrost_ui_visible

        is_rear_center_seat_cooler_ui_visible: bool | None | Unset
        if isinstance(self.is_rear_center_seat_cooler_ui_visible, Unset):
            is_rear_center_seat_cooler_ui_visible = UNSET
        else:
            is_rear_center_seat_cooler_ui_visible = self.is_rear_center_seat_cooler_ui_visible

        is_rear_center_seat_heater_ui_visible: bool | None | Unset
        if isinstance(self.is_rear_center_seat_heater_ui_visible, Unset):
            is_rear_center_seat_heater_ui_visible = UNSET
        else:
            is_rear_center_seat_heater_ui_visible = self.is_rear_center_seat_heater_ui_visible

        is_rear_defrost_ui_visible: bool | None | Unset
        if isinstance(self.is_rear_defrost_ui_visible, Unset):
            is_rear_defrost_ui_visible = UNSET
        else:
            is_rear_defrost_ui_visible = self.is_rear_defrost_ui_visible

        is_rear_left_seat_cooler_ui_visible: bool | None | Unset
        if isinstance(self.is_rear_left_seat_cooler_ui_visible, Unset):
            is_rear_left_seat_cooler_ui_visible = UNSET
        else:
            is_rear_left_seat_cooler_ui_visible = self.is_rear_left_seat_cooler_ui_visible

        is_rear_left_seat_heater_ui_visible: bool | None | Unset
        if isinstance(self.is_rear_left_seat_heater_ui_visible, Unset):
            is_rear_left_seat_heater_ui_visible = UNSET
        else:
            is_rear_left_seat_heater_ui_visible = self.is_rear_left_seat_heater_ui_visible

        is_rear_right_seat_cooler_ui_visible: bool | None | Unset
        if isinstance(self.is_rear_right_seat_cooler_ui_visible, Unset):
            is_rear_right_seat_cooler_ui_visible = UNSET
        else:
            is_rear_right_seat_cooler_ui_visible = self.is_rear_right_seat_cooler_ui_visible

        is_rear_right_seat_heater_ui_visible: bool | None | Unset
        if isinstance(self.is_rear_right_seat_heater_ui_visible, Unset):
            is_rear_right_seat_heater_ui_visible = UNSET
        else:
            is_rear_right_seat_heater_ui_visible = self.is_rear_right_seat_heater_ui_visible

        is_steering_heater_ui_visible: bool | None | Unset
        if isinstance(self.is_steering_heater_ui_visible, Unset):
            is_steering_heater_ui_visible = UNSET
        else:
            is_steering_heater_ui_visible = self.is_steering_heater_ui_visible

        is_temperature_setting_ui_visible: bool | None | Unset
        if isinstance(self.is_temperature_setting_ui_visible, Unset):
            is_temperature_setting_ui_visible = UNSET
        else:
            is_temperature_setting_ui_visible = self.is_temperature_setting_ui_visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_delay_cancel_ui_visible is not UNSET:
            field_dict["isDelayCancelUIVisible"] = is_delay_cancel_ui_visible
        if is_fan_ui_visible is not UNSET:
            field_dict["isFanUIVisible"] = is_fan_ui_visible
        if is_front_defrost_ui_visible is not UNSET:
            field_dict["isFrontDefrostUIVisible"] = is_front_defrost_ui_visible
        if is_front_left_seat_cooler_ui_visible is not UNSET:
            field_dict["isFrontLeftSeatCoolerUIVisible"] = is_front_left_seat_cooler_ui_visible
        if is_front_left_seat_heater_ui_visible is not UNSET:
            field_dict["isFrontLeftSeatHeaterUIVisible"] = is_front_left_seat_heater_ui_visible
        if is_front_right_seat_cooler_ui_visible is not UNSET:
            field_dict["isFrontRightSeatCoolerUIVisible"] = is_front_right_seat_cooler_ui_visible
        if is_front_right_seat_heater_ui_visible is not UNSET:
            field_dict["isFrontRightSeatHeaterUIVisible"] = is_front_right_seat_heater_ui_visible
        if is_max_defrost_ui_visible is not UNSET:
            field_dict["isMaxDefrostUIVisible"] = is_max_defrost_ui_visible
        if is_rear_center_seat_cooler_ui_visible is not UNSET:
            field_dict["isRearCenterSeatCoolerUIVisible"] = is_rear_center_seat_cooler_ui_visible
        if is_rear_center_seat_heater_ui_visible is not UNSET:
            field_dict["isRearCenterSeatHeaterUIVisible"] = is_rear_center_seat_heater_ui_visible
        if is_rear_defrost_ui_visible is not UNSET:
            field_dict["isRearDefrostUIVisible"] = is_rear_defrost_ui_visible
        if is_rear_left_seat_cooler_ui_visible is not UNSET:
            field_dict["isRearLeftSeatCoolerUIVisible"] = is_rear_left_seat_cooler_ui_visible
        if is_rear_left_seat_heater_ui_visible is not UNSET:
            field_dict["isRearLeftSeatHeaterUIVisible"] = is_rear_left_seat_heater_ui_visible
        if is_rear_right_seat_cooler_ui_visible is not UNSET:
            field_dict["isRearRightSeatCoolerUIVisible"] = is_rear_right_seat_cooler_ui_visible
        if is_rear_right_seat_heater_ui_visible is not UNSET:
            field_dict["isRearRightSeatHeaterUIVisible"] = is_rear_right_seat_heater_ui_visible
        if is_steering_heater_ui_visible is not UNSET:
            field_dict["isSteeringHeaterUIVisible"] = is_steering_heater_ui_visible
        if is_temperature_setting_ui_visible is not UNSET:
            field_dict["isTemperatureSettingUIVisible"] = is_temperature_setting_ui_visible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_is_delay_cancel_ui_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_delay_cancel_ui_visible = _parse_is_delay_cancel_ui_visible(d.pop("isDelayCancelUIVisible", UNSET))

        def _parse_is_fan_ui_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_fan_ui_visible = _parse_is_fan_ui_visible(d.pop("isFanUIVisible", UNSET))

        def _parse_is_front_defrost_ui_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_front_defrost_ui_visible = _parse_is_front_defrost_ui_visible(d.pop("isFrontDefrostUIVisible", UNSET))

        def _parse_is_front_left_seat_cooler_ui_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_front_left_seat_cooler_ui_visible = _parse_is_front_left_seat_cooler_ui_visible(
            d.pop("isFrontLeftSeatCoolerUIVisible", UNSET)
        )

        def _parse_is_front_left_seat_heater_ui_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_front_left_seat_heater_ui_visible = _parse_is_front_left_seat_heater_ui_visible(
            d.pop("isFrontLeftSeatHeaterUIVisible", UNSET)
        )

        def _parse_is_front_right_seat_cooler_ui_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_front_right_seat_cooler_ui_visible = _parse_is_front_right_seat_cooler_ui_visible(
            d.pop("isFrontRightSeatCoolerUIVisible", UNSET)
        )

        def _parse_is_front_right_seat_heater_ui_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_front_right_seat_heater_ui_visible = _parse_is_front_right_seat_heater_ui_visible(
            d.pop("isFrontRightSeatHeaterUIVisible", UNSET)
        )

        def _parse_is_max_defrost_ui_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_max_defrost_ui_visible = _parse_is_max_defrost_ui_visible(d.pop("isMaxDefrostUIVisible", UNSET))

        def _parse_is_rear_center_seat_cooler_ui_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_rear_center_seat_cooler_ui_visible = _parse_is_rear_center_seat_cooler_ui_visible(
            d.pop("isRearCenterSeatCoolerUIVisible", UNSET)
        )

        def _parse_is_rear_center_seat_heater_ui_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_rear_center_seat_heater_ui_visible = _parse_is_rear_center_seat_heater_ui_visible(
            d.pop("isRearCenterSeatHeaterUIVisible", UNSET)
        )

        def _parse_is_rear_defrost_ui_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_rear_defrost_ui_visible = _parse_is_rear_defrost_ui_visible(d.pop("isRearDefrostUIVisible", UNSET))

        def _parse_is_rear_left_seat_cooler_ui_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_rear_left_seat_cooler_ui_visible = _parse_is_rear_left_seat_cooler_ui_visible(
            d.pop("isRearLeftSeatCoolerUIVisible", UNSET)
        )

        def _parse_is_rear_left_seat_heater_ui_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_rear_left_seat_heater_ui_visible = _parse_is_rear_left_seat_heater_ui_visible(
            d.pop("isRearLeftSeatHeaterUIVisible", UNSET)
        )

        def _parse_is_rear_right_seat_cooler_ui_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_rear_right_seat_cooler_ui_visible = _parse_is_rear_right_seat_cooler_ui_visible(
            d.pop("isRearRightSeatCoolerUIVisible", UNSET)
        )

        def _parse_is_rear_right_seat_heater_ui_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_rear_right_seat_heater_ui_visible = _parse_is_rear_right_seat_heater_ui_visible(
            d.pop("isRearRightSeatHeaterUIVisible", UNSET)
        )

        def _parse_is_steering_heater_ui_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_steering_heater_ui_visible = _parse_is_steering_heater_ui_visible(d.pop("isSteeringHeaterUIVisible", UNSET))

        def _parse_is_temperature_setting_ui_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_temperature_setting_ui_visible = _parse_is_temperature_setting_ui_visible(
            d.pop("isTemperatureSettingUIVisible", UNSET)
        )

        hvac_settings_entity = cls(
            is_delay_cancel_ui_visible=is_delay_cancel_ui_visible,
            is_fan_ui_visible=is_fan_ui_visible,
            is_front_defrost_ui_visible=is_front_defrost_ui_visible,
            is_front_left_seat_cooler_ui_visible=is_front_left_seat_cooler_ui_visible,
            is_front_left_seat_heater_ui_visible=is_front_left_seat_heater_ui_visible,
            is_front_right_seat_cooler_ui_visible=is_front_right_seat_cooler_ui_visible,
            is_front_right_seat_heater_ui_visible=is_front_right_seat_heater_ui_visible,
            is_max_defrost_ui_visible=is_max_defrost_ui_visible,
            is_rear_center_seat_cooler_ui_visible=is_rear_center_seat_cooler_ui_visible,
            is_rear_center_seat_heater_ui_visible=is_rear_center_seat_heater_ui_visible,
            is_rear_defrost_ui_visible=is_rear_defrost_ui_visible,
            is_rear_left_seat_cooler_ui_visible=is_rear_left_seat_cooler_ui_visible,
            is_rear_left_seat_heater_ui_visible=is_rear_left_seat_heater_ui_visible,
            is_rear_right_seat_cooler_ui_visible=is_rear_right_seat_cooler_ui_visible,
            is_rear_right_seat_heater_ui_visible=is_rear_right_seat_heater_ui_visible,
            is_steering_heater_ui_visible=is_steering_heater_ui_visible,
            is_temperature_setting_ui_visible=is_temperature_setting_ui_visible,
        )

        hvac_settings_entity.additional_properties = d
        return hvac_settings_entity

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
