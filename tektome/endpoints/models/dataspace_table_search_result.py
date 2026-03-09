from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataspace_entity_type import DataspaceEntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataspace_table_result_hit import DataspaceTableResultHit
    from ..models.dataspace_table_search_result_debug_type_0 import DataspaceTableSearchResultDebugType0
    from ..models.table_column_info import TableColumnInfo
    from ..models.table_result_info import TableResultInfo


T = TypeVar("T", bound="DataspaceTableSearchResult")


@_attrs_define
class DataspaceTableSearchResult:
    """Table-centric result. Each hit is a row-level match from a table attribute.

    Attributes:
        page (int):
        page_size (int):
        total_page (int):
        project_count (int):
        resource_count (int):
        table_name (str):
        parent_entity_type (DataspaceEntityType):
        type_ (Literal['table'] | Unset):  Default: 'table'.
        tables (list[TableResultInfo] | Unset):
        debug (DataspaceTableSearchResultDebugType0 | None | Unset):
        table_column_info (list[TableColumnInfo] | Unset):
        target_columns (list[str] | Unset):
        hits (list[DataspaceTableResultHit] | Unset):
    """

    page: int
    page_size: int
    total_page: int
    project_count: int
    resource_count: int
    table_name: str
    parent_entity_type: DataspaceEntityType
    type_: Literal["table"] | Unset = "table"
    tables: list[TableResultInfo] | Unset = UNSET
    debug: DataspaceTableSearchResultDebugType0 | None | Unset = UNSET
    table_column_info: list[TableColumnInfo] | Unset = UNSET
    target_columns: list[str] | Unset = UNSET
    hits: list[DataspaceTableResultHit] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dataspace_table_search_result_debug_type_0 import DataspaceTableSearchResultDebugType0

        page = self.page

        page_size = self.page_size

        total_page = self.total_page

        project_count = self.project_count

        resource_count = self.resource_count

        table_name = self.table_name

        parent_entity_type = self.parent_entity_type.value

        type_ = self.type_

        tables: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tables, Unset):
            tables = []
            for tables_item_data in self.tables:
                tables_item = tables_item_data.to_dict()
                tables.append(tables_item)

        debug: dict[str, Any] | None | Unset
        if isinstance(self.debug, Unset):
            debug = UNSET
        elif isinstance(self.debug, DataspaceTableSearchResultDebugType0):
            debug = self.debug.to_dict()
        else:
            debug = self.debug

        table_column_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.table_column_info, Unset):
            table_column_info = []
            for table_column_info_item_data in self.table_column_info:
                table_column_info_item = table_column_info_item_data.to_dict()
                table_column_info.append(table_column_info_item)

        target_columns: list[str] | Unset = UNSET
        if not isinstance(self.target_columns, Unset):
            target_columns = self.target_columns

        hits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hits, Unset):
            hits = []
            for hits_item_data in self.hits:
                hits_item = hits_item_data.to_dict()
                hits.append(hits_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "page_size": page_size,
                "total_page": total_page,
                "project_count": project_count,
                "resource_count": resource_count,
                "table_name": table_name,
                "parent_entity_type": parent_entity_type,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if tables is not UNSET:
            field_dict["tables"] = tables
        if debug is not UNSET:
            field_dict["debug"] = debug
        if table_column_info is not UNSET:
            field_dict["table_column_info"] = table_column_info
        if target_columns is not UNSET:
            field_dict["target_columns"] = target_columns
        if hits is not UNSET:
            field_dict["hits"] = hits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataspace_table_result_hit import DataspaceTableResultHit
        from ..models.dataspace_table_search_result_debug_type_0 import DataspaceTableSearchResultDebugType0
        from ..models.table_column_info import TableColumnInfo
        from ..models.table_result_info import TableResultInfo

        d = dict(src_dict)
        page = d.pop("page")

        page_size = d.pop("page_size")

        total_page = d.pop("total_page")

        project_count = d.pop("project_count")

        resource_count = d.pop("resource_count")

        table_name = d.pop("table_name")

        parent_entity_type = DataspaceEntityType(d.pop("parent_entity_type"))

        type_ = cast(Literal["table"] | Unset, d.pop("type", UNSET))
        if type_ != "table" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'table', got '{type_}'")

        _tables = d.pop("tables", UNSET)
        tables: list[TableResultInfo] | Unset = UNSET
        if _tables is not UNSET:
            tables = []
            for tables_item_data in _tables:
                tables_item = TableResultInfo.from_dict(tables_item_data)

                tables.append(tables_item)

        def _parse_debug(data: object) -> DataspaceTableSearchResultDebugType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                debug_type_0 = DataspaceTableSearchResultDebugType0.from_dict(data)

                return debug_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DataspaceTableSearchResultDebugType0 | None | Unset, data)

        debug = _parse_debug(d.pop("debug", UNSET))

        _table_column_info = d.pop("table_column_info", UNSET)
        table_column_info: list[TableColumnInfo] | Unset = UNSET
        if _table_column_info is not UNSET:
            table_column_info = []
            for table_column_info_item_data in _table_column_info:
                table_column_info_item = TableColumnInfo.from_dict(table_column_info_item_data)

                table_column_info.append(table_column_info_item)

        target_columns = cast(list[str], d.pop("target_columns", UNSET))

        _hits = d.pop("hits", UNSET)
        hits: list[DataspaceTableResultHit] | Unset = UNSET
        if _hits is not UNSET:
            hits = []
            for hits_item_data in _hits:
                hits_item = DataspaceTableResultHit.from_dict(hits_item_data)

                hits.append(hits_item)

        dataspace_table_search_result = cls(
            page=page,
            page_size=page_size,
            total_page=total_page,
            project_count=project_count,
            resource_count=resource_count,
            table_name=table_name,
            parent_entity_type=parent_entity_type,
            type_=type_,
            tables=tables,
            debug=debug,
            table_column_info=table_column_info,
            target_columns=target_columns,
            hits=hits,
        )

        dataspace_table_search_result.additional_properties = d
        return dataspace_table_search_result

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
