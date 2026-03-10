from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataspace_entity_type import DataspaceEntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataspace_search_result_hit import DataspaceSearchResultHit
    from ..models.table_row_cell_info import TableRowCellInfo


T = TypeVar("T", bound="DataspaceTableResultHit")


@_attrs_define
class DataspaceTableResultHit:
    """Entity-level hit from table search. Each hit carries the full parent entity and table rows.

    Attributes:
        parent_entity (DataspaceSearchResultHit): Base fields for a single search hit (project or resource).
        parent_entity_type (DataspaceEntityType):
        table_id (UUID):
        score (float):
        rows (list[list[TableRowCellInfo]] | Unset):
    """

    parent_entity: DataspaceSearchResultHit
    parent_entity_type: DataspaceEntityType
    table_id: UUID
    score: float
    rows: list[list[TableRowCellInfo]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_entity = self.parent_entity.to_dict()

        parent_entity_type = self.parent_entity_type.value

        table_id = str(self.table_id)

        score = self.score

        rows: list[list[dict[str, Any]]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = []
                for rows_item_item_data in rows_item_data:
                    rows_item_item = rows_item_item_data.to_dict()
                    rows_item.append(rows_item_item)

                rows.append(rows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_entity": parent_entity,
                "parent_entity_type": parent_entity_type,
                "table_id": table_id,
                "score": score,
            }
        )
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataspace_search_result_hit import DataspaceSearchResultHit
        from ..models.table_row_cell_info import TableRowCellInfo

        d = dict(src_dict)
        parent_entity = DataspaceSearchResultHit.from_dict(d.pop("parent_entity"))

        parent_entity_type = DataspaceEntityType(d.pop("parent_entity_type"))

        table_id = UUID(d.pop("table_id"))

        score = d.pop("score")

        _rows = d.pop("rows", UNSET)
        rows: list[list[TableRowCellInfo]] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = []
                _rows_item = rows_item_data
                for rows_item_item_data in _rows_item:
                    rows_item_item = TableRowCellInfo.from_dict(rows_item_item_data)

                    rows_item.append(rows_item_item)

                rows.append(rows_item)

        dataspace_table_result_hit = cls(
            parent_entity=parent_entity,
            parent_entity_type=parent_entity_type,
            table_id=table_id,
            score=score,
            rows=rows,
        )

        dataspace_table_result_hit.additional_properties = d
        return dataspace_table_result_hit

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
