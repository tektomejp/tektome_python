from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataspace_entity_type import DataspaceEntityType
from ..models.dataspace_search_request_schema_keyword_match_mode import DataspaceSearchRequestSchemaKeywordMatchMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_condition_input import FieldConditionInput


T = TypeVar("T", bound="DataspaceSearchRequestSchema")


@_attrs_define
class DataspaceSearchRequestSchema:
    """Base schema for search request fields

    Attributes:
        keywords (None | str | Unset): Search keywords for fuzzy matching across all string attributes
        highlight_keywords (list[str] | Unset): List of keywords to highlight in the search results
        tag_id (None | Unset | UUID): Tag configuration ID for the search request
        filter_ids (list[UUID] | Unset): List of filter configuration IDs to apply (stored for reference)
        conditions (list[FieldConditionInput] | Unset): List of field-based search conditions (field_id, action, value)
        page (int | Unset): Page number for pagination, starting from 1, default to 1 Default: 1.
        page_size (int | Unset): Page size for pagination, range between 1 and 100 default to 30 Default: 30.
        keyword_match_mode (DataspaceSearchRequestSchemaKeywordMatchMode | Unset): How to treat provided keywords: 'any'
            matches any keyword, 'all' requires all keywords. Defaults to any. Default:
            DataspaceSearchRequestSchemaKeywordMatchMode.ANY.
        max_chunks_per_resource (int | Unset): Maximum number of OCR chunk inner_hits to return per resource, be careful
            with high values as it may impact performance. Range between 1 and 100. Defaults to 5. Default: 5.
        max_resource_per_project (int | Unset): Maximum number of resource inner_hits to return per project be careful
            with high values as it may impact performance. Range between 1 and 100. Defaults to 25. Default: 25.
        target_entity (DataspaceEntityType | Unset):  Default: DataspaceEntityType.PROJECT.
        is_debug (bool | Unset): Enable debug mode to log raw query and results Default: False.
    """

    keywords: None | str | Unset = UNSET
    highlight_keywords: list[str] | Unset = UNSET
    tag_id: None | Unset | UUID = UNSET
    filter_ids: list[UUID] | Unset = UNSET
    conditions: list[FieldConditionInput] | Unset = UNSET
    page: int | Unset = 1
    page_size: int | Unset = 30
    keyword_match_mode: DataspaceSearchRequestSchemaKeywordMatchMode | Unset = (
        DataspaceSearchRequestSchemaKeywordMatchMode.ANY
    )
    max_chunks_per_resource: int | Unset = 5
    max_resource_per_project: int | Unset = 25
    target_entity: DataspaceEntityType | Unset = DataspaceEntityType.PROJECT
    is_debug: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keywords: None | str | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        else:
            keywords = self.keywords

        highlight_keywords: list[str] | Unset = UNSET
        if not isinstance(self.highlight_keywords, Unset):
            highlight_keywords = self.highlight_keywords

        tag_id: None | str | Unset
        if isinstance(self.tag_id, Unset):
            tag_id = UNSET
        elif isinstance(self.tag_id, UUID):
            tag_id = str(self.tag_id)
        else:
            tag_id = self.tag_id

        filter_ids: list[str] | Unset = UNSET
        if not isinstance(self.filter_ids, Unset):
            filter_ids = []
            for filter_ids_item_data in self.filter_ids:
                filter_ids_item = str(filter_ids_item_data)
                filter_ids.append(filter_ids_item)

        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        page = self.page

        page_size = self.page_size

        keyword_match_mode: str | Unset = UNSET
        if not isinstance(self.keyword_match_mode, Unset):
            keyword_match_mode = self.keyword_match_mode.value

        max_chunks_per_resource = self.max_chunks_per_resource

        max_resource_per_project = self.max_resource_per_project

        target_entity: str | Unset = UNSET
        if not isinstance(self.target_entity, Unset):
            target_entity = self.target_entity.value

        is_debug = self.is_debug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if highlight_keywords is not UNSET:
            field_dict["highlight_keywords"] = highlight_keywords
        if tag_id is not UNSET:
            field_dict["tag_id"] = tag_id
        if filter_ids is not UNSET:
            field_dict["filter_ids"] = filter_ids
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["page_size"] = page_size
        if keyword_match_mode is not UNSET:
            field_dict["keyword_match_mode"] = keyword_match_mode
        if max_chunks_per_resource is not UNSET:
            field_dict["max_chunks_per_resource"] = max_chunks_per_resource
        if max_resource_per_project is not UNSET:
            field_dict["max_resource_per_project"] = max_resource_per_project
        if target_entity is not UNSET:
            field_dict["target_entity"] = target_entity
        if is_debug is not UNSET:
            field_dict["is_debug"] = is_debug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_condition_input import FieldConditionInput

        d = dict(src_dict)

        def _parse_keywords(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        highlight_keywords = cast(list[str], d.pop("highlight_keywords", UNSET))

        def _parse_tag_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tag_id_type_0 = UUID(data)

                return tag_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        tag_id = _parse_tag_id(d.pop("tag_id", UNSET))

        _filter_ids = d.pop("filter_ids", UNSET)
        filter_ids: list[UUID] | Unset = UNSET
        if _filter_ids is not UNSET:
            filter_ids = []
            for filter_ids_item_data in _filter_ids:
                filter_ids_item = UUID(filter_ids_item_data)

                filter_ids.append(filter_ids_item)

        _conditions = d.pop("conditions", UNSET)
        conditions: list[FieldConditionInput] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = FieldConditionInput.from_dict(conditions_item_data)

                conditions.append(conditions_item)

        page = d.pop("page", UNSET)

        page_size = d.pop("page_size", UNSET)

        _keyword_match_mode = d.pop("keyword_match_mode", UNSET)
        keyword_match_mode: DataspaceSearchRequestSchemaKeywordMatchMode | Unset
        if isinstance(_keyword_match_mode, Unset):
            keyword_match_mode = UNSET
        else:
            keyword_match_mode = DataspaceSearchRequestSchemaKeywordMatchMode(_keyword_match_mode)

        max_chunks_per_resource = d.pop("max_chunks_per_resource", UNSET)

        max_resource_per_project = d.pop("max_resource_per_project", UNSET)

        _target_entity = d.pop("target_entity", UNSET)
        target_entity: DataspaceEntityType | Unset
        if isinstance(_target_entity, Unset):
            target_entity = UNSET
        else:
            target_entity = DataspaceEntityType(_target_entity)

        is_debug = d.pop("is_debug", UNSET)

        dataspace_search_request_schema = cls(
            keywords=keywords,
            highlight_keywords=highlight_keywords,
            tag_id=tag_id,
            filter_ids=filter_ids,
            conditions=conditions,
            page=page,
            page_size=page_size,
            keyword_match_mode=keyword_match_mode,
            max_chunks_per_resource=max_chunks_per_resource,
            max_resource_per_project=max_resource_per_project,
            target_entity=target_entity,
            is_debug=is_debug,
        )

        dataspace_search_request_schema.additional_properties = d
        return dataspace_search_request_schema

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
