from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jellybean_entity import JellybeanEntity
    from ..models.meta_data_entity import MetaDataEntity
    from ..models.pair_vehicle_otp_config import PairVehicleOtpConfig
    from ..models.vehicle_brands_entity import VehicleBrandsEntity
    from ..models.vehicle_connectivity import VehicleConnectivity
    from ..models.vehicle_exterior_color import VehicleExteriorColor
    from ..models.vehicle_localization_entity import VehicleLocalizationEntity
    from ..models.vehicle_model import VehicleModel


T = TypeVar("T", bound="Vehicle")


@_attrs_define
class Vehicle:
    """
    Attributes:
        brands (VehicleBrandsEntity | Unset):
        default_vehicle_color (None | str | Unset):
        exterior_color (VehicleExteriorColor | Unset):
        internal_vin (None | str | Unset): Internal VIN from `getVehicleList` (`vinList`), omitted when not provided.
            Example: JA4XXXXXXXXXXXXXX.
        is_fleet (bool | None | Unset):
        is_primary (bool | None | Unset):
        is_selected (bool | Unset):  Default: False.
        is_xbadge_flag (bool | None | str | Unset): Sent as the string `"true"` or `"false"`; kept permissive.
        jellybean_model (JellybeanEntity | Unset):
        license_plate_number (None | str | Unset):
        localization (VehicleLocalizationEntity | Unset):
        meta_data (MetaDataEntity | Unset):
        model (VehicleModel | Unset):
        model_code (None | str | Unset):
        nick_name (None | str | Unset):
        otp_config (PairVehicleOtpConfig | Unset):
        pair_vehicle_method (None | str | Unset): 0 KeyFob, 1 Otp, 2 Ivi, 3 Icall.
        trial_eligible (bool | None | Unset):
        user_associated (bool | None | Unset):
        vehicle_connectivity (VehicleConnectivity | Unset):
        vehicle_country_code (None | str | Unset):
        vehicle_display_name (None | str | Unset):
        vehicle_type (None | str | Unset): `ice`, `phev` or `ev`.
        vin (str | Unset): 17-character Vehicle Identification Number. Always sent for vehicle-scoped calls. Default:
            ''. Example: JA4XXXXXXXXXXXXXX.
    """

    brands: VehicleBrandsEntity | Unset = UNSET
    default_vehicle_color: None | str | Unset = UNSET
    exterior_color: VehicleExteriorColor | Unset = UNSET
    internal_vin: None | str | Unset = UNSET
    is_fleet: bool | None | Unset = UNSET
    is_primary: bool | None | Unset = UNSET
    is_selected: bool | Unset = False
    is_xbadge_flag: bool | None | str | Unset = UNSET
    jellybean_model: JellybeanEntity | Unset = UNSET
    license_plate_number: None | str | Unset = UNSET
    localization: VehicleLocalizationEntity | Unset = UNSET
    meta_data: MetaDataEntity | Unset = UNSET
    model: VehicleModel | Unset = UNSET
    model_code: None | str | Unset = UNSET
    nick_name: None | str | Unset = UNSET
    otp_config: PairVehicleOtpConfig | Unset = UNSET
    pair_vehicle_method: None | str | Unset = UNSET
    trial_eligible: bool | None | Unset = UNSET
    user_associated: bool | None | Unset = UNSET
    vehicle_connectivity: VehicleConnectivity | Unset = UNSET
    vehicle_country_code: None | str | Unset = UNSET
    vehicle_display_name: None | str | Unset = UNSET
    vehicle_type: None | str | Unset = UNSET
    vin: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brands: dict[str, Any] | Unset = UNSET
        if not isinstance(self.brands, Unset):
            brands = self.brands.to_dict()

        default_vehicle_color: None | str | Unset
        if isinstance(self.default_vehicle_color, Unset):
            default_vehicle_color = UNSET
        else:
            default_vehicle_color = self.default_vehicle_color

        exterior_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exterior_color, Unset):
            exterior_color = self.exterior_color.to_dict()

        internal_vin: None | str | Unset
        if isinstance(self.internal_vin, Unset):
            internal_vin = UNSET
        else:
            internal_vin = self.internal_vin

        is_fleet: bool | None | Unset
        if isinstance(self.is_fleet, Unset):
            is_fleet = UNSET
        else:
            is_fleet = self.is_fleet

        is_primary: bool | None | Unset
        if isinstance(self.is_primary, Unset):
            is_primary = UNSET
        else:
            is_primary = self.is_primary

        is_selected = self.is_selected

        is_xbadge_flag: bool | None | str | Unset
        if isinstance(self.is_xbadge_flag, Unset):
            is_xbadge_flag = UNSET
        else:
            is_xbadge_flag = self.is_xbadge_flag

        jellybean_model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.jellybean_model, Unset):
            jellybean_model = self.jellybean_model.to_dict()

        license_plate_number: None | str | Unset
        if isinstance(self.license_plate_number, Unset):
            license_plate_number = UNSET
        else:
            license_plate_number = self.license_plate_number

        localization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.localization, Unset):
            localization = self.localization.to_dict()

        meta_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta_data, Unset):
            meta_data = self.meta_data.to_dict()

        model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.to_dict()

        model_code: None | str | Unset
        if isinstance(self.model_code, Unset):
            model_code = UNSET
        else:
            model_code = self.model_code

        nick_name: None | str | Unset
        if isinstance(self.nick_name, Unset):
            nick_name = UNSET
        else:
            nick_name = self.nick_name

        otp_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.otp_config, Unset):
            otp_config = self.otp_config.to_dict()

        pair_vehicle_method: None | str | Unset
        if isinstance(self.pair_vehicle_method, Unset):
            pair_vehicle_method = UNSET
        else:
            pair_vehicle_method = self.pair_vehicle_method

        trial_eligible: bool | None | Unset
        if isinstance(self.trial_eligible, Unset):
            trial_eligible = UNSET
        else:
            trial_eligible = self.trial_eligible

        user_associated: bool | None | Unset
        if isinstance(self.user_associated, Unset):
            user_associated = UNSET
        else:
            user_associated = self.user_associated

        vehicle_connectivity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vehicle_connectivity, Unset):
            vehicle_connectivity = self.vehicle_connectivity.to_dict()

        vehicle_country_code: None | str | Unset
        if isinstance(self.vehicle_country_code, Unset):
            vehicle_country_code = UNSET
        else:
            vehicle_country_code = self.vehicle_country_code

        vehicle_display_name: None | str | Unset
        if isinstance(self.vehicle_display_name, Unset):
            vehicle_display_name = UNSET
        else:
            vehicle_display_name = self.vehicle_display_name

        vehicle_type: None | str | Unset
        if isinstance(self.vehicle_type, Unset):
            vehicle_type = UNSET
        else:
            vehicle_type = self.vehicle_type

        vin = self.vin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if brands is not UNSET:
            field_dict["brands"] = brands
        if default_vehicle_color is not UNSET:
            field_dict["defaultVehicleColor"] = default_vehicle_color
        if exterior_color is not UNSET:
            field_dict["exteriorColor"] = exterior_color
        if internal_vin is not UNSET:
            field_dict["internalVin"] = internal_vin
        if is_fleet is not UNSET:
            field_dict["isFleet"] = is_fleet
        if is_primary is not UNSET:
            field_dict["isPrimary"] = is_primary
        if is_selected is not UNSET:
            field_dict["isSelected"] = is_selected
        if is_xbadge_flag is not UNSET:
            field_dict["isXbadgeFlag"] = is_xbadge_flag
        if jellybean_model is not UNSET:
            field_dict["jellybeanModel"] = jellybean_model
        if license_plate_number is not UNSET:
            field_dict["licensePlateNumber"] = license_plate_number
        if localization is not UNSET:
            field_dict["localization"] = localization
        if meta_data is not UNSET:
            field_dict["metaData"] = meta_data
        if model is not UNSET:
            field_dict["model"] = model
        if model_code is not UNSET:
            field_dict["modelCode"] = model_code
        if nick_name is not UNSET:
            field_dict["nickName"] = nick_name
        if otp_config is not UNSET:
            field_dict["otpConfig"] = otp_config
        if pair_vehicle_method is not UNSET:
            field_dict["pairVehicleMethod"] = pair_vehicle_method
        if trial_eligible is not UNSET:
            field_dict["trialEligible"] = trial_eligible
        if user_associated is not UNSET:
            field_dict["userAssociated"] = user_associated
        if vehicle_connectivity is not UNSET:
            field_dict["vehicleConnectivity"] = vehicle_connectivity
        if vehicle_country_code is not UNSET:
            field_dict["vehicleCountryCode"] = vehicle_country_code
        if vehicle_display_name is not UNSET:
            field_dict["vehicleDisplayName"] = vehicle_display_name
        if vehicle_type is not UNSET:
            field_dict["vehicleType"] = vehicle_type
        if vin is not UNSET:
            field_dict["vin"] = vin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jellybean_entity import JellybeanEntity  # noqa: PLC0415
        from ..models.meta_data_entity import MetaDataEntity  # noqa: PLC0415
        from ..models.pair_vehicle_otp_config import PairVehicleOtpConfig  # noqa: PLC0415
        from ..models.vehicle_brands_entity import VehicleBrandsEntity  # noqa: PLC0415
        from ..models.vehicle_connectivity import VehicleConnectivity  # noqa: PLC0415
        from ..models.vehicle_exterior_color import VehicleExteriorColor  # noqa: PLC0415
        from ..models.vehicle_localization_entity import VehicleLocalizationEntity  # noqa: PLC0415
        from ..models.vehicle_model import VehicleModel  # noqa: PLC0415

        d = dict(src_dict)
        _brands = d.pop("brands", UNSET)
        brands: VehicleBrandsEntity | Unset
        if isinstance(_brands, Unset):
            brands = UNSET
        else:
            brands = VehicleBrandsEntity.from_dict(_brands)

        def _parse_default_vehicle_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_vehicle_color = _parse_default_vehicle_color(d.pop("defaultVehicleColor", UNSET))

        _exterior_color = d.pop("exteriorColor", UNSET)
        exterior_color: VehicleExteriorColor | Unset
        if isinstance(_exterior_color, Unset):
            exterior_color = UNSET
        else:
            exterior_color = VehicleExteriorColor.from_dict(_exterior_color)

        def _parse_internal_vin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_vin = _parse_internal_vin(d.pop("internalVin", UNSET))

        def _parse_is_fleet(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_fleet = _parse_is_fleet(d.pop("isFleet", UNSET))

        def _parse_is_primary(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_primary = _parse_is_primary(d.pop("isPrimary", UNSET))

        is_selected = d.pop("isSelected", UNSET)

        def _parse_is_xbadge_flag(data: object) -> bool | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | str | Unset, data)

        is_xbadge_flag = _parse_is_xbadge_flag(d.pop("isXbadgeFlag", UNSET))

        _jellybean_model = d.pop("jellybeanModel", UNSET)
        jellybean_model: JellybeanEntity | Unset
        if isinstance(_jellybean_model, Unset):
            jellybean_model = UNSET
        else:
            jellybean_model = JellybeanEntity.from_dict(_jellybean_model)

        def _parse_license_plate_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        license_plate_number = _parse_license_plate_number(d.pop("licensePlateNumber", UNSET))

        _localization = d.pop("localization", UNSET)
        localization: VehicleLocalizationEntity | Unset
        if isinstance(_localization, Unset):
            localization = UNSET
        else:
            localization = VehicleLocalizationEntity.from_dict(_localization)

        _meta_data = d.pop("metaData", UNSET)
        meta_data: MetaDataEntity | Unset
        if isinstance(_meta_data, Unset):
            meta_data = UNSET
        else:
            meta_data = MetaDataEntity.from_dict(_meta_data)

        _model = d.pop("model", UNSET)
        model: VehicleModel | Unset
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = VehicleModel.from_dict(_model)

        def _parse_model_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_code = _parse_model_code(d.pop("modelCode", UNSET))

        def _parse_nick_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nick_name = _parse_nick_name(d.pop("nickName", UNSET))

        _otp_config = d.pop("otpConfig", UNSET)
        otp_config: PairVehicleOtpConfig | Unset
        if isinstance(_otp_config, Unset):
            otp_config = UNSET
        else:
            otp_config = PairVehicleOtpConfig.from_dict(_otp_config)

        def _parse_pair_vehicle_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pair_vehicle_method = _parse_pair_vehicle_method(d.pop("pairVehicleMethod", UNSET))

        def _parse_trial_eligible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        trial_eligible = _parse_trial_eligible(d.pop("trialEligible", UNSET))

        def _parse_user_associated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        user_associated = _parse_user_associated(d.pop("userAssociated", UNSET))

        _vehicle_connectivity = d.pop("vehicleConnectivity", UNSET)
        vehicle_connectivity: VehicleConnectivity | Unset
        if isinstance(_vehicle_connectivity, Unset):
            vehicle_connectivity = UNSET
        else:
            vehicle_connectivity = VehicleConnectivity.from_dict(_vehicle_connectivity)

        def _parse_vehicle_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vehicle_country_code = _parse_vehicle_country_code(d.pop("vehicleCountryCode", UNSET))

        def _parse_vehicle_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vehicle_display_name = _parse_vehicle_display_name(d.pop("vehicleDisplayName", UNSET))

        def _parse_vehicle_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vehicle_type = _parse_vehicle_type(d.pop("vehicleType", UNSET))

        vin = d.pop("vin", UNSET)

        vehicle = cls(
            brands=brands,
            default_vehicle_color=default_vehicle_color,
            exterior_color=exterior_color,
            internal_vin=internal_vin,
            is_fleet=is_fleet,
            is_primary=is_primary,
            is_selected=is_selected,
            is_xbadge_flag=is_xbadge_flag,
            jellybean_model=jellybean_model,
            license_plate_number=license_plate_number,
            localization=localization,
            meta_data=meta_data,
            model=model,
            model_code=model_code,
            nick_name=nick_name,
            otp_config=otp_config,
            pair_vehicle_method=pair_vehicle_method,
            trial_eligible=trial_eligible,
            user_associated=user_associated,
            vehicle_connectivity=vehicle_connectivity,
            vehicle_country_code=vehicle_country_code,
            vehicle_display_name=vehicle_display_name,
            vehicle_type=vehicle_type,
            vin=vin,
        )

        vehicle.additional_properties = d
        return vehicle

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
