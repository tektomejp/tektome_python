from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.large_language_model_enum import LargeLanguageModelEnum

if TYPE_CHECKING:
    from ..models.llm_search_input_shape import LLMSearchInputShape
    from ..models.llm_search_project_attributes import LLMSearchProjectAttributes


T = TypeVar("T", bound="LLMSearch")


@_attrs_define
class LLMSearch:
    """
    Attributes:
        model_name (LargeLanguageModelEnum):
        input_shape (LLMSearchInputShape):
        project_attributes (LLMSearchProjectAttributes):
        project_table (str):
        search_query (str):
    """

    model_name: LargeLanguageModelEnum
    input_shape: LLMSearchInputShape
    project_attributes: LLMSearchProjectAttributes
    project_table: str
    search_query: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_name = self.model_name.value

        input_shape = self.input_shape.to_dict()

        project_attributes = self.project_attributes.to_dict()

        project_table = self.project_table

        search_query = self.search_query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model_name": model_name,
                "input_shape": input_shape,
                "project_attributes": project_attributes,
                "project_table": project_table,
                "search_query": search_query,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.llm_search_input_shape import LLMSearchInputShape
        from ..models.llm_search_project_attributes import LLMSearchProjectAttributes

        d = dict(src_dict)
        model_name = LargeLanguageModelEnum(d.pop("model_name"))

        input_shape = LLMSearchInputShape.from_dict(d.pop("input_shape"))

        project_attributes = LLMSearchProjectAttributes.from_dict(d.pop("project_attributes"))

        project_table = d.pop("project_table")

        search_query = d.pop("search_query")

        llm_search = cls(
            model_name=model_name,
            input_shape=input_shape,
            project_attributes=project_attributes,
            project_table=project_table,
            search_query=search_query,
        )

        llm_search.additional_properties = d
        return llm_search

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
