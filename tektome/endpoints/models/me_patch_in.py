from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MePatchIn")


@_attrs_define
class MePatchIn:
    """
    Attributes:
        username (str | Unset):
        language (str | Unset): Language code, e.g., 'en' for English
        tos_accepted_at (bool | Unset): Terms of Service accepted
        first_name (str | Unset):  Default: ''.
        last_name (str | Unset):  Default: ''.
        avatar_url (None | str | Unset):
    """

    username: str | Unset = UNSET
    language: str | Unset = UNSET
    tos_accepted_at: bool | Unset = UNSET
    first_name: str | Unset = ""
    last_name: str | Unset = ""
    avatar_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        language = self.language

        tos_accepted_at = self.tos_accepted_at

        first_name = self.first_name

        last_name = self.last_name

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if language is not UNSET:
            field_dict["language"] = language
        if tos_accepted_at is not UNSET:
            field_dict["tos_accepted_at"] = tos_accepted_at
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username", UNSET)

        language = d.pop("language", UNSET)

        tos_accepted_at = d.pop("tos_accepted_at", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url", UNSET))

        me_patch_in = cls(
            username=username,
            language=language,
            tos_accepted_at=tos_accepted_at,
            first_name=first_name,
            last_name=last_name,
            avatar_url=avatar_url,
        )

        me_patch_in.additional_properties = d
        return me_patch_in

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
