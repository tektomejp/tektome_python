from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileUploadCandidatePayload")


@_attrs_define
class FileUploadCandidatePayload:
    """
    Attributes:
        project_id (UUID):
        resource_url (None | str | Unset):
        resource_name (None | str | Unset):
        extension (None | str | Unset):
    """

    project_id: UUID
    resource_url: None | str | Unset = UNSET
    resource_name: None | str | Unset = UNSET
    extension: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = str(self.project_id)

        resource_url: None | str | Unset
        if isinstance(self.resource_url, Unset):
            resource_url = UNSET
        else:
            resource_url = self.resource_url

        resource_name: None | str | Unset
        if isinstance(self.resource_name, Unset):
            resource_name = UNSET
        else:
            resource_name = self.resource_name

        extension: None | str | Unset
        if isinstance(self.extension, Unset):
            extension = UNSET
        else:
            extension = self.extension

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
            }
        )
        if resource_url is not UNSET:
            field_dict["resource_url"] = resource_url
        if resource_name is not UNSET:
            field_dict["resource_name"] = resource_name
        if extension is not UNSET:
            field_dict["extension"] = extension

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = UUID(d.pop("project_id"))

        def _parse_resource_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_url = _parse_resource_url(d.pop("resource_url", UNSET))

        def _parse_resource_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_name = _parse_resource_name(d.pop("resource_name", UNSET))

        def _parse_extension(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extension = _parse_extension(d.pop("extension", UNSET))

        file_upload_candidate_payload = cls(
            project_id=project_id,
            resource_url=resource_url,
            resource_name=resource_name,
            extension=extension,
        )

        file_upload_candidate_payload.additional_properties = d
        return file_upload_candidate_payload

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
