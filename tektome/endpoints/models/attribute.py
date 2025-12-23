from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribute_type import AttributeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.json_field import JsonField
    from ..models.table_column import TableColumn


T = TypeVar("T", bound="Attribute")


@_attrs_define
class Attribute:
    """WARN: Also used in the agent

    Attributes:
        name (str): Attribute name
        prompt (str): Prompt explaining what the attribute is
        kind (AttributeType): StrEnum for all available attribute types

            .. warning::
                Do not change the values of this enum, as they are used in the database.
                If you need to add a new attribute type, add a new enum value with a unique name.
        id (UUID | Unset):
        table_column_prompts (list[TableColumn] | Unset): Prompts for table columns, if the attribute is a table
        json_field_prompts (list[JsonField] | Unset): Prompts for json fields, if the attribute is a json
    """

    name: str
    prompt: str
    kind: AttributeType
    id: UUID | Unset = UNSET
    table_column_prompts: list[TableColumn] | Unset = UNSET
    json_field_prompts: list[JsonField] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        prompt = self.prompt

        kind = self.kind.value

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        table_column_prompts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.table_column_prompts, Unset):
            table_column_prompts = []
            for table_column_prompts_item_data in self.table_column_prompts:
                table_column_prompts_item = table_column_prompts_item_data.to_dict()
                table_column_prompts.append(table_column_prompts_item)

        json_field_prompts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.json_field_prompts, Unset):
            json_field_prompts = []
            for json_field_prompts_item_data in self.json_field_prompts:
                json_field_prompts_item = json_field_prompts_item_data.to_dict()
                json_field_prompts.append(json_field_prompts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "prompt": prompt,
                "kind": kind,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if table_column_prompts is not UNSET:
            field_dict["table_column_prompts"] = table_column_prompts
        if json_field_prompts is not UNSET:
            field_dict["json_field_prompts"] = json_field_prompts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.json_field import JsonField
        from ..models.table_column import TableColumn

        d = dict(src_dict)
        name = d.pop("name")

        prompt = d.pop("prompt")

        kind = AttributeType(d.pop("kind"))

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _table_column_prompts = d.pop("table_column_prompts", UNSET)
        table_column_prompts: list[TableColumn] | Unset = UNSET
        if _table_column_prompts is not UNSET:
            table_column_prompts = []
            for table_column_prompts_item_data in _table_column_prompts:
                table_column_prompts_item = TableColumn.from_dict(table_column_prompts_item_data)

                table_column_prompts.append(table_column_prompts_item)

        _json_field_prompts = d.pop("json_field_prompts", UNSET)
        json_field_prompts: list[JsonField] | Unset = UNSET
        if _json_field_prompts is not UNSET:
            json_field_prompts = []
            for json_field_prompts_item_data in _json_field_prompts:
                json_field_prompts_item = JsonField.from_dict(json_field_prompts_item_data)

                json_field_prompts.append(json_field_prompts_item)

        attribute = cls(
            name=name,
            prompt=prompt,
            kind=kind,
            id=id,
            table_column_prompts=table_column_prompts,
            json_field_prompts=json_field_prompts,
        )

        attribute.additional_properties = d
        return attribute

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
