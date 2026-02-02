from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnvironmentVariableResponse")


@_attrs_define
class EnvironmentVariableResponse:
    """
    Attributes:
        id (UUID):
        value (str):
        created (datetime.datetime):
        updated (datetime.datetime):
        organization (UUID):
        key (str):
        created_by (None | Unset | UUID):
        updated_by (None | Unset | UUID):
        project (None | Unset | UUID):
        dataspace (None | Unset | UUID):
        description (None | str | Unset):  Default: ''.
        is_secret (bool | Unset):  Default: False.
    """

    id: UUID
    value: str
    created: datetime.datetime
    updated: datetime.datetime
    organization: UUID
    key: str
    created_by: None | Unset | UUID = UNSET
    updated_by: None | Unset | UUID = UNSET
    project: None | Unset | UUID = UNSET
    dataspace: None | Unset | UUID = UNSET
    description: None | str | Unset = ""
    is_secret: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        value = self.value

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        organization = str(self.organization)

        key = self.key

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        elif isinstance(self.updated_by, UUID):
            updated_by = str(self.updated_by)
        else:
            updated_by = self.updated_by

        project: None | str | Unset
        if isinstance(self.project, Unset):
            project = UNSET
        elif isinstance(self.project, UUID):
            project = str(self.project)
        else:
            project = self.project

        dataspace: None | str | Unset
        if isinstance(self.dataspace, Unset):
            dataspace = UNSET
        elif isinstance(self.dataspace, UUID):
            dataspace = str(self.dataspace)
        else:
            dataspace = self.dataspace

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_secret = self.is_secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "value": value,
                "created": created,
                "updated": updated,
                "organization": organization,
                "key": key,
            }
        )
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if project is not UNSET:
            field_dict["project"] = project
        if dataspace is not UNSET:
            field_dict["dataspace"] = dataspace
        if description is not UNSET:
            field_dict["description"] = description
        if is_secret is not UNSET:
            field_dict["is_secret"] = is_secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        value = d.pop("value")

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        organization = UUID(d.pop("organization"))

        key = d.pop("key")

        def _parse_created_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_type_0 = UUID(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_updated_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_by_type_0 = UUID(data)

                return updated_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        def _parse_project(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                project_type_0 = UUID(data)

                return project_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        project = _parse_project(d.pop("project", UNSET))

        def _parse_dataspace(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dataspace_type_0 = UUID(data)

                return dataspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        dataspace = _parse_dataspace(d.pop("dataspace", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        is_secret = d.pop("is_secret", UNSET)

        environment_variable_response = cls(
            id=id,
            value=value,
            created=created,
            updated=updated,
            organization=organization,
            key=key,
            created_by=created_by,
            updated_by=updated_by,
            project=project,
            dataspace=dataspace,
            description=description,
            is_secret=is_secret,
        )

        environment_variable_response.additional_properties = d
        return environment_variable_response

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
