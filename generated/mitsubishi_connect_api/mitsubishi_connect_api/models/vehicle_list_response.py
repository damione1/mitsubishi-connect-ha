from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_vin_entity import InternalVinEntity
    from ..models.vehicle import Vehicle


T = TypeVar("T", bound="VehicleListResponse")


@_attrs_define
class VehicleListResponse:
    """
    Attributes:
        call_center_language (None | str | Unset):
        set_pin_flag (bool | None | Unset):
        vehicles (list[Vehicle] | Unset):
        vin_list (list[InternalVinEntity] | Unset):
    """

    call_center_language: None | str | Unset = UNSET
    set_pin_flag: bool | None | Unset = UNSET
    vehicles: list[Vehicle] | Unset = UNSET
    vin_list: list[InternalVinEntity] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        call_center_language: None | str | Unset
        if isinstance(self.call_center_language, Unset):
            call_center_language = UNSET
        else:
            call_center_language = self.call_center_language

        set_pin_flag: bool | None | Unset
        if isinstance(self.set_pin_flag, Unset):
            set_pin_flag = UNSET
        else:
            set_pin_flag = self.set_pin_flag

        vehicles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vehicles, Unset):
            vehicles = []
            for vehicles_item_data in self.vehicles:
                vehicles_item = vehicles_item_data.to_dict()
                vehicles.append(vehicles_item)

        vin_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vin_list, Unset):
            vin_list = []
            for vin_list_item_data in self.vin_list:
                vin_list_item = vin_list_item_data.to_dict()
                vin_list.append(vin_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if call_center_language is not UNSET:
            field_dict["callCenterLanguage"] = call_center_language
        if set_pin_flag is not UNSET:
            field_dict["setPINFlag"] = set_pin_flag
        if vehicles is not UNSET:
            field_dict["vehicles"] = vehicles
        if vin_list is not UNSET:
            field_dict["vinList"] = vin_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_vin_entity import InternalVinEntity  # noqa: PLC0415
        from ..models.vehicle import Vehicle  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_call_center_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        call_center_language = _parse_call_center_language(d.pop("callCenterLanguage", UNSET))

        def _parse_set_pin_flag(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        set_pin_flag = _parse_set_pin_flag(d.pop("setPINFlag", UNSET))

        _vehicles = d.pop("vehicles", UNSET)
        vehicles: list[Vehicle] | Unset = UNSET
        if _vehicles is not UNSET:
            vehicles = []
            for vehicles_item_data in _vehicles:
                vehicles_item = Vehicle.from_dict(vehicles_item_data)

                vehicles.append(vehicles_item)

        _vin_list = d.pop("vinList", UNSET)
        vin_list: list[InternalVinEntity] | Unset = UNSET
        if _vin_list is not UNSET:
            vin_list = []
            for vin_list_item_data in _vin_list:
                vin_list_item = InternalVinEntity.from_dict(vin_list_item_data)

                vin_list.append(vin_list_item)

        vehicle_list_response = cls(
            call_center_language=call_center_language,
            set_pin_flag=set_pin_flag,
            vehicles=vehicles,
            vin_list=vin_list,
        )

        vehicle_list_response.additional_properties = d
        return vehicle_list_response

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
