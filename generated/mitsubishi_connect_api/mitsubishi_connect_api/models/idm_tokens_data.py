from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.idm_tokens_data_extra_data import IdmTokensDataExtraData
    from ..models.idm_tokens_data_meta_data import IdmTokensDataMetaData


T = TypeVar("T", bound="IdmTokensData")


@_attrs_define
class IdmTokensData:
    """
    Attributes:
        access_token (str | Unset):  Example: eyJhbGciOiJIUzI1NiJ9.example.signature.
        address (None | str | Unset):
        avatar (None | str | Unset):
        birthday (None | str | Unset):
        city (None | str | Unset):
        client_id (None | str | Unset): IDM client id from the regional configuration. Example: example-client-id.
        country (None | str | Unset):
        email (None | str | Unset):  Example: driver@example.com.
        encrypt_password (None | str | Unset):
        expires_in (int | Unset):
        extra_data (IdmTokensDataExtraData | Unset):
        first_name (None | str | Unset):  Example: Alex.
        gender (int | None | str | Unset): String on login, integer on refresh.
        id (None | str | Unset):
        is_email_verified (bool | None | Unset):  Default: False.
        is_mobile_verified (bool | None | Unset):  Default: False.
        is_temporary_password (bool | None | Unset):  Default: False.
        last_login_ip (None | str | Unset):
        last_login_time (None | str | Unset):
        last_name (None | str | Unset):  Example: Doe.
        locale (None | str | Unset):
        login_by (None | str | Unset):
        login_count (None | str | Unset):
        meta_data (IdmTokensDataMetaData | Unset):
        middle_name (None | str | Unset):
        mobile (None | str | Unset):  Example: 555-0100.
        nickname (None | str | Unset):
        openid (None | str | Unset):
        org_code (None | str | Unset):
        partner_1_id (None | str | Unset):
        partner_2_id (None | str | Unset):
        refresh_token (str | Unset):  Example: eyJhbGciOiJIUzI1NiJ9.example.refresh.
        register_date (None | str | Unset):
        register_type (None | str | Unset):
        state (None | str | Unset):
        street1 (None | str | Unset):
        street2 (None | str | Unset):
        street3 (None | str | Unset):
        token_type (str | Unset):
        username (None | str | Unset):  Example: owner@example.com.
        zip_code (None | str | Unset):
        account_link_url (None | str | Unset):
        error_msg (None | str | Unset):
        link_status (bool | None | Unset):
    """

    access_token: str | Unset = UNSET
    address: None | str | Unset = UNSET
    avatar: None | str | Unset = UNSET
    birthday: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    client_id: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    encrypt_password: None | str | Unset = UNSET
    expires_in: int | Unset = UNSET
    extra_data: IdmTokensDataExtraData | Unset = UNSET
    first_name: None | str | Unset = UNSET
    gender: int | None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    is_email_verified: bool | None | Unset = False
    is_mobile_verified: bool | None | Unset = False
    is_temporary_password: bool | None | Unset = False
    last_login_ip: None | str | Unset = UNSET
    last_login_time: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    locale: None | str | Unset = UNSET
    login_by: None | str | Unset = UNSET
    login_count: None | str | Unset = UNSET
    meta_data: IdmTokensDataMetaData | Unset = UNSET
    middle_name: None | str | Unset = UNSET
    mobile: None | str | Unset = UNSET
    nickname: None | str | Unset = UNSET
    openid: None | str | Unset = UNSET
    org_code: None | str | Unset = UNSET
    partner_1_id: None | str | Unset = UNSET
    partner_2_id: None | str | Unset = UNSET
    refresh_token: str | Unset = UNSET
    register_date: None | str | Unset = UNSET
    register_type: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    street1: None | str | Unset = UNSET
    street2: None | str | Unset = UNSET
    street3: None | str | Unset = UNSET
    token_type: str | Unset = UNSET
    username: None | str | Unset = UNSET
    zip_code: None | str | Unset = UNSET
    account_link_url: None | str | Unset = UNSET
    error_msg: None | str | Unset = UNSET
    link_status: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        avatar: None | str | Unset
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        else:
            avatar = self.avatar

        birthday: None | str | Unset
        if isinstance(self.birthday, Unset):
            birthday = UNSET
        else:
            birthday = self.birthday

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        client_id: None | str | Unset
        if isinstance(self.client_id, Unset):
            client_id = UNSET
        else:
            client_id = self.client_id

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        encrypt_password: None | str | Unset
        if isinstance(self.encrypt_password, Unset):
            encrypt_password = UNSET
        else:
            encrypt_password = self.encrypt_password

        expires_in = self.expires_in

        extra_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extra_data, Unset):
            extra_data = self.extra_data.to_dict()

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        gender: int | None | str | Unset
        if isinstance(self.gender, Unset):
            gender = UNSET
        else:
            gender = self.gender

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        is_email_verified: bool | None | Unset
        if isinstance(self.is_email_verified, Unset):
            is_email_verified = UNSET
        else:
            is_email_verified = self.is_email_verified

        is_mobile_verified: bool | None | Unset
        if isinstance(self.is_mobile_verified, Unset):
            is_mobile_verified = UNSET
        else:
            is_mobile_verified = self.is_mobile_verified

        is_temporary_password: bool | None | Unset
        if isinstance(self.is_temporary_password, Unset):
            is_temporary_password = UNSET
        else:
            is_temporary_password = self.is_temporary_password

        last_login_ip: None | str | Unset
        if isinstance(self.last_login_ip, Unset):
            last_login_ip = UNSET
        else:
            last_login_ip = self.last_login_ip

        last_login_time: None | str | Unset
        if isinstance(self.last_login_time, Unset):
            last_login_time = UNSET
        else:
            last_login_time = self.last_login_time

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        locale: None | str | Unset
        if isinstance(self.locale, Unset):
            locale = UNSET
        else:
            locale = self.locale

        login_by: None | str | Unset
        if isinstance(self.login_by, Unset):
            login_by = UNSET
        else:
            login_by = self.login_by

        login_count: None | str | Unset
        if isinstance(self.login_count, Unset):
            login_count = UNSET
        else:
            login_count = self.login_count

        meta_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta_data, Unset):
            meta_data = self.meta_data.to_dict()

        middle_name: None | str | Unset
        if isinstance(self.middle_name, Unset):
            middle_name = UNSET
        else:
            middle_name = self.middle_name

        mobile: None | str | Unset
        if isinstance(self.mobile, Unset):
            mobile = UNSET
        else:
            mobile = self.mobile

        nickname: None | str | Unset
        if isinstance(self.nickname, Unset):
            nickname = UNSET
        else:
            nickname = self.nickname

        openid: None | str | Unset
        if isinstance(self.openid, Unset):
            openid = UNSET
        else:
            openid = self.openid

        org_code: None | str | Unset
        if isinstance(self.org_code, Unset):
            org_code = UNSET
        else:
            org_code = self.org_code

        partner_1_id: None | str | Unset
        if isinstance(self.partner_1_id, Unset):
            partner_1_id = UNSET
        else:
            partner_1_id = self.partner_1_id

        partner_2_id: None | str | Unset
        if isinstance(self.partner_2_id, Unset):
            partner_2_id = UNSET
        else:
            partner_2_id = self.partner_2_id

        refresh_token = self.refresh_token

        register_date: None | str | Unset
        if isinstance(self.register_date, Unset):
            register_date = UNSET
        else:
            register_date = self.register_date

        register_type: None | str | Unset
        if isinstance(self.register_type, Unset):
            register_type = UNSET
        else:
            register_type = self.register_type

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        street1: None | str | Unset
        if isinstance(self.street1, Unset):
            street1 = UNSET
        else:
            street1 = self.street1

        street2: None | str | Unset
        if isinstance(self.street2, Unset):
            street2 = UNSET
        else:
            street2 = self.street2

        street3: None | str | Unset
        if isinstance(self.street3, Unset):
            street3 = UNSET
        else:
            street3 = self.street3

        token_type = self.token_type

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        zip_code: None | str | Unset
        if isinstance(self.zip_code, Unset):
            zip_code = UNSET
        else:
            zip_code = self.zip_code

        account_link_url: None | str | Unset
        if isinstance(self.account_link_url, Unset):
            account_link_url = UNSET
        else:
            account_link_url = self.account_link_url

        error_msg: None | str | Unset
        if isinstance(self.error_msg, Unset):
            error_msg = UNSET
        else:
            error_msg = self.error_msg

        link_status: bool | None | Unset
        if isinstance(self.link_status, Unset):
            link_status = UNSET
        else:
            link_status = self.link_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["accessToken"] = access_token
        if address is not UNSET:
            field_dict["address"] = address
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if city is not UNSET:
            field_dict["city"] = city
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if country is not UNSET:
            field_dict["country"] = country
        if email is not UNSET:
            field_dict["email"] = email
        if encrypt_password is not UNSET:
            field_dict["encrypt_password"] = encrypt_password
        if expires_in is not UNSET:
            field_dict["expiresIn"] = expires_in
        if extra_data is not UNSET:
            field_dict["extraData"] = extra_data
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if gender is not UNSET:
            field_dict["gender"] = gender
        if id is not UNSET:
            field_dict["id"] = id
        if is_email_verified is not UNSET:
            field_dict["isEmailVerified"] = is_email_verified
        if is_mobile_verified is not UNSET:
            field_dict["isMobileVerified"] = is_mobile_verified
        if is_temporary_password is not UNSET:
            field_dict["isTemporaryPassword"] = is_temporary_password
        if last_login_ip is not UNSET:
            field_dict["last_login_ip"] = last_login_ip
        if last_login_time is not UNSET:
            field_dict["last_login_time"] = last_login_time
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if locale is not UNSET:
            field_dict["locale"] = locale
        if login_by is not UNSET:
            field_dict["loginBy"] = login_by
        if login_count is not UNSET:
            field_dict["login_count"] = login_count
        if meta_data is not UNSET:
            field_dict["metaData"] = meta_data
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if openid is not UNSET:
            field_dict["openid"] = openid
        if org_code is not UNSET:
            field_dict["org_code"] = org_code
        if partner_1_id is not UNSET:
            field_dict["partner1Id"] = partner_1_id
        if partner_2_id is not UNSET:
            field_dict["partner2Id"] = partner_2_id
        if refresh_token is not UNSET:
            field_dict["refreshToken"] = refresh_token
        if register_date is not UNSET:
            field_dict["register_date"] = register_date
        if register_type is not UNSET:
            field_dict["register_type"] = register_type
        if state is not UNSET:
            field_dict["state"] = state
        if street1 is not UNSET:
            field_dict["street1"] = street1
        if street2 is not UNSET:
            field_dict["street2"] = street2
        if street3 is not UNSET:
            field_dict["street3"] = street3
        if token_type is not UNSET:
            field_dict["tokenType"] = token_type
        if username is not UNSET:
            field_dict["username"] = username
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code
        if account_link_url is not UNSET:
            field_dict["accountLinkUrl"] = account_link_url
        if error_msg is not UNSET:
            field_dict["errorMsg"] = error_msg
        if link_status is not UNSET:
            field_dict["linkStatus"] = link_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.idm_tokens_data_extra_data import IdmTokensDataExtraData  # noqa: PLC0415
        from ..models.idm_tokens_data_meta_data import IdmTokensDataMetaData  # noqa: PLC0415

        d = dict(src_dict)
        access_token = d.pop("accessToken", UNSET)

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

        def _parse_birthday(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        birthday = _parse_birthday(d.pop("birthday", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_client_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_id = _parse_client_id(d.pop("client_id", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_encrypt_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        encrypt_password = _parse_encrypt_password(d.pop("encrypt_password", UNSET))

        expires_in = d.pop("expiresIn", UNSET)

        _extra_data = d.pop("extraData", UNSET)
        extra_data: IdmTokensDataExtraData | Unset
        if isinstance(_extra_data, Unset):
            extra_data = UNSET
        else:
            extra_data = IdmTokensDataExtraData.from_dict(_extra_data)

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("firstName", UNSET))

        def _parse_gender(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        gender = _parse_gender(d.pop("gender", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_is_email_verified(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_email_verified = _parse_is_email_verified(d.pop("isEmailVerified", UNSET))

        def _parse_is_mobile_verified(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_mobile_verified = _parse_is_mobile_verified(d.pop("isMobileVerified", UNSET))

        def _parse_is_temporary_password(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_temporary_password = _parse_is_temporary_password(d.pop("isTemporaryPassword", UNSET))

        def _parse_last_login_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_login_ip = _parse_last_login_ip(d.pop("last_login_ip", UNSET))

        def _parse_last_login_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_login_time = _parse_last_login_time(d.pop("last_login_time", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("lastName", UNSET))

        def _parse_locale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locale = _parse_locale(d.pop("locale", UNSET))

        def _parse_login_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        login_by = _parse_login_by(d.pop("loginBy", UNSET))

        def _parse_login_count(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        login_count = _parse_login_count(d.pop("login_count", UNSET))

        _meta_data = d.pop("metaData", UNSET)
        meta_data: IdmTokensDataMetaData | Unset
        if isinstance(_meta_data, Unset):
            meta_data = UNSET
        else:
            meta_data = IdmTokensDataMetaData.from_dict(_meta_data)

        def _parse_middle_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        middle_name = _parse_middle_name(d.pop("middleName", UNSET))

        def _parse_mobile(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mobile = _parse_mobile(d.pop("mobile", UNSET))

        def _parse_nickname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nickname = _parse_nickname(d.pop("nickname", UNSET))

        def _parse_openid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        openid = _parse_openid(d.pop("openid", UNSET))

        def _parse_org_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        org_code = _parse_org_code(d.pop("org_code", UNSET))

        def _parse_partner_1_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        partner_1_id = _parse_partner_1_id(d.pop("partner1Id", UNSET))

        def _parse_partner_2_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        partner_2_id = _parse_partner_2_id(d.pop("partner2Id", UNSET))

        refresh_token = d.pop("refreshToken", UNSET)

        def _parse_register_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        register_date = _parse_register_date(d.pop("register_date", UNSET))

        def _parse_register_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        register_type = _parse_register_type(d.pop("register_type", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_street1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street1 = _parse_street1(d.pop("street1", UNSET))

        def _parse_street2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street2 = _parse_street2(d.pop("street2", UNSET))

        def _parse_street3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street3 = _parse_street3(d.pop("street3", UNSET))

        token_type = d.pop("tokenType", UNSET)

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_zip_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zip_code = _parse_zip_code(d.pop("zipCode", UNSET))

        def _parse_account_link_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_link_url = _parse_account_link_url(d.pop("accountLinkUrl", UNSET))

        def _parse_error_msg(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_msg = _parse_error_msg(d.pop("errorMsg", UNSET))

        def _parse_link_status(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        link_status = _parse_link_status(d.pop("linkStatus", UNSET))

        idm_tokens_data = cls(
            access_token=access_token,
            address=address,
            avatar=avatar,
            birthday=birthday,
            city=city,
            client_id=client_id,
            country=country,
            email=email,
            encrypt_password=encrypt_password,
            expires_in=expires_in,
            extra_data=extra_data,
            first_name=first_name,
            gender=gender,
            id=id,
            is_email_verified=is_email_verified,
            is_mobile_verified=is_mobile_verified,
            is_temporary_password=is_temporary_password,
            last_login_ip=last_login_ip,
            last_login_time=last_login_time,
            last_name=last_name,
            locale=locale,
            login_by=login_by,
            login_count=login_count,
            meta_data=meta_data,
            middle_name=middle_name,
            mobile=mobile,
            nickname=nickname,
            openid=openid,
            org_code=org_code,
            partner_1_id=partner_1_id,
            partner_2_id=partner_2_id,
            refresh_token=refresh_token,
            register_date=register_date,
            register_type=register_type,
            state=state,
            street1=street1,
            street2=street2,
            street3=street3,
            token_type=token_type,
            username=username,
            zip_code=zip_code,
            account_link_url=account_link_url,
            error_msg=error_msg,
            link_status=link_status,
        )

        idm_tokens_data.additional_properties = d
        return idm_tokens_data

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
