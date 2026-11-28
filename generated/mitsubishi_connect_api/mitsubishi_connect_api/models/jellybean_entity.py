from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JellybeanEntity")


@_attrs_define
class JellybeanEntity:
    """
    Attributes:
        home_jellybean (None | str | Unset):
        vehicle_color (None | str | Unset):
        vehicle_model (None | str | Unset):
        vehicle_year (None | str | Unset):
        vsr_body_jellybean (None | str | Unset):
        vsr_door_left_front_close_jellybean (None | str | Unset):
        vsr_door_left_front_open_jellybean (None | str | Unset):
        vsr_door_left_rear_close_jellybean (None | str | Unset):
        vsr_door_left_rear_open_jellybean (None | str | Unset):
        vsr_door_right_front_close_jellybean (None | str | Unset):
        vsr_door_right_front_open_jellybean (None | str | Unset):
        vsr_door_right_rear_close_jellybean (None | str | Unset):
        vsr_door_right_rear_open_jellybean (None | str | Unset):
        vsr_hood_jellybean (None | str | Unset):
        vsr_tailgate_jellybean (None | str | Unset):
    """

    home_jellybean: None | str | Unset = UNSET
    vehicle_color: None | str | Unset = UNSET
    vehicle_model: None | str | Unset = UNSET
    vehicle_year: None | str | Unset = UNSET
    vsr_body_jellybean: None | str | Unset = UNSET
    vsr_door_left_front_close_jellybean: None | str | Unset = UNSET
    vsr_door_left_front_open_jellybean: None | str | Unset = UNSET
    vsr_door_left_rear_close_jellybean: None | str | Unset = UNSET
    vsr_door_left_rear_open_jellybean: None | str | Unset = UNSET
    vsr_door_right_front_close_jellybean: None | str | Unset = UNSET
    vsr_door_right_front_open_jellybean: None | str | Unset = UNSET
    vsr_door_right_rear_close_jellybean: None | str | Unset = UNSET
    vsr_door_right_rear_open_jellybean: None | str | Unset = UNSET
    vsr_hood_jellybean: None | str | Unset = UNSET
    vsr_tailgate_jellybean: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        home_jellybean: None | str | Unset
        if isinstance(self.home_jellybean, Unset):
            home_jellybean = UNSET
        else:
            home_jellybean = self.home_jellybean

        vehicle_color: None | str | Unset
        if isinstance(self.vehicle_color, Unset):
            vehicle_color = UNSET
        else:
            vehicle_color = self.vehicle_color

        vehicle_model: None | str | Unset
        if isinstance(self.vehicle_model, Unset):
            vehicle_model = UNSET
        else:
            vehicle_model = self.vehicle_model

        vehicle_year: None | str | Unset
        if isinstance(self.vehicle_year, Unset):
            vehicle_year = UNSET
        else:
            vehicle_year = self.vehicle_year

        vsr_body_jellybean: None | str | Unset
        if isinstance(self.vsr_body_jellybean, Unset):
            vsr_body_jellybean = UNSET
        else:
            vsr_body_jellybean = self.vsr_body_jellybean

        vsr_door_left_front_close_jellybean: None | str | Unset
        if isinstance(self.vsr_door_left_front_close_jellybean, Unset):
            vsr_door_left_front_close_jellybean = UNSET
        else:
            vsr_door_left_front_close_jellybean = self.vsr_door_left_front_close_jellybean

        vsr_door_left_front_open_jellybean: None | str | Unset
        if isinstance(self.vsr_door_left_front_open_jellybean, Unset):
            vsr_door_left_front_open_jellybean = UNSET
        else:
            vsr_door_left_front_open_jellybean = self.vsr_door_left_front_open_jellybean

        vsr_door_left_rear_close_jellybean: None | str | Unset
        if isinstance(self.vsr_door_left_rear_close_jellybean, Unset):
            vsr_door_left_rear_close_jellybean = UNSET
        else:
            vsr_door_left_rear_close_jellybean = self.vsr_door_left_rear_close_jellybean

        vsr_door_left_rear_open_jellybean: None | str | Unset
        if isinstance(self.vsr_door_left_rear_open_jellybean, Unset):
            vsr_door_left_rear_open_jellybean = UNSET
        else:
            vsr_door_left_rear_open_jellybean = self.vsr_door_left_rear_open_jellybean

        vsr_door_right_front_close_jellybean: None | str | Unset
        if isinstance(self.vsr_door_right_front_close_jellybean, Unset):
            vsr_door_right_front_close_jellybean = UNSET
        else:
            vsr_door_right_front_close_jellybean = self.vsr_door_right_front_close_jellybean

        vsr_door_right_front_open_jellybean: None | str | Unset
        if isinstance(self.vsr_door_right_front_open_jellybean, Unset):
            vsr_door_right_front_open_jellybean = UNSET
        else:
            vsr_door_right_front_open_jellybean = self.vsr_door_right_front_open_jellybean

        vsr_door_right_rear_close_jellybean: None | str | Unset
        if isinstance(self.vsr_door_right_rear_close_jellybean, Unset):
            vsr_door_right_rear_close_jellybean = UNSET
        else:
            vsr_door_right_rear_close_jellybean = self.vsr_door_right_rear_close_jellybean

        vsr_door_right_rear_open_jellybean: None | str | Unset
        if isinstance(self.vsr_door_right_rear_open_jellybean, Unset):
            vsr_door_right_rear_open_jellybean = UNSET
        else:
            vsr_door_right_rear_open_jellybean = self.vsr_door_right_rear_open_jellybean

        vsr_hood_jellybean: None | str | Unset
        if isinstance(self.vsr_hood_jellybean, Unset):
            vsr_hood_jellybean = UNSET
        else:
            vsr_hood_jellybean = self.vsr_hood_jellybean

        vsr_tailgate_jellybean: None | str | Unset
        if isinstance(self.vsr_tailgate_jellybean, Unset):
            vsr_tailgate_jellybean = UNSET
        else:
            vsr_tailgate_jellybean = self.vsr_tailgate_jellybean

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if home_jellybean is not UNSET:
            field_dict["homeJellybean"] = home_jellybean
        if vehicle_color is not UNSET:
            field_dict["vehicleColor"] = vehicle_color
        if vehicle_model is not UNSET:
            field_dict["vehicleModel"] = vehicle_model
        if vehicle_year is not UNSET:
            field_dict["vehicleYear"] = vehicle_year
        if vsr_body_jellybean is not UNSET:
            field_dict["vsrBodyJellybean"] = vsr_body_jellybean
        if vsr_door_left_front_close_jellybean is not UNSET:
            field_dict["vsrDoorLeftFrontCloseJellybean"] = vsr_door_left_front_close_jellybean
        if vsr_door_left_front_open_jellybean is not UNSET:
            field_dict["vsrDoorLeftFrontOpenJellybean"] = vsr_door_left_front_open_jellybean
        if vsr_door_left_rear_close_jellybean is not UNSET:
            field_dict["vsrDoorLeftRearCloseJellybean"] = vsr_door_left_rear_close_jellybean
        if vsr_door_left_rear_open_jellybean is not UNSET:
            field_dict["vsrDoorLeftRearOpenJellybean"] = vsr_door_left_rear_open_jellybean
        if vsr_door_right_front_close_jellybean is not UNSET:
            field_dict["vsrDoorRightFrontCloseJellybean"] = vsr_door_right_front_close_jellybean
        if vsr_door_right_front_open_jellybean is not UNSET:
            field_dict["vsrDoorRightFrontOpenJellybean"] = vsr_door_right_front_open_jellybean
        if vsr_door_right_rear_close_jellybean is not UNSET:
            field_dict["vsrDoorRightRearCloseJellybean"] = vsr_door_right_rear_close_jellybean
        if vsr_door_right_rear_open_jellybean is not UNSET:
            field_dict["vsrDoorRightRearOpenJellybean"] = vsr_door_right_rear_open_jellybean
        if vsr_hood_jellybean is not UNSET:
            field_dict["vsrHoodJellybean"] = vsr_hood_jellybean
        if vsr_tailgate_jellybean is not UNSET:
            field_dict["vsrTailgateJellybean"] = vsr_tailgate_jellybean

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_home_jellybean(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        home_jellybean = _parse_home_jellybean(d.pop("homeJellybean", UNSET))

        def _parse_vehicle_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vehicle_color = _parse_vehicle_color(d.pop("vehicleColor", UNSET))

        def _parse_vehicle_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vehicle_model = _parse_vehicle_model(d.pop("vehicleModel", UNSET))

        def _parse_vehicle_year(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vehicle_year = _parse_vehicle_year(d.pop("vehicleYear", UNSET))

        def _parse_vsr_body_jellybean(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vsr_body_jellybean = _parse_vsr_body_jellybean(d.pop("vsrBodyJellybean", UNSET))

        def _parse_vsr_door_left_front_close_jellybean(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vsr_door_left_front_close_jellybean = _parse_vsr_door_left_front_close_jellybean(
            d.pop("vsrDoorLeftFrontCloseJellybean", UNSET)
        )

        def _parse_vsr_door_left_front_open_jellybean(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vsr_door_left_front_open_jellybean = _parse_vsr_door_left_front_open_jellybean(
            d.pop("vsrDoorLeftFrontOpenJellybean", UNSET)
        )

        def _parse_vsr_door_left_rear_close_jellybean(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vsr_door_left_rear_close_jellybean = _parse_vsr_door_left_rear_close_jellybean(
            d.pop("vsrDoorLeftRearCloseJellybean", UNSET)
        )

        def _parse_vsr_door_left_rear_open_jellybean(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vsr_door_left_rear_open_jellybean = _parse_vsr_door_left_rear_open_jellybean(
            d.pop("vsrDoorLeftRearOpenJellybean", UNSET)
        )

        def _parse_vsr_door_right_front_close_jellybean(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vsr_door_right_front_close_jellybean = _parse_vsr_door_right_front_close_jellybean(
            d.pop("vsrDoorRightFrontCloseJellybean", UNSET)
        )

        def _parse_vsr_door_right_front_open_jellybean(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vsr_door_right_front_open_jellybean = _parse_vsr_door_right_front_open_jellybean(
            d.pop("vsrDoorRightFrontOpenJellybean", UNSET)
        )

        def _parse_vsr_door_right_rear_close_jellybean(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vsr_door_right_rear_close_jellybean = _parse_vsr_door_right_rear_close_jellybean(
            d.pop("vsrDoorRightRearCloseJellybean", UNSET)
        )

        def _parse_vsr_door_right_rear_open_jellybean(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vsr_door_right_rear_open_jellybean = _parse_vsr_door_right_rear_open_jellybean(
            d.pop("vsrDoorRightRearOpenJellybean", UNSET)
        )

        def _parse_vsr_hood_jellybean(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vsr_hood_jellybean = _parse_vsr_hood_jellybean(d.pop("vsrHoodJellybean", UNSET))

        def _parse_vsr_tailgate_jellybean(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vsr_tailgate_jellybean = _parse_vsr_tailgate_jellybean(d.pop("vsrTailgateJellybean", UNSET))

        jellybean_entity = cls(
            home_jellybean=home_jellybean,
            vehicle_color=vehicle_color,
            vehicle_model=vehicle_model,
            vehicle_year=vehicle_year,
            vsr_body_jellybean=vsr_body_jellybean,
            vsr_door_left_front_close_jellybean=vsr_door_left_front_close_jellybean,
            vsr_door_left_front_open_jellybean=vsr_door_left_front_open_jellybean,
            vsr_door_left_rear_close_jellybean=vsr_door_left_rear_close_jellybean,
            vsr_door_left_rear_open_jellybean=vsr_door_left_rear_open_jellybean,
            vsr_door_right_front_close_jellybean=vsr_door_right_front_close_jellybean,
            vsr_door_right_front_open_jellybean=vsr_door_right_front_open_jellybean,
            vsr_door_right_rear_close_jellybean=vsr_door_right_rear_close_jellybean,
            vsr_door_right_rear_open_jellybean=vsr_door_right_rear_open_jellybean,
            vsr_hood_jellybean=vsr_hood_jellybean,
            vsr_tailgate_jellybean=vsr_tailgate_jellybean,
        )

        jellybean_entity.additional_properties = d
        return jellybean_entity

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
