from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentProjectUpdate")


@_attrs_define
class DocumentProjectUpdate:
    """
    Attributes:
        file_id (UUID):
        old_project_id (str):
        new_project_id (str):
        data_space_id (None | str | Unset):
        keep_attributes (bool | Unset):  Default: False.
    """

    file_id: UUID
    old_project_id: str
    new_project_id: str
    data_space_id: None | str | Unset = UNSET
    keep_attributes: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = str(self.file_id)

        old_project_id = self.old_project_id

        new_project_id = self.new_project_id

        data_space_id: None | str | Unset
        if isinstance(self.data_space_id, Unset):
            data_space_id = UNSET
        else:
            data_space_id = self.data_space_id

        keep_attributes = self.keep_attributes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_id": file_id,
                "old_project_id": old_project_id,
                "new_project_id": new_project_id,
            }
        )
        if data_space_id is not UNSET:
            field_dict["data_space_id"] = data_space_id
        if keep_attributes is not UNSET:
            field_dict["keep_attributes"] = keep_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = UUID(d.pop("file_id"))

        old_project_id = d.pop("old_project_id")

        new_project_id = d.pop("new_project_id")

        def _parse_data_space_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_space_id = _parse_data_space_id(d.pop("data_space_id", UNSET))

        keep_attributes = d.pop("keep_attributes", UNSET)

        document_project_update = cls(
            file_id=file_id,
            old_project_id=old_project_id,
            new_project_id=new_project_id,
            data_space_id=data_space_id,
            keep_attributes=keep_attributes,
        )

        document_project_update.additional_properties = d
        return document_project_update

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
