from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.login_providers import LoginProviders

T = TypeVar("T", bound="LoginPostIn")


@_attrs_define
class LoginPostIn:
    """
    Attributes:
        email (str): Email of the user
        uid (str): provider's unique id ex. sid
        provider (LoginProviders):
    """

    email: str
    uid: str
    provider: LoginProviders
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        uid = self.uid

        provider = self.provider.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "uid": uid,
                "provider": provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        uid = d.pop("uid")

        provider = LoginProviders(d.pop("provider"))

        login_post_in = cls(
            email=email,
            uid=uid,
            provider=provider,
        )

        login_post_in.additional_properties = d
        return login_post_in

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
