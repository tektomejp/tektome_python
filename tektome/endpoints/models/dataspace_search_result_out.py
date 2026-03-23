from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dataspace_search_request_get_out import DataspaceSearchRequestGetOut
    from ..models.paginated_search_result_hits import PaginatedSearchResultHits


T = TypeVar("T", bound="DataspaceSearchResultOut")


@_attrs_define
class DataspaceSearchResultOut:
    """Output schema for search results with search request info

    Attributes:
        search_request (DataspaceSearchRequestGetOut): Output schema for a single search request
        search_result (PaginatedSearchResultHits): Paginated search result hits
    """

    search_request: DataspaceSearchRequestGetOut
    search_result: PaginatedSearchResultHits
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search_request = self.search_request.to_dict()

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
        from ..models.dataspace_search_request_get_out import DataspaceSearchRequestGetOut
        from ..models.paginated_search_result_hits import PaginatedSearchResultHits

        d = dict(src_dict)
        search_request = DataspaceSearchRequestGetOut.from_dict(d.pop("search_request"))

        search_result = PaginatedSearchResultHits.from_dict(d.pop("search_result"))

        dataspace_search_result_out = cls(
            search_request=search_request,
            search_result=search_result,
        )

        dataspace_search_result_out.additional_properties = d
        return dataspace_search_result_out

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
