from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceSchemaPostOut")


@_attrs_define
class ResourceSchemaPostOut:
    """
    Attributes:
        file (str):
        resource_id (UUID):
        attributes (Any): List of attributes
        created (datetime.datetime):
        updated (datetime.datetime):
        string_attributes (list[str]):
        integer_attributes (list[str]):
        float_attributes (list[str]):
        boolean_attributes (list[str]):
        date_attributes (list[str]):
        datetime_attributes (list[str]):
        time_attributes (list[str]):
        coordinate_attributes (list[str]):
        polygon_attributes (list[str]):
        table_attributes (list[str]):
        list_object_attributes (list[str]):
        json_attributes (list[str]):
        single_select_attributes (list[str]):
        multi_select_attributes (list[str]):
        created_by (None | Unset | UUID):
        updated_by (None | Unset | UUID):
        resource_version_control (None | Unset | UUID):
        version (int | Unset):  Default: 1.
    """

    file: str
    resource_id: UUID
    attributes: Any
    created: datetime.datetime
    updated: datetime.datetime
    string_attributes: list[str]
    integer_attributes: list[str]
    float_attributes: list[str]
    boolean_attributes: list[str]
    date_attributes: list[str]
    datetime_attributes: list[str]
    time_attributes: list[str]
    coordinate_attributes: list[str]
    polygon_attributes: list[str]
    table_attributes: list[str]
    list_object_attributes: list[str]
    json_attributes: list[str]
    single_select_attributes: list[str]
    multi_select_attributes: list[str]
    created_by: None | Unset | UUID = UNSET
    updated_by: None | Unset | UUID = UNSET
    resource_version_control: None | Unset | UUID = UNSET
    version: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file

        resource_id = str(self.resource_id)

        attributes = self.attributes

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        string_attributes = self.string_attributes

        integer_attributes = self.integer_attributes

        float_attributes = self.float_attributes

        boolean_attributes = self.boolean_attributes

        date_attributes = self.date_attributes

        datetime_attributes = self.datetime_attributes

        time_attributes = self.time_attributes

        coordinate_attributes = self.coordinate_attributes

        polygon_attributes = self.polygon_attributes

        table_attributes = self.table_attributes

        list_object_attributes = self.list_object_attributes

        json_attributes = self.json_attributes

        single_select_attributes = self.single_select_attributes

        multi_select_attributes = self.multi_select_attributes

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

        resource_version_control: None | str | Unset
        if isinstance(self.resource_version_control, Unset):
            resource_version_control = UNSET
        elif isinstance(self.resource_version_control, UUID):
            resource_version_control = str(self.resource_version_control)
        else:
            resource_version_control = self.resource_version_control

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "resource_id": resource_id,
                "attributes": attributes,
                "created": created,
                "updated": updated,
                "string_attributes": string_attributes,
                "integer_attributes": integer_attributes,
                "float_attributes": float_attributes,
                "boolean_attributes": boolean_attributes,
                "date_attributes": date_attributes,
                "datetime_attributes": datetime_attributes,
                "time_attributes": time_attributes,
                "coordinate_attributes": coordinate_attributes,
                "polygon_attributes": polygon_attributes,
                "table_attributes": table_attributes,
                "list_object_attributes": list_object_attributes,
                "json_attributes": json_attributes,
                "single_select_attributes": single_select_attributes,
                "multi_select_attributes": multi_select_attributes,
            }
        )
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if resource_version_control is not UNSET:
            field_dict["resource_version_control"] = resource_version_control
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = d.pop("file")

        resource_id = UUID(d.pop("resource_id"))

        attributes = d.pop("attributes")

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        string_attributes = cast(list[str], d.pop("string_attributes"))

        integer_attributes = cast(list[str], d.pop("integer_attributes"))

        float_attributes = cast(list[str], d.pop("float_attributes"))

        boolean_attributes = cast(list[str], d.pop("boolean_attributes"))

        date_attributes = cast(list[str], d.pop("date_attributes"))

        datetime_attributes = cast(list[str], d.pop("datetime_attributes"))

        time_attributes = cast(list[str], d.pop("time_attributes"))

        coordinate_attributes = cast(list[str], d.pop("coordinate_attributes"))

        polygon_attributes = cast(list[str], d.pop("polygon_attributes"))

        table_attributes = cast(list[str], d.pop("table_attributes"))

        list_object_attributes = cast(list[str], d.pop("list_object_attributes"))

        json_attributes = cast(list[str], d.pop("json_attributes"))

        single_select_attributes = cast(list[str], d.pop("single_select_attributes"))

        multi_select_attributes = cast(list[str], d.pop("multi_select_attributes"))

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

        def _parse_resource_version_control(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resource_version_control_type_0 = UUID(data)

                return resource_version_control_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        resource_version_control = _parse_resource_version_control(d.pop("resource_version_control", UNSET))

        version = d.pop("version", UNSET)

        resource_schema_post_out = cls(
            file=file,
            resource_id=resource_id,
            attributes=attributes,
            created=created,
            updated=updated,
            string_attributes=string_attributes,
            integer_attributes=integer_attributes,
            float_attributes=float_attributes,
            boolean_attributes=boolean_attributes,
            date_attributes=date_attributes,
            datetime_attributes=datetime_attributes,
            time_attributes=time_attributes,
            coordinate_attributes=coordinate_attributes,
            polygon_attributes=polygon_attributes,
            table_attributes=table_attributes,
            list_object_attributes=list_object_attributes,
            json_attributes=json_attributes,
            single_select_attributes=single_select_attributes,
            multi_select_attributes=multi_select_attributes,
            created_by=created_by,
            updated_by=updated_by,
            resource_version_control=resource_version_control,
            version=version,
        )

        resource_schema_post_out.additional_properties = d
        return resource_schema_post_out

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
