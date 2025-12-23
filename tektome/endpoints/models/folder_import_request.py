from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.import_folder import ImportFolder


T = TypeVar("T", bound="FolderImportRequest")


@_attrs_define
class FolderImportRequest:
    """Request schema for folder import operation.

    Attributes:
        folders (list[ImportFolder]): List of folders to import
    """

    folders: list[ImportFolder]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        folders = []
        for folders_item_data in self.folders:
            folders_item = folders_item_data.to_dict()
            folders.append(folders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "folders": folders,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_folder import ImportFolder

        d = dict(src_dict)
        folders = []
        _folders = d.pop("folders")
        for folders_item_data in _folders:
            folders_item = ImportFolder.from_dict(folders_item_data)

            folders.append(folders_item)

        folder_import_request = cls(
            folders=folders,
        )

        folder_import_request.additional_properties = d
        return folder_import_request

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
