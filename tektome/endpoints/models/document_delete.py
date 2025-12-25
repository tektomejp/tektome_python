from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentDelete")


@_attrs_define
class DocumentDelete:
    """
    Attributes:
        file_id (UUID):
        project_id (str):
        data_space_id (None | str | Unset):
    """

    file_id: UUID
    project_id: str
    data_space_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = str(self.file_id)

        project_id = self.project_id

        data_space_id: None | str | Unset
        if isinstance(self.data_space_id, Unset):
            data_space_id = UNSET
        else:
            data_space_id = self.data_space_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_id": file_id,
                "project_id": project_id,
            }
        )
        if data_space_id is not UNSET:
            field_dict["data_space_id"] = data_space_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = UUID(d.pop("file_id"))

        project_id = d.pop("project_id")

        def _parse_data_space_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_space_id = _parse_data_space_id(d.pop("data_space_id", UNSET))

        document_delete = cls(
            file_id=file_id,
            project_id=project_id,
            data_space_id=data_space_id,
        )

        document_delete.additional_properties = d
        return document_delete

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
