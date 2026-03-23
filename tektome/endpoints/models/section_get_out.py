from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.section_get_out_pages_paragraphs_paths_type_0 import SectionGetOutPagesParagraphsPathsType0
    from ..models.section_get_out_pages_tables_paths_type_0 import SectionGetOutPagesTablesPathsType0


T = TypeVar("T", bound="SectionGetOut")


@_attrs_define
class SectionGetOut:
    """
    Attributes:
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
        resources (list[str]):
        pages (list[str]):
        chunk_groups (list[str]):
        raw_texts (list[str]):
        bim_objects (list[str]):
        source_string_attributes (list[str]):
        source_integer_attributes (list[str]):
        source_float_attributes (list[str]):
        source_boolean_attributes (list[str]):
        source_date_attributes (list[str]):
        source_datetime_attributes (list[str]):
        source_time_attributes (list[str]):
        source_coordinate_attributes (list[str]):
        source_polygon_attributes (list[str]):
        source_table_attributes (list[str]):
        id (None | Unset | UUID):
        created_by (None | Unset | UUID):
        updated_by (None | Unset | UUID):
        project (None | Unset | UUID):
        pages_paragraphs_paths (None | SectionGetOutPagesParagraphsPathsType0 | Unset):
        pages_tables_paths (None | SectionGetOutPagesTablesPathsType0 | Unset):
    """

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
    resources: list[str]
    pages: list[str]
    chunk_groups: list[str]
    raw_texts: list[str]
    bim_objects: list[str]
    source_string_attributes: list[str]
    source_integer_attributes: list[str]
    source_float_attributes: list[str]
    source_boolean_attributes: list[str]
    source_date_attributes: list[str]
    source_datetime_attributes: list[str]
    source_time_attributes: list[str]
    source_coordinate_attributes: list[str]
    source_polygon_attributes: list[str]
    source_table_attributes: list[str]
    id: None | Unset | UUID = UNSET
    created_by: None | Unset | UUID = UNSET
    updated_by: None | Unset | UUID = UNSET
    project: None | Unset | UUID = UNSET
    pages_paragraphs_paths: None | SectionGetOutPagesParagraphsPathsType0 | Unset = UNSET
    pages_tables_paths: None | SectionGetOutPagesTablesPathsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.section_get_out_pages_paragraphs_paths_type_0 import SectionGetOutPagesParagraphsPathsType0
        from ..models.section_get_out_pages_tables_paths_type_0 import SectionGetOutPagesTablesPathsType0

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

        resources = self.resources

        pages = self.pages

        chunk_groups = self.chunk_groups

        raw_texts = self.raw_texts

        bim_objects = self.bim_objects

        source_string_attributes = self.source_string_attributes

        source_integer_attributes = self.source_integer_attributes

        source_float_attributes = self.source_float_attributes

        source_boolean_attributes = self.source_boolean_attributes

        source_date_attributes = self.source_date_attributes

        source_datetime_attributes = self.source_datetime_attributes

        source_time_attributes = self.source_time_attributes

        source_coordinate_attributes = self.source_coordinate_attributes

        source_polygon_attributes = self.source_polygon_attributes

        source_table_attributes = self.source_table_attributes

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

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

        pages_paragraphs_paths: dict[str, Any] | None | Unset
        if isinstance(self.pages_paragraphs_paths, Unset):
            pages_paragraphs_paths = UNSET
        elif isinstance(self.pages_paragraphs_paths, SectionGetOutPagesParagraphsPathsType0):
            pages_paragraphs_paths = self.pages_paragraphs_paths.to_dict()
        else:
            pages_paragraphs_paths = self.pages_paragraphs_paths

        pages_tables_paths: dict[str, Any] | None | Unset
        if isinstance(self.pages_tables_paths, Unset):
            pages_tables_paths = UNSET
        elif isinstance(self.pages_tables_paths, SectionGetOutPagesTablesPathsType0):
            pages_tables_paths = self.pages_tables_paths.to_dict()
        else:
            pages_tables_paths = self.pages_tables_paths

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
                "resources": resources,
                "pages": pages,
                "chunk_groups": chunk_groups,
                "raw_texts": raw_texts,
                "bim_objects": bim_objects,
                "source_string_attributes": source_string_attributes,
                "source_integer_attributes": source_integer_attributes,
                "source_float_attributes": source_float_attributes,
                "source_boolean_attributes": source_boolean_attributes,
                "source_date_attributes": source_date_attributes,
                "source_datetime_attributes": source_datetime_attributes,
                "source_time_attributes": source_time_attributes,
                "source_coordinate_attributes": source_coordinate_attributes,
                "source_polygon_attributes": source_polygon_attributes,
                "source_table_attributes": source_table_attributes,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if project is not UNSET:
            field_dict["project"] = project
        if pages_paragraphs_paths is not UNSET:
            field_dict["pages_paragraphs_paths"] = pages_paragraphs_paths
        if pages_tables_paths is not UNSET:
            field_dict["pages_tables_paths"] = pages_tables_paths

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.section_get_out_pages_paragraphs_paths_type_0 import SectionGetOutPagesParagraphsPathsType0
        from ..models.section_get_out_pages_tables_paths_type_0 import SectionGetOutPagesTablesPathsType0

        d = dict(src_dict)
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

        resources = cast(list[str], d.pop("resources"))

        pages = cast(list[str], d.pop("pages"))

        chunk_groups = cast(list[str], d.pop("chunk_groups"))

        raw_texts = cast(list[str], d.pop("raw_texts"))

        bim_objects = cast(list[str], d.pop("bim_objects"))

        source_string_attributes = cast(list[str], d.pop("source_string_attributes"))

        source_integer_attributes = cast(list[str], d.pop("source_integer_attributes"))

        source_float_attributes = cast(list[str], d.pop("source_float_attributes"))

        source_boolean_attributes = cast(list[str], d.pop("source_boolean_attributes"))

        source_date_attributes = cast(list[str], d.pop("source_date_attributes"))

        source_datetime_attributes = cast(list[str], d.pop("source_datetime_attributes"))

        source_time_attributes = cast(list[str], d.pop("source_time_attributes"))

        source_coordinate_attributes = cast(list[str], d.pop("source_coordinate_attributes"))

        source_polygon_attributes = cast(list[str], d.pop("source_polygon_attributes"))

        source_table_attributes = cast(list[str], d.pop("source_table_attributes"))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

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

        def _parse_pages_paragraphs_paths(data: object) -> None | SectionGetOutPagesParagraphsPathsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pages_paragraphs_paths_type_0 = SectionGetOutPagesParagraphsPathsType0.from_dict(data)

                return pages_paragraphs_paths_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SectionGetOutPagesParagraphsPathsType0 | Unset, data)

        pages_paragraphs_paths = _parse_pages_paragraphs_paths(d.pop("pages_paragraphs_paths", UNSET))

        def _parse_pages_tables_paths(data: object) -> None | SectionGetOutPagesTablesPathsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pages_tables_paths_type_0 = SectionGetOutPagesTablesPathsType0.from_dict(data)

                return pages_tables_paths_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SectionGetOutPagesTablesPathsType0 | Unset, data)

        pages_tables_paths = _parse_pages_tables_paths(d.pop("pages_tables_paths", UNSET))

        section_get_out = cls(
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
            resources=resources,
            pages=pages,
            chunk_groups=chunk_groups,
            raw_texts=raw_texts,
            bim_objects=bim_objects,
            source_string_attributes=source_string_attributes,
            source_integer_attributes=source_integer_attributes,
            source_float_attributes=source_float_attributes,
            source_boolean_attributes=source_boolean_attributes,
            source_date_attributes=source_date_attributes,
            source_datetime_attributes=source_datetime_attributes,
            source_time_attributes=source_time_attributes,
            source_coordinate_attributes=source_coordinate_attributes,
            source_polygon_attributes=source_polygon_attributes,
            source_table_attributes=source_table_attributes,
            id=id,
            created_by=created_by,
            updated_by=updated_by,
            project=project,
            pages_paragraphs_paths=pages_paragraphs_paths,
            pages_tables_paths=pages_tables_paths,
        )

        section_get_out.additional_properties = d
        return section_get_out

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
