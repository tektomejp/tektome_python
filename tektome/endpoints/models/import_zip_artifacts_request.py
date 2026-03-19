from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.duplicate_strategy import DuplicateStrategy
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportZipArtifactsRequest")


@_attrs_define
class ImportZipArtifactsRequest:
    """
    Attributes:
        url (str): URL to a .zip file to download and extract
        base_path (str | Unset): Prefix prepended to all extracted file paths. Empty string means files are placed at
            the root. Default: ''.
        on_duplicate (DuplicateStrategy | Unset): Controls how duplicate artifact paths are handled during import.
            Default: DuplicateStrategy.FORBID.
        strip_common_root (bool | Unset): If true, detect and strip a single common root folder (e.g. GitHub archives
            wrap files in a repo-tag/ folder). Default: True.
    """

    url: str
    base_path: str | Unset = ""
    on_duplicate: DuplicateStrategy | Unset = DuplicateStrategy.FORBID
    strip_common_root: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        base_path = self.base_path

        on_duplicate: str | Unset = UNSET
        if not isinstance(self.on_duplicate, Unset):
            on_duplicate = self.on_duplicate.value

        strip_common_root = self.strip_common_root

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if base_path is not UNSET:
            field_dict["base_path"] = base_path
        if on_duplicate is not UNSET:
            field_dict["on_duplicate"] = on_duplicate
        if strip_common_root is not UNSET:
            field_dict["strip_common_root"] = strip_common_root

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        base_path = d.pop("base_path", UNSET)

        _on_duplicate = d.pop("on_duplicate", UNSET)
        on_duplicate: DuplicateStrategy | Unset
        if isinstance(_on_duplicate, Unset):
            on_duplicate = UNSET
        else:
            on_duplicate = DuplicateStrategy(_on_duplicate)

        strip_common_root = d.pop("strip_common_root", UNSET)

        import_zip_artifacts_request = cls(
            url=url,
            base_path=base_path,
            on_duplicate=on_duplicate,
            strip_common_root=strip_common_root,
        )

        import_zip_artifacts_request.additional_properties = d
        return import_zip_artifacts_request

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
