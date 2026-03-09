from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataspace_project_result_hit import DataspaceProjectResultHit
    from ..models.dataspace_project_search_result_debug_type_0 import DataspaceProjectSearchResultDebugType0


T = TypeVar("T", bound="DataspaceProjectSearchResult")


@_attrs_define
class DataspaceProjectSearchResult:
    """Project-centric result. Each hit embeds its child resources.

    Attributes:
        page (int):
        page_size (int):
        total_page (int):
        project_count (int):
        resource_count (int):
        hits (list[DataspaceProjectResultHit]):
        type_ (Literal['project'] | Unset):  Default: 'project'.
        debug (DataspaceProjectSearchResultDebugType0 | None | Unset):
    """

    page: int
    page_size: int
    total_page: int
    project_count: int
    resource_count: int
    hits: list[DataspaceProjectResultHit]
    type_: Literal["project"] | Unset = "project"
    debug: DataspaceProjectSearchResultDebugType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dataspace_project_search_result_debug_type_0 import DataspaceProjectSearchResultDebugType0

        page = self.page

        page_size = self.page_size

        total_page = self.total_page

        project_count = self.project_count

        resource_count = self.resource_count

        hits = []
        for hits_item_data in self.hits:
            hits_item = hits_item_data.to_dict()
            hits.append(hits_item)

        type_ = self.type_

        debug: dict[str, Any] | None | Unset
        if isinstance(self.debug, Unset):
            debug = UNSET
        elif isinstance(self.debug, DataspaceProjectSearchResultDebugType0):
            debug = self.debug.to_dict()
        else:
            debug = self.debug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "page_size": page_size,
                "total_page": total_page,
                "project_count": project_count,
                "resource_count": resource_count,
                "hits": hits,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if debug is not UNSET:
            field_dict["debug"] = debug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataspace_project_result_hit import DataspaceProjectResultHit
        from ..models.dataspace_project_search_result_debug_type_0 import DataspaceProjectSearchResultDebugType0

        d = dict(src_dict)
        page = d.pop("page")

        page_size = d.pop("page_size")

        total_page = d.pop("total_page")

        project_count = d.pop("project_count")

        resource_count = d.pop("resource_count")

        hits = []
        _hits = d.pop("hits")
        for hits_item_data in _hits:
            hits_item = DataspaceProjectResultHit.from_dict(hits_item_data)

            hits.append(hits_item)

        type_ = cast(Literal["project"] | Unset, d.pop("type", UNSET))
        if type_ != "project" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'project', got '{type_}'")

        def _parse_debug(data: object) -> DataspaceProjectSearchResultDebugType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                debug_type_0 = DataspaceProjectSearchResultDebugType0.from_dict(data)

                return debug_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DataspaceProjectSearchResultDebugType0 | None | Unset, data)

        debug = _parse_debug(d.pop("debug", UNSET))

        dataspace_project_search_result = cls(
            page=page,
            page_size=page_size,
            total_page=total_page,
            project_count=project_count,
            resource_count=resource_count,
            hits=hits,
            type_=type_,
            debug=debug,
        )

        dataspace_project_search_result.additional_properties = d
        return dataspace_project_search_result

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
