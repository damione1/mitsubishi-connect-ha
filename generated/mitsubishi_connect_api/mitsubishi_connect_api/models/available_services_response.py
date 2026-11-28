from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.available_service_item import AvailableServiceItem


T = TypeVar("T", bound="AvailableServicesResponse")


@_attrs_define
class AvailableServicesResponse:
    """
    Attributes:
        available_service_force_check (bool | None | Unset):  Default: False.
        services (list[AvailableServiceItem] | Unset):
    """

    available_service_force_check: bool | None | Unset = False
    services: list[AvailableServiceItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_service_force_check: bool | None | Unset
        if isinstance(self.available_service_force_check, Unset):
            available_service_force_check = UNSET
        else:
            available_service_force_check = self.available_service_force_check

        services: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_service_force_check is not UNSET:
            field_dict["availableServiceForceCheck"] = available_service_force_check
        if services is not UNSET:
            field_dict["services"] = services

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.available_service_item import AvailableServiceItem  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_available_service_force_check(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        available_service_force_check = _parse_available_service_force_check(d.pop("availableServiceForceCheck", UNSET))

        _services = d.pop("services", UNSET)
        services: list[AvailableServiceItem] | Unset = UNSET
        if _services is not UNSET:
            services = []
            for services_item_data in _services:
                services_item = AvailableServiceItem.from_dict(services_item_data)

                services.append(services_item)

        available_services_response = cls(
            available_service_force_check=available_service_force_check,
            services=services,
        )

        available_services_response.additional_properties = d
        return available_services_response

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
