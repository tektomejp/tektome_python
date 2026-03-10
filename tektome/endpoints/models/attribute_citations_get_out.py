from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.boolean_attribute_schema_out import BooleanAttributeSchemaOut
    from ..models.coordinate_attribute_schema_out import CoordinateAttributeSchemaOut
    from ..models.date_attribute_schema_out import DateAttributeSchemaOut
    from ..models.date_time_attribute_schema_out import DateTimeAttributeSchemaOut
    from ..models.float_attribute_schema_out import FloatAttributeSchemaOut
    from ..models.integer_attribute_schema_out import IntegerAttributeSchemaOut
    from ..models.json_attribute_schema_out import JSONAttributeSchemaOut
    from ..models.multi_select_attribute_schema_out import MultiSelectAttributeSchemaOut
    from ..models.polygon_attribute_schema_out import PolygonAttributeSchemaOut
    from ..models.single_select_attribute_schema_out import SingleSelectAttributeSchemaOut
    from ..models.string_attribute_schema_out import StringAttributeSchemaOut
    from ..models.table_attribute_schema_out import TableAttributeSchemaOut
    from ..models.time_attribute_schema_out import TimeAttributeSchemaOut
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="AttributeCitationsGetOut")


@_attrs_define
class AttributeCitationsGetOut:
    """
    Attributes:
        created_by (UserMetadata):
        updated_by (UserMetadata):
        attribute (BooleanAttributeSchemaOut | CoordinateAttributeSchemaOut | DateAttributeSchemaOut |
            DateTimeAttributeSchemaOut | FloatAttributeSchemaOut | IntegerAttributeSchemaOut | JSONAttributeSchemaOut |
            MultiSelectAttributeSchemaOut | PolygonAttributeSchemaOut | SingleSelectAttributeSchemaOut |
            StringAttributeSchemaOut | TableAttributeSchemaOut | TimeAttributeSchemaOut):
        created (datetime.datetime):
        updated (datetime.datetime):
        citation_type (Literal['attribute_citation'] | Unset):  Default: 'attribute_citation'.
        id (None | Unset | UUID):
        title (str | Unset):  Default: ''.
    """

    created_by: UserMetadata
    updated_by: UserMetadata
    attribute: (
        BooleanAttributeSchemaOut
        | CoordinateAttributeSchemaOut
        | DateAttributeSchemaOut
        | DateTimeAttributeSchemaOut
        | FloatAttributeSchemaOut
        | IntegerAttributeSchemaOut
        | JSONAttributeSchemaOut
        | MultiSelectAttributeSchemaOut
        | PolygonAttributeSchemaOut
        | SingleSelectAttributeSchemaOut
        | StringAttributeSchemaOut
        | TableAttributeSchemaOut
        | TimeAttributeSchemaOut
    )
    created: datetime.datetime
    updated: datetime.datetime
    citation_type: Literal["attribute_citation"] | Unset = "attribute_citation"
    id: None | Unset | UUID = UNSET
    title: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.boolean_attribute_schema_out import BooleanAttributeSchemaOut
        from ..models.coordinate_attribute_schema_out import CoordinateAttributeSchemaOut
        from ..models.date_attribute_schema_out import DateAttributeSchemaOut
        from ..models.date_time_attribute_schema_out import DateTimeAttributeSchemaOut
        from ..models.float_attribute_schema_out import FloatAttributeSchemaOut
        from ..models.integer_attribute_schema_out import IntegerAttributeSchemaOut
        from ..models.json_attribute_schema_out import JSONAttributeSchemaOut
        from ..models.polygon_attribute_schema_out import PolygonAttributeSchemaOut
        from ..models.single_select_attribute_schema_out import SingleSelectAttributeSchemaOut
        from ..models.string_attribute_schema_out import StringAttributeSchemaOut
        from ..models.table_attribute_schema_out import TableAttributeSchemaOut
        from ..models.time_attribute_schema_out import TimeAttributeSchemaOut

        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        attribute: dict[str, Any]
        if isinstance(self.attribute, StringAttributeSchemaOut):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, IntegerAttributeSchemaOut):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, FloatAttributeSchemaOut):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, BooleanAttributeSchemaOut):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, DateAttributeSchemaOut):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, DateTimeAttributeSchemaOut):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, TimeAttributeSchemaOut):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, CoordinateAttributeSchemaOut):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, PolygonAttributeSchemaOut):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, TableAttributeSchemaOut):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, JSONAttributeSchemaOut):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, SingleSelectAttributeSchemaOut):
            attribute = self.attribute.to_dict()
        else:
            attribute = self.attribute.to_dict()

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        citation_type = self.citation_type

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_by": created_by,
                "updated_by": updated_by,
                "attribute": attribute,
                "created": created,
                "updated": updated,
            }
        )
        if citation_type is not UNSET:
            field_dict["citation_type"] = citation_type
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.boolean_attribute_schema_out import BooleanAttributeSchemaOut
        from ..models.coordinate_attribute_schema_out import CoordinateAttributeSchemaOut
        from ..models.date_attribute_schema_out import DateAttributeSchemaOut
        from ..models.date_time_attribute_schema_out import DateTimeAttributeSchemaOut
        from ..models.float_attribute_schema_out import FloatAttributeSchemaOut
        from ..models.integer_attribute_schema_out import IntegerAttributeSchemaOut
        from ..models.json_attribute_schema_out import JSONAttributeSchemaOut
        from ..models.multi_select_attribute_schema_out import MultiSelectAttributeSchemaOut
        from ..models.polygon_attribute_schema_out import PolygonAttributeSchemaOut
        from ..models.single_select_attribute_schema_out import SingleSelectAttributeSchemaOut
        from ..models.string_attribute_schema_out import StringAttributeSchemaOut
        from ..models.table_attribute_schema_out import TableAttributeSchemaOut
        from ..models.time_attribute_schema_out import TimeAttributeSchemaOut
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        def _parse_attribute(
            data: object,
        ) -> (
            BooleanAttributeSchemaOut
            | CoordinateAttributeSchemaOut
            | DateAttributeSchemaOut
            | DateTimeAttributeSchemaOut
            | FloatAttributeSchemaOut
            | IntegerAttributeSchemaOut
            | JSONAttributeSchemaOut
            | MultiSelectAttributeSchemaOut
            | PolygonAttributeSchemaOut
            | SingleSelectAttributeSchemaOut
            | StringAttributeSchemaOut
            | TableAttributeSchemaOut
            | TimeAttributeSchemaOut
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_0 = StringAttributeSchemaOut.from_dict(data)

                return componentsschemas_attribute_schema_out_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_1 = IntegerAttributeSchemaOut.from_dict(data)

                return componentsschemas_attribute_schema_out_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_2 = FloatAttributeSchemaOut.from_dict(data)

                return componentsschemas_attribute_schema_out_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_3 = BooleanAttributeSchemaOut.from_dict(data)

                return componentsschemas_attribute_schema_out_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_4 = DateAttributeSchemaOut.from_dict(data)

                return componentsschemas_attribute_schema_out_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_5 = DateTimeAttributeSchemaOut.from_dict(data)

                return componentsschemas_attribute_schema_out_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_6 = TimeAttributeSchemaOut.from_dict(data)

                return componentsschemas_attribute_schema_out_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_7 = CoordinateAttributeSchemaOut.from_dict(data)

                return componentsschemas_attribute_schema_out_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_8 = PolygonAttributeSchemaOut.from_dict(data)

                return componentsschemas_attribute_schema_out_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_9 = TableAttributeSchemaOut.from_dict(data)

                return componentsschemas_attribute_schema_out_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_10 = JSONAttributeSchemaOut.from_dict(data)

                return componentsschemas_attribute_schema_out_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_11 = SingleSelectAttributeSchemaOut.from_dict(data)

                return componentsschemas_attribute_schema_out_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_attribute_schema_out_type_12 = MultiSelectAttributeSchemaOut.from_dict(data)

            return componentsschemas_attribute_schema_out_type_12

        attribute = _parse_attribute(d.pop("attribute"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        citation_type = cast(Literal["attribute_citation"] | Unset, d.pop("citation_type", UNSET))
        if citation_type != "attribute_citation" and not isinstance(citation_type, Unset):
            raise ValueError(f"citation_type must match const 'attribute_citation', got '{citation_type}'")

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

        title = d.pop("title", UNSET)

        attribute_citations_get_out = cls(
            created_by=created_by,
            updated_by=updated_by,
            attribute=attribute,
            created=created,
            updated=updated,
            citation_type=citation_type,
            id=id,
            title=title,
        )

        attribute_citations_get_out.additional_properties = d
        return attribute_citations_get_out

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
