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
    from ..models.get_extracted_page_get_out_tables_type_0 import GetExtractedPageGetOutTablesType0
    from ..models.positional_text import PositionalText


T = TypeVar("T", bound="GetExtractedPageGetOut")


@_attrs_define
class GetExtractedPageGetOut:
    """
    Attributes:
        positional_text (list[PositionalText]):
        created (datetime.datetime):
        updated (datetime.datetime):
        resource (UUID):
        page_number (int):
        width (float):
        height (float):
        unit (str):
        id (None | Unset | UUID):
        tables (GetExtractedPageGetOutTablesType0 | None | Unset):
    """

    positional_text: list[PositionalText]
    created: datetime.datetime
    updated: datetime.datetime
    resource: UUID
    page_number: int
    width: float
    height: float
    unit: str
    id: None | Unset | UUID = UNSET
    tables: GetExtractedPageGetOutTablesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_extracted_page_get_out_tables_type_0 import GetExtractedPageGetOutTablesType0

        positional_text = []
        for positional_text_item_data in self.positional_text:
            positional_text_item = positional_text_item_data.to_dict()
            positional_text.append(positional_text_item)

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
        elif isinstance(self.tables, GetExtractedPageGetOutTablesType0):
            tables = self.tables.to_dict()
        else:
            tables = self.tables

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "positional_text": positional_text,
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
        from ..models.get_extracted_page_get_out_tables_type_0 import GetExtractedPageGetOutTablesType0
        from ..models.positional_text import PositionalText

        d = dict(src_dict)
        positional_text = []
        _positional_text = d.pop("positional_text")
        for positional_text_item_data in _positional_text:
            positional_text_item = PositionalText.from_dict(positional_text_item_data)

            positional_text.append(positional_text_item)

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

        def _parse_tables(data: object) -> GetExtractedPageGetOutTablesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tables_type_0 = GetExtractedPageGetOutTablesType0.from_dict(data)

                return tables_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetExtractedPageGetOutTablesType0 | None | Unset, data)

        tables = _parse_tables(d.pop("tables", UNSET))

        get_extracted_page_get_out = cls(
            positional_text=positional_text,
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

        get_extracted_page_get_out.additional_properties = d
        return get_extracted_page_get_out

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
