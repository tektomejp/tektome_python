from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MeGetGitbookTokenOut")


@_attrs_define
class MeGetGitbookTokenOut:
    """
    Attributes:
        gitbook_url (str):
        gitbook_token (str):
    """

    gitbook_url: str
    gitbook_token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gitbook_url = self.gitbook_url

        gitbook_token = self.gitbook_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gitbook_url": gitbook_url,
                "gitbook_token": gitbook_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gitbook_url = d.pop("gitbook_url")

        gitbook_token = d.pop("gitbook_token")

        me_get_gitbook_token_out = cls(
            gitbook_url=gitbook_url,
            gitbook_token=gitbook_token,
        )

        me_get_gitbook_token_out.additional_properties = d
        return me_get_gitbook_token_out

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
