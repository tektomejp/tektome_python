from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dataspace_project_search_result import DataspaceProjectSearchResult
    from ..models.dataspace_resource_search_result import DataspaceResourceSearchResult
    from ..models.dataspace_search_request_response import DataspaceSearchRequestResponse
    from ..models.dataspace_table_search_result import DataspaceTableSearchResult


T = TypeVar("T", bound="DataspaceSearchResultResponse")


@_attrs_define
class DataspaceSearchResultResponse:
    """Output schema for search results with search request info

    Attributes:
        search_request (DataspaceSearchRequestResponse): Output schema for a single search request
        search_result (DataspaceProjectSearchResult | DataspaceResourceSearchResult | DataspaceTableSearchResult): A
            resource-centric, project-centric, or table-centric search result
    """

    search_request: DataspaceSearchRequestResponse
    search_result: DataspaceProjectSearchResult | DataspaceResourceSearchResult | DataspaceTableSearchResult
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dataspace_project_search_result import DataspaceProjectSearchResult
        from ..models.dataspace_resource_search_result import DataspaceResourceSearchResult

        search_request = self.search_request.to_dict()

        search_result: dict[str, Any]
        if isinstance(self.search_result, DataspaceResourceSearchResult):
            search_result = self.search_result.to_dict()
        elif isinstance(self.search_result, DataspaceProjectSearchResult):
            search_result = self.search_result.to_dict()
        else:
            search_result = self.search_result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "search_request": search_request,
                "search_result": search_result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataspace_project_search_result import DataspaceProjectSearchResult
        from ..models.dataspace_resource_search_result import DataspaceResourceSearchResult
        from ..models.dataspace_search_request_response import DataspaceSearchRequestResponse
        from ..models.dataspace_table_search_result import DataspaceTableSearchResult

        d = dict(src_dict)
        search_request = DataspaceSearchRequestResponse.from_dict(d.pop("search_request"))

        def _parse_search_result(
            data: object,
        ) -> DataspaceProjectSearchResult | DataspaceResourceSearchResult | DataspaceTableSearchResult:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                search_result_type_0 = DataspaceResourceSearchResult.from_dict(data)

                return search_result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                search_result_type_1 = DataspaceProjectSearchResult.from_dict(data)

                return search_result_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            search_result_type_2 = DataspaceTableSearchResult.from_dict(data)

            return search_result_type_2

        search_result = _parse_search_result(d.pop("search_result"))

        dataspace_search_result_response = cls(
            search_request=search_request,
            search_result=search_result,
        )

        dataspace_search_result_response.additional_properties = d
        return dataspace_search_result_response

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
