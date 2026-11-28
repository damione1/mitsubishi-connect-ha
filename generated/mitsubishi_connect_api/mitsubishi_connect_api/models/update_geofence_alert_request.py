from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_geofence_alert_request_geofence_status import UpdateGeofenceAlertRequestGeofenceStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.geofence_spatial_details_request_entity import GeofenceSpatialDetailsRequestEntity


T = TypeVar("T", bound="UpdateGeofenceAlertRequest")


@_attrs_define
class UpdateGeofenceAlertRequest:
    """
    Attributes:
        geofence_spatial_details (GeofenceSpatialDetailsRequestEntity):
        geofence_status (UpdateGeofenceAlertRequestGeofenceStatus): 0 disabled, 1 enabled.
        geofence_id (None | str | Unset):
        geofence_name (None | str | Unset):
        internal_vin (None | str | Unset): Internal VIN from `getVehicleList` (`vinList`), omitted when not provided.
            Example: JA4XXXXXXXXXXXXXX.
        support_polling_flag (bool | None | Unset): When `true`, the server returns a `requestId` to poll with
            `getBatchRequestStatus`.
        type_ (int | None | Unset):
        vin (None | str | Unset): 17-character Vehicle Identification Number. Always sent for vehicle-scoped calls.
            Example: JA4XXXXXXXXXXXXXX.
    """

    geofence_spatial_details: GeofenceSpatialDetailsRequestEntity
    geofence_status: UpdateGeofenceAlertRequestGeofenceStatus
    geofence_id: None | str | Unset = UNSET
    geofence_name: None | str | Unset = UNSET
    internal_vin: None | str | Unset = UNSET
    support_polling_flag: bool | None | Unset = UNSET
    type_: int | None | Unset = UNSET
    vin: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        geofence_spatial_details = self.geofence_spatial_details.to_dict()

        geofence_status = self.geofence_status.value

        geofence_id: None | str | Unset
        if isinstance(self.geofence_id, Unset):
            geofence_id = UNSET
        else:
            geofence_id = self.geofence_id

        geofence_name: None | str | Unset
        if isinstance(self.geofence_name, Unset):
            geofence_name = UNSET
        else:
            geofence_name = self.geofence_name

        internal_vin: None | str | Unset
        if isinstance(self.internal_vin, Unset):
            internal_vin = UNSET
        else:
            internal_vin = self.internal_vin

        support_polling_flag: bool | None | Unset
        if isinstance(self.support_polling_flag, Unset):
            support_polling_flag = UNSET
        else:
            support_polling_flag = self.support_polling_flag

        type_: int | None | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        vin: None | str | Unset
        if isinstance(self.vin, Unset):
            vin = UNSET
        else:
            vin = self.vin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "geofenceSpatialDetails": geofence_spatial_details,
                "geofenceStatus": geofence_status,
            }
        )
        if geofence_id is not UNSET:
            field_dict["geofenceId"] = geofence_id
        if geofence_name is not UNSET:
            field_dict["geofenceName"] = geofence_name
        if internal_vin is not UNSET:
            field_dict["internalVin"] = internal_vin
        if support_polling_flag is not UNSET:
            field_dict["supportPollingFlag"] = support_polling_flag
        if type_ is not UNSET:
            field_dict["type"] = type_
        if vin is not UNSET:
            field_dict["vin"] = vin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.geofence_spatial_details_request_entity import GeofenceSpatialDetailsRequestEntity  # noqa: PLC0415

        d = dict(src_dict)
        geofence_spatial_details = GeofenceSpatialDetailsRequestEntity.from_dict(d.pop("geofenceSpatialDetails"))

        geofence_status = UpdateGeofenceAlertRequestGeofenceStatus(d.pop("geofenceStatus"))

        def _parse_geofence_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geofence_id = _parse_geofence_id(d.pop("geofenceId", UNSET))

        def _parse_geofence_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geofence_name = _parse_geofence_name(d.pop("geofenceName", UNSET))

        def _parse_internal_vin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_vin = _parse_internal_vin(d.pop("internalVin", UNSET))

        def _parse_support_polling_flag(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        support_polling_flag = _parse_support_polling_flag(d.pop("supportPollingFlag", UNSET))

        def _parse_type_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_vin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vin = _parse_vin(d.pop("vin", UNSET))

        update_geofence_alert_request = cls(
            geofence_spatial_details=geofence_spatial_details,
            geofence_status=geofence_status,
            geofence_id=geofence_id,
            geofence_name=geofence_name,
            internal_vin=internal_vin,
            support_polling_flag=support_polling_flag,
            type_=type_,
            vin=vin,
        )

        update_geofence_alert_request.additional_properties = d
        return update_geofence_alert_request

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
