from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hvac_settings_entity import HVACSettingsEntity


T = TypeVar("T", bound="AvailableServiceItem")


@_attrs_define
class AvailableServiceItem:
    """
    Attributes:
        available_service_id (int | None | Unset):
        hvac_settings (HVACSettingsEntity | Unset):
        is_active (bool | None | Unset):  Default: True.
        is_initial (bool | None | Unset):  Default: False.
        is_ui_visible (bool | None | Unset):  Default: True.
        modified_at (None | str | Unset):
        version (None | str | Unset):
    """

    available_service_id: int | None | Unset = UNSET
    hvac_settings: HVACSettingsEntity | Unset = UNSET
    is_active: bool | None | Unset = True
    is_initial: bool | None | Unset = False
    is_ui_visible: bool | None | Unset = True
    modified_at: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_service_id: int | None | Unset
        if isinstance(self.available_service_id, Unset):
            available_service_id = UNSET
        else:
            available_service_id = self.available_service_id

        hvac_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hvac_settings, Unset):
            hvac_settings = self.hvac_settings.to_dict()

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        is_initial: bool | None | Unset
        if isinstance(self.is_initial, Unset):
            is_initial = UNSET
        else:
            is_initial = self.is_initial

        is_ui_visible: bool | None | Unset
        if isinstance(self.is_ui_visible, Unset):
            is_ui_visible = UNSET
        else:
            is_ui_visible = self.is_ui_visible

        modified_at: None | str | Unset
        if isinstance(self.modified_at, Unset):
            modified_at = UNSET
        else:
            modified_at = self.modified_at

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_service_id is not UNSET:
            field_dict["availableServiceId"] = available_service_id
        if hvac_settings is not UNSET:
            field_dict["hvacSettings"] = hvac_settings
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if is_initial is not UNSET:
            field_dict["isInitial"] = is_initial
        if is_ui_visible is not UNSET:
            field_dict["isUIVisible"] = is_ui_visible
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hvac_settings_entity import HVACSettingsEntity  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_available_service_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        available_service_id = _parse_available_service_id(d.pop("availableServiceId", UNSET))

        _hvac_settings = d.pop("hvacSettings", UNSET)
        hvac_settings: HVACSettingsEntity | Unset
        if isinstance(_hvac_settings, Unset):
            hvac_settings = UNSET
        else:
            hvac_settings = HVACSettingsEntity.from_dict(_hvac_settings)

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("isActive", UNSET))

        def _parse_is_initial(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_initial = _parse_is_initial(d.pop("isInitial", UNSET))

        def _parse_is_ui_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_ui_visible = _parse_is_ui_visible(d.pop("isUIVisible", UNSET))

        def _parse_modified_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        modified_at = _parse_modified_at(d.pop("modifiedAt", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        available_service_item = cls(
            available_service_id=available_service_id,
            hvac_settings=hvac_settings,
            is_active=is_active,
            is_initial=is_initial,
            is_ui_visible=is_ui_visible,
            modified_at=modified_at,
            version=version,
        )

        available_service_item.additional_properties = d
        return available_service_item

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
