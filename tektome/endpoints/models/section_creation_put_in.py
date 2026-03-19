from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.section_creation_put_in_bim_project_object_ids import SectionCreationPutInBimProjectObjectIds
    from ..models.section_paragraph_path import SectionParagraphPath
    from ..models.section_table_path import SectionTablePath


T = TypeVar("T", bound="SectionCreationPutIn")


@_attrs_define
class SectionCreationPutIn:
    """
    Attributes:
        project_id (UUID): Project's ID to bind a section
        resource_ids (list[UUID] | Unset): List of resource IDs to include in the section
        page_ids (list[UUID] | Unset): List of page IDs to include in the section
        pages_paragraphs_paths (list[SectionParagraphPath] | Unset): Path to access paragraphs in pages
        pages_tables_paths (list[SectionTablePath] | Unset): Path to access tables in pages
        chunk_group_ids (list[UUID] | Unset): List of chunk group IDs to include in the section
        raw_text_ids (list[UUID] | Unset): List of raw text IDs to include in the section
        bim_project_object_ids (SectionCreationPutInBimProjectObjectIds | Unset): Mapping of BIM Project IDs to the list
            of BIM Object IDs from that project to be include in the section
        source_string_attribute_ids (list[UUID] | Unset): List of string attribute IDs to include in the section
        source_integer_attribute_ids (list[UUID] | Unset): List of integer attribute IDs to include in the section
        source_float_attribute_ids (list[UUID] | Unset): List of float attribute IDs to include in the section
        source_boolean_attribute_ids (list[UUID] | Unset): List of boolean attribute IDs to include in the section
        source_date_attribute_ids (list[UUID] | Unset): List of date attribute IDs to include in the section
        source_datetime_attribute_ids (list[UUID] | Unset): List of datetime attribute IDs to include in the section
        source_time_attribute_ids (list[UUID] | Unset): List of time attribute IDs to include in the section
        source_coordinate_attribute_ids (list[UUID] | Unset): List of coordinate attribute IDs to include in the section
        source_polygon_attribute_ids (list[UUID] | Unset): List of polygon attribute IDs to include in the section
        source_table_attribute_ids (list[UUID] | Unset): List of table attribute IDs to include in the section
    """

    project_id: UUID
    resource_ids: list[UUID] | Unset = UNSET
    page_ids: list[UUID] | Unset = UNSET
    pages_paragraphs_paths: list[SectionParagraphPath] | Unset = UNSET
    pages_tables_paths: list[SectionTablePath] | Unset = UNSET
    chunk_group_ids: list[UUID] | Unset = UNSET
    raw_text_ids: list[UUID] | Unset = UNSET
    bim_project_object_ids: SectionCreationPutInBimProjectObjectIds | Unset = UNSET
    source_string_attribute_ids: list[UUID] | Unset = UNSET
    source_integer_attribute_ids: list[UUID] | Unset = UNSET
    source_float_attribute_ids: list[UUID] | Unset = UNSET
    source_boolean_attribute_ids: list[UUID] | Unset = UNSET
    source_date_attribute_ids: list[UUID] | Unset = UNSET
    source_datetime_attribute_ids: list[UUID] | Unset = UNSET
    source_time_attribute_ids: list[UUID] | Unset = UNSET
    source_coordinate_attribute_ids: list[UUID] | Unset = UNSET
    source_polygon_attribute_ids: list[UUID] | Unset = UNSET
    source_table_attribute_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = str(self.project_id)

        resource_ids: list[str] | Unset = UNSET
        if not isinstance(self.resource_ids, Unset):
            resource_ids = []
            for resource_ids_item_data in self.resource_ids:
                resource_ids_item = str(resource_ids_item_data)
                resource_ids.append(resource_ids_item)

        page_ids: list[str] | Unset = UNSET
        if not isinstance(self.page_ids, Unset):
            page_ids = []
            for page_ids_item_data in self.page_ids:
                page_ids_item = str(page_ids_item_data)
                page_ids.append(page_ids_item)

        pages_paragraphs_paths: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pages_paragraphs_paths, Unset):
            pages_paragraphs_paths = []
            for pages_paragraphs_paths_item_data in self.pages_paragraphs_paths:
                pages_paragraphs_paths_item = pages_paragraphs_paths_item_data.to_dict()
                pages_paragraphs_paths.append(pages_paragraphs_paths_item)

        pages_tables_paths: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pages_tables_paths, Unset):
            pages_tables_paths = []
            for pages_tables_paths_item_data in self.pages_tables_paths:
                pages_tables_paths_item = pages_tables_paths_item_data.to_dict()
                pages_tables_paths.append(pages_tables_paths_item)

        chunk_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.chunk_group_ids, Unset):
            chunk_group_ids = []
            for chunk_group_ids_item_data in self.chunk_group_ids:
                chunk_group_ids_item = str(chunk_group_ids_item_data)
                chunk_group_ids.append(chunk_group_ids_item)

        raw_text_ids: list[str] | Unset = UNSET
        if not isinstance(self.raw_text_ids, Unset):
            raw_text_ids = []
            for raw_text_ids_item_data in self.raw_text_ids:
                raw_text_ids_item = str(raw_text_ids_item_data)
                raw_text_ids.append(raw_text_ids_item)

        bim_project_object_ids: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bim_project_object_ids, Unset):
            bim_project_object_ids = self.bim_project_object_ids.to_dict()

        source_string_attribute_ids: list[str] | Unset = UNSET
        if not isinstance(self.source_string_attribute_ids, Unset):
            source_string_attribute_ids = []
            for source_string_attribute_ids_item_data in self.source_string_attribute_ids:
                source_string_attribute_ids_item = str(source_string_attribute_ids_item_data)
                source_string_attribute_ids.append(source_string_attribute_ids_item)

        source_integer_attribute_ids: list[str] | Unset = UNSET
        if not isinstance(self.source_integer_attribute_ids, Unset):
            source_integer_attribute_ids = []
            for source_integer_attribute_ids_item_data in self.source_integer_attribute_ids:
                source_integer_attribute_ids_item = str(source_integer_attribute_ids_item_data)
                source_integer_attribute_ids.append(source_integer_attribute_ids_item)

        source_float_attribute_ids: list[str] | Unset = UNSET
        if not isinstance(self.source_float_attribute_ids, Unset):
            source_float_attribute_ids = []
            for source_float_attribute_ids_item_data in self.source_float_attribute_ids:
                source_float_attribute_ids_item = str(source_float_attribute_ids_item_data)
                source_float_attribute_ids.append(source_float_attribute_ids_item)

        source_boolean_attribute_ids: list[str] | Unset = UNSET
        if not isinstance(self.source_boolean_attribute_ids, Unset):
            source_boolean_attribute_ids = []
            for source_boolean_attribute_ids_item_data in self.source_boolean_attribute_ids:
                source_boolean_attribute_ids_item = str(source_boolean_attribute_ids_item_data)
                source_boolean_attribute_ids.append(source_boolean_attribute_ids_item)

        source_date_attribute_ids: list[str] | Unset = UNSET
        if not isinstance(self.source_date_attribute_ids, Unset):
            source_date_attribute_ids = []
            for source_date_attribute_ids_item_data in self.source_date_attribute_ids:
                source_date_attribute_ids_item = str(source_date_attribute_ids_item_data)
                source_date_attribute_ids.append(source_date_attribute_ids_item)

        source_datetime_attribute_ids: list[str] | Unset = UNSET
        if not isinstance(self.source_datetime_attribute_ids, Unset):
            source_datetime_attribute_ids = []
            for source_datetime_attribute_ids_item_data in self.source_datetime_attribute_ids:
                source_datetime_attribute_ids_item = str(source_datetime_attribute_ids_item_data)
                source_datetime_attribute_ids.append(source_datetime_attribute_ids_item)

        source_time_attribute_ids: list[str] | Unset = UNSET
        if not isinstance(self.source_time_attribute_ids, Unset):
            source_time_attribute_ids = []
            for source_time_attribute_ids_item_data in self.source_time_attribute_ids:
                source_time_attribute_ids_item = str(source_time_attribute_ids_item_data)
                source_time_attribute_ids.append(source_time_attribute_ids_item)

        source_coordinate_attribute_ids: list[str] | Unset = UNSET
        if not isinstance(self.source_coordinate_attribute_ids, Unset):
            source_coordinate_attribute_ids = []
            for source_coordinate_attribute_ids_item_data in self.source_coordinate_attribute_ids:
                source_coordinate_attribute_ids_item = str(source_coordinate_attribute_ids_item_data)
                source_coordinate_attribute_ids.append(source_coordinate_attribute_ids_item)

        source_polygon_attribute_ids: list[str] | Unset = UNSET
        if not isinstance(self.source_polygon_attribute_ids, Unset):
            source_polygon_attribute_ids = []
            for source_polygon_attribute_ids_item_data in self.source_polygon_attribute_ids:
                source_polygon_attribute_ids_item = str(source_polygon_attribute_ids_item_data)
                source_polygon_attribute_ids.append(source_polygon_attribute_ids_item)

        source_table_attribute_ids: list[str] | Unset = UNSET
        if not isinstance(self.source_table_attribute_ids, Unset):
            source_table_attribute_ids = []
            for source_table_attribute_ids_item_data in self.source_table_attribute_ids:
                source_table_attribute_ids_item = str(source_table_attribute_ids_item_data)
                source_table_attribute_ids.append(source_table_attribute_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
            }
        )
        if resource_ids is not UNSET:
            field_dict["resource_ids"] = resource_ids
        if page_ids is not UNSET:
            field_dict["page_ids"] = page_ids
        if pages_paragraphs_paths is not UNSET:
            field_dict["pages_paragraphs_paths"] = pages_paragraphs_paths
        if pages_tables_paths is not UNSET:
            field_dict["pages_tables_paths"] = pages_tables_paths
        if chunk_group_ids is not UNSET:
            field_dict["chunk_group_ids"] = chunk_group_ids
        if raw_text_ids is not UNSET:
            field_dict["raw_text_ids"] = raw_text_ids
        if bim_project_object_ids is not UNSET:
            field_dict["bim_project_object_ids"] = bim_project_object_ids
        if source_string_attribute_ids is not UNSET:
            field_dict["source_string_attribute_ids"] = source_string_attribute_ids
        if source_integer_attribute_ids is not UNSET:
            field_dict["source_integer_attribute_ids"] = source_integer_attribute_ids
        if source_float_attribute_ids is not UNSET:
            field_dict["source_float_attribute_ids"] = source_float_attribute_ids
        if source_boolean_attribute_ids is not UNSET:
            field_dict["source_boolean_attribute_ids"] = source_boolean_attribute_ids
        if source_date_attribute_ids is not UNSET:
            field_dict["source_date_attribute_ids"] = source_date_attribute_ids
        if source_datetime_attribute_ids is not UNSET:
            field_dict["source_datetime_attribute_ids"] = source_datetime_attribute_ids
        if source_time_attribute_ids is not UNSET:
            field_dict["source_time_attribute_ids"] = source_time_attribute_ids
        if source_coordinate_attribute_ids is not UNSET:
            field_dict["source_coordinate_attribute_ids"] = source_coordinate_attribute_ids
        if source_polygon_attribute_ids is not UNSET:
            field_dict["source_polygon_attribute_ids"] = source_polygon_attribute_ids
        if source_table_attribute_ids is not UNSET:
            field_dict["source_table_attribute_ids"] = source_table_attribute_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.section_creation_put_in_bim_project_object_ids import SectionCreationPutInBimProjectObjectIds
        from ..models.section_paragraph_path import SectionParagraphPath
        from ..models.section_table_path import SectionTablePath

        d = dict(src_dict)
        project_id = UUID(d.pop("project_id"))

        _resource_ids = d.pop("resource_ids", UNSET)
        resource_ids: list[UUID] | Unset = UNSET
        if _resource_ids is not UNSET:
            resource_ids = []
            for resource_ids_item_data in _resource_ids:
                resource_ids_item = UUID(resource_ids_item_data)

                resource_ids.append(resource_ids_item)

        _page_ids = d.pop("page_ids", UNSET)
        page_ids: list[UUID] | Unset = UNSET
        if _page_ids is not UNSET:
            page_ids = []
            for page_ids_item_data in _page_ids:
                page_ids_item = UUID(page_ids_item_data)

                page_ids.append(page_ids_item)

        _pages_paragraphs_paths = d.pop("pages_paragraphs_paths", UNSET)
        pages_paragraphs_paths: list[SectionParagraphPath] | Unset = UNSET
        if _pages_paragraphs_paths is not UNSET:
            pages_paragraphs_paths = []
            for pages_paragraphs_paths_item_data in _pages_paragraphs_paths:
                pages_paragraphs_paths_item = SectionParagraphPath.from_dict(pages_paragraphs_paths_item_data)

                pages_paragraphs_paths.append(pages_paragraphs_paths_item)

        _pages_tables_paths = d.pop("pages_tables_paths", UNSET)
        pages_tables_paths: list[SectionTablePath] | Unset = UNSET
        if _pages_tables_paths is not UNSET:
            pages_tables_paths = []
            for pages_tables_paths_item_data in _pages_tables_paths:
                pages_tables_paths_item = SectionTablePath.from_dict(pages_tables_paths_item_data)

                pages_tables_paths.append(pages_tables_paths_item)

        _chunk_group_ids = d.pop("chunk_group_ids", UNSET)
        chunk_group_ids: list[UUID] | Unset = UNSET
        if _chunk_group_ids is not UNSET:
            chunk_group_ids = []
            for chunk_group_ids_item_data in _chunk_group_ids:
                chunk_group_ids_item = UUID(chunk_group_ids_item_data)

                chunk_group_ids.append(chunk_group_ids_item)

        _raw_text_ids = d.pop("raw_text_ids", UNSET)
        raw_text_ids: list[UUID] | Unset = UNSET
        if _raw_text_ids is not UNSET:
            raw_text_ids = []
            for raw_text_ids_item_data in _raw_text_ids:
                raw_text_ids_item = UUID(raw_text_ids_item_data)

                raw_text_ids.append(raw_text_ids_item)

        _bim_project_object_ids = d.pop("bim_project_object_ids", UNSET)
        bim_project_object_ids: SectionCreationPutInBimProjectObjectIds | Unset
        if isinstance(_bim_project_object_ids, Unset):
            bim_project_object_ids = UNSET
        else:
            bim_project_object_ids = SectionCreationPutInBimProjectObjectIds.from_dict(_bim_project_object_ids)

        _source_string_attribute_ids = d.pop("source_string_attribute_ids", UNSET)
        source_string_attribute_ids: list[UUID] | Unset = UNSET
        if _source_string_attribute_ids is not UNSET:
            source_string_attribute_ids = []
            for source_string_attribute_ids_item_data in _source_string_attribute_ids:
                source_string_attribute_ids_item = UUID(source_string_attribute_ids_item_data)

                source_string_attribute_ids.append(source_string_attribute_ids_item)

        _source_integer_attribute_ids = d.pop("source_integer_attribute_ids", UNSET)
        source_integer_attribute_ids: list[UUID] | Unset = UNSET
        if _source_integer_attribute_ids is not UNSET:
            source_integer_attribute_ids = []
            for source_integer_attribute_ids_item_data in _source_integer_attribute_ids:
                source_integer_attribute_ids_item = UUID(source_integer_attribute_ids_item_data)

                source_integer_attribute_ids.append(source_integer_attribute_ids_item)

        _source_float_attribute_ids = d.pop("source_float_attribute_ids", UNSET)
        source_float_attribute_ids: list[UUID] | Unset = UNSET
        if _source_float_attribute_ids is not UNSET:
            source_float_attribute_ids = []
            for source_float_attribute_ids_item_data in _source_float_attribute_ids:
                source_float_attribute_ids_item = UUID(source_float_attribute_ids_item_data)

                source_float_attribute_ids.append(source_float_attribute_ids_item)

        _source_boolean_attribute_ids = d.pop("source_boolean_attribute_ids", UNSET)
        source_boolean_attribute_ids: list[UUID] | Unset = UNSET
        if _source_boolean_attribute_ids is not UNSET:
            source_boolean_attribute_ids = []
            for source_boolean_attribute_ids_item_data in _source_boolean_attribute_ids:
                source_boolean_attribute_ids_item = UUID(source_boolean_attribute_ids_item_data)

                source_boolean_attribute_ids.append(source_boolean_attribute_ids_item)

        _source_date_attribute_ids = d.pop("source_date_attribute_ids", UNSET)
        source_date_attribute_ids: list[UUID] | Unset = UNSET
        if _source_date_attribute_ids is not UNSET:
            source_date_attribute_ids = []
            for source_date_attribute_ids_item_data in _source_date_attribute_ids:
                source_date_attribute_ids_item = UUID(source_date_attribute_ids_item_data)

                source_date_attribute_ids.append(source_date_attribute_ids_item)

        _source_datetime_attribute_ids = d.pop("source_datetime_attribute_ids", UNSET)
        source_datetime_attribute_ids: list[UUID] | Unset = UNSET
        if _source_datetime_attribute_ids is not UNSET:
            source_datetime_attribute_ids = []
            for source_datetime_attribute_ids_item_data in _source_datetime_attribute_ids:
                source_datetime_attribute_ids_item = UUID(source_datetime_attribute_ids_item_data)

                source_datetime_attribute_ids.append(source_datetime_attribute_ids_item)

        _source_time_attribute_ids = d.pop("source_time_attribute_ids", UNSET)
        source_time_attribute_ids: list[UUID] | Unset = UNSET
        if _source_time_attribute_ids is not UNSET:
            source_time_attribute_ids = []
            for source_time_attribute_ids_item_data in _source_time_attribute_ids:
                source_time_attribute_ids_item = UUID(source_time_attribute_ids_item_data)

                source_time_attribute_ids.append(source_time_attribute_ids_item)

        _source_coordinate_attribute_ids = d.pop("source_coordinate_attribute_ids", UNSET)
        source_coordinate_attribute_ids: list[UUID] | Unset = UNSET
        if _source_coordinate_attribute_ids is not UNSET:
            source_coordinate_attribute_ids = []
            for source_coordinate_attribute_ids_item_data in _source_coordinate_attribute_ids:
                source_coordinate_attribute_ids_item = UUID(source_coordinate_attribute_ids_item_data)

                source_coordinate_attribute_ids.append(source_coordinate_attribute_ids_item)

        _source_polygon_attribute_ids = d.pop("source_polygon_attribute_ids", UNSET)
        source_polygon_attribute_ids: list[UUID] | Unset = UNSET
        if _source_polygon_attribute_ids is not UNSET:
            source_polygon_attribute_ids = []
            for source_polygon_attribute_ids_item_data in _source_polygon_attribute_ids:
                source_polygon_attribute_ids_item = UUID(source_polygon_attribute_ids_item_data)

                source_polygon_attribute_ids.append(source_polygon_attribute_ids_item)

        _source_table_attribute_ids = d.pop("source_table_attribute_ids", UNSET)
        source_table_attribute_ids: list[UUID] | Unset = UNSET
        if _source_table_attribute_ids is not UNSET:
            source_table_attribute_ids = []
            for source_table_attribute_ids_item_data in _source_table_attribute_ids:
                source_table_attribute_ids_item = UUID(source_table_attribute_ids_item_data)

                source_table_attribute_ids.append(source_table_attribute_ids_item)

        section_creation_put_in = cls(
            project_id=project_id,
            resource_ids=resource_ids,
            page_ids=page_ids,
            pages_paragraphs_paths=pages_paragraphs_paths,
            pages_tables_paths=pages_tables_paths,
            chunk_group_ids=chunk_group_ids,
            raw_text_ids=raw_text_ids,
            bim_project_object_ids=bim_project_object_ids,
            source_string_attribute_ids=source_string_attribute_ids,
            source_integer_attribute_ids=source_integer_attribute_ids,
            source_float_attribute_ids=source_float_attribute_ids,
            source_boolean_attribute_ids=source_boolean_attribute_ids,
            source_date_attribute_ids=source_date_attribute_ids,
            source_datetime_attribute_ids=source_datetime_attribute_ids,
            source_time_attribute_ids=source_time_attribute_ids,
            source_coordinate_attribute_ids=source_coordinate_attribute_ids,
            source_polygon_attribute_ids=source_polygon_attribute_ids,
            source_table_attribute_ids=source_table_attribute_ids,
        )

        section_creation_put_in.additional_properties = d
        return section_creation_put_in

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
