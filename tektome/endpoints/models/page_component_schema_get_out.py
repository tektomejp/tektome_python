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
    from ..models.chunk import Chunk
    from ..models.page_component_schema_get_out_tables_type_0 import PageComponentSchemaGetOutTablesType0


T = TypeVar("T", bound="PageComponentSchemaGetOut")


@_attrs_define
class PageComponentSchemaGetOut:
    """
    Attributes:
        chunks (list[Chunk]):
        created (datetime.datetime):
        updated (datetime.datetime):
        resource (UUID):
        page_number (int):
        width (float):
        height (float):
        unit (str):
        id (None | Unset | UUID):
        tables (None | PageComponentSchemaGetOutTablesType0 | Unset):
    """

    chunks: list[Chunk]
    created: datetime.datetime
    updated: datetime.datetime
    resource: UUID
    page_number: int
    width: float
    height: float
    unit: str
    id: None | Unset | UUID = UNSET
    tables: None | PageComponentSchemaGetOutTablesType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.page_component_schema_get_out_tables_type_0 import PageComponentSchemaGetOutTablesType0

        chunks = []
        for chunks_item_data in self.chunks:
            chunks_item = chunks_item_data.to_dict()
            chunks.append(chunks_item)

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        resource = str(self.resource)

        page_number = self.page_number

        width = self.width

        height = self.height

        unit = self.unit

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        tables: dict[str, Any] | None | Unset
        if isinstance(self.tables, Unset):
            tables = UNSET
        elif isinstance(self.tables, PageComponentSchemaGetOutTablesType0):
            tables = self.tables.to_dict()
        else:
            tables = self.tables

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chunks": chunks,
                "created": created,
                "updated": updated,
                "resource": resource,
                "page_number": page_number,
                "width": width,
                "height": height,
                "unit": unit,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if tables is not UNSET:
            field_dict["tables"] = tables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chunk import Chunk
        from ..models.page_component_schema_get_out_tables_type_0 import PageComponentSchemaGetOutTablesType0

        d = dict(src_dict)
        chunks = []
        _chunks = d.pop("chunks")
        for chunks_item_data in _chunks:
            chunks_item = Chunk.from_dict(chunks_item_data)

            chunks.append(chunks_item)

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        resource = UUID(d.pop("resource"))

        page_number = d.pop("page_number")

        width = d.pop("width")

        height = d.pop("height")

        unit = d.pop("unit")

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

        def _parse_tables(data: object) -> None | PageComponentSchemaGetOutTablesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tables_type_0 = PageComponentSchemaGetOutTablesType0.from_dict(data)

                return tables_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PageComponentSchemaGetOutTablesType0 | Unset, data)

        tables = _parse_tables(d.pop("tables", UNSET))

        page_component_schema_get_out = cls(
            chunks=chunks,
            created=created,
            updated=updated,
            resource=resource,
            page_number=page_number,
            width=width,
            height=height,
            unit=unit,
            id=id,
            tables=tables,
        )

        page_component_schema_get_out.additional_properties = d
        return page_component_schema_get_out

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
