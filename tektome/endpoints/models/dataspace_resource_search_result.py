from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataspace_resource_result_hit import DataspaceResourceResultHit
    from ..models.dataspace_resource_search_result_debug_type_0 import DataspaceResourceSearchResultDebugType0
    from ..models.table_result_info import TableResultInfo
    from ..models.total_objects_count import TotalObjectsCount


T = TypeVar("T", bound="DataspaceResourceSearchResult")


@_attrs_define
class DataspaceResourceSearchResult:
    """Resource-centric result. Each hit embeds its parent project.

    Attributes:
        page (int):
        page_size (int):
        total_page (int):
        hits (list[DataspaceResourceResultHit]):
        type_ (Literal['resource'] | Unset):  Default: 'resource'.
        total_objects_count (TotalObjectsCount | Unset): Aggregated counts of matched objects across the entire search
            result.
        tables (list[TableResultInfo] | Unset):
        debug (DataspaceResourceSearchResultDebugType0 | None | Unset):
    """

    page: int
    page_size: int
    total_page: int
    hits: list[DataspaceResourceResultHit]
    type_: Literal["resource"] | Unset = "resource"
    total_objects_count: TotalObjectsCount | Unset = UNSET
    tables: list[TableResultInfo] | Unset = UNSET
    debug: DataspaceResourceSearchResultDebugType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dataspace_resource_search_result_debug_type_0 import DataspaceResourceSearchResultDebugType0

        page = self.page

        page_size = self.page_size

        total_page = self.total_page

        hits = []
        for hits_item_data in self.hits:
            hits_item = hits_item_data.to_dict()
            hits.append(hits_item)

        type_ = self.type_

        total_objects_count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_objects_count, Unset):
            total_objects_count = self.total_objects_count.to_dict()

        tables: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tables, Unset):
            tables = []
            for tables_item_data in self.tables:
                tables_item = tables_item_data.to_dict()
                tables.append(tables_item)

        debug: dict[str, Any] | None | Unset
        if isinstance(self.debug, Unset):
            debug = UNSET
        elif isinstance(self.debug, DataspaceResourceSearchResultDebugType0):
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
                "hits": hits,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if total_objects_count is not UNSET:
            field_dict["total_objects_count"] = total_objects_count
        if tables is not UNSET:
            field_dict["tables"] = tables
        if debug is not UNSET:
            field_dict["debug"] = debug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataspace_resource_result_hit import DataspaceResourceResultHit
        from ..models.dataspace_resource_search_result_debug_type_0 import DataspaceResourceSearchResultDebugType0
        from ..models.table_result_info import TableResultInfo
        from ..models.total_objects_count import TotalObjectsCount

        d = dict(src_dict)
        page = d.pop("page")

        page_size = d.pop("page_size")

        total_page = d.pop("total_page")

        hits = []
        _hits = d.pop("hits")
        for hits_item_data in _hits:
            hits_item = DataspaceResourceResultHit.from_dict(hits_item_data)

            hits.append(hits_item)

        type_ = cast(Literal["resource"] | Unset, d.pop("type", UNSET))
        if type_ != "resource" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'resource', got '{type_}'")

        _total_objects_count = d.pop("total_objects_count", UNSET)
        total_objects_count: TotalObjectsCount | Unset
        if isinstance(_total_objects_count, Unset):
            total_objects_count = UNSET
        else:
            total_objects_count = TotalObjectsCount.from_dict(_total_objects_count)

        _tables = d.pop("tables", UNSET)
        tables: list[TableResultInfo] | Unset = UNSET
        if _tables is not UNSET:
            tables = []
            for tables_item_data in _tables:
                tables_item = TableResultInfo.from_dict(tables_item_data)

                tables.append(tables_item)

        def _parse_debug(data: object) -> DataspaceResourceSearchResultDebugType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                debug_type_0 = DataspaceResourceSearchResultDebugType0.from_dict(data)

                return debug_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DataspaceResourceSearchResultDebugType0 | None | Unset, data)

        debug = _parse_debug(d.pop("debug", UNSET))

        dataspace_resource_search_result = cls(
            page=page,
            page_size=page_size,
            total_page=total_page,
            hits=hits,
            type_=type_,
            total_objects_count=total_objects_count,
            tables=tables,
            debug=debug,
        )

        dataspace_resource_search_result.additional_properties = d
        return dataspace_resource_search_result

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
