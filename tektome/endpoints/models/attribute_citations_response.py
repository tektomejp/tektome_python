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
    from ..models.boolean_attribute_schema_response import BooleanAttributeSchemaResponse
    from ..models.coordinate_attribute_schema_response import CoordinateAttributeSchemaResponse
    from ..models.date_attribute_schema_response import DateAttributeSchemaResponse
    from ..models.date_time_attribute_schema_response import DateTimeAttributeSchemaResponse
    from ..models.float_attribute_schema_response import FloatAttributeSchemaResponse
    from ..models.integer_attribute_schema_response import IntegerAttributeSchemaResponse
    from ..models.json_attribute_schema_response import JSONAttributeSchemaResponse
    from ..models.multi_select_attribute_schema_response import MultiSelectAttributeSchemaResponse
    from ..models.polygon_attribute_schema_response import PolygonAttributeSchemaResponse
    from ..models.single_select_attribute_schema_response import SingleSelectAttributeSchemaResponse
    from ..models.string_attribute_schema_response import StringAttributeSchemaResponse
    from ..models.table_attribute_schema_response import TableAttributeSchemaResponse
    from ..models.time_attribute_schema_response import TimeAttributeSchemaResponse
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="AttributeCitationsResponse")


@_attrs_define
class AttributeCitationsResponse:
    """
    Attributes:
        created_by (UserMetadata):
        updated_by (UserMetadata):
        attribute (BooleanAttributeSchemaResponse | CoordinateAttributeSchemaResponse | DateAttributeSchemaResponse |
            DateTimeAttributeSchemaResponse | FloatAttributeSchemaResponse | IntegerAttributeSchemaResponse |
            JSONAttributeSchemaResponse | MultiSelectAttributeSchemaResponse | PolygonAttributeSchemaResponse |
            SingleSelectAttributeSchemaResponse | StringAttributeSchemaResponse | TableAttributeSchemaResponse |
            TimeAttributeSchemaResponse):
        created (datetime.datetime):
        updated (datetime.datetime):
        citation_type (Literal['attribute_citation'] | Unset):  Default: 'attribute_citation'.
        id (None | Unset | UUID):
        title (str | Unset):  Default: ''.
    """

    created_by: UserMetadata
    updated_by: UserMetadata
    attribute: (
        BooleanAttributeSchemaResponse
        | CoordinateAttributeSchemaResponse
        | DateAttributeSchemaResponse
        | DateTimeAttributeSchemaResponse
        | FloatAttributeSchemaResponse
        | IntegerAttributeSchemaResponse
        | JSONAttributeSchemaResponse
        | MultiSelectAttributeSchemaResponse
        | PolygonAttributeSchemaResponse
        | SingleSelectAttributeSchemaResponse
        | StringAttributeSchemaResponse
        | TableAttributeSchemaResponse
        | TimeAttributeSchemaResponse
    )
    created: datetime.datetime
    updated: datetime.datetime
    citation_type: Literal["attribute_citation"] | Unset = "attribute_citation"
    id: None | Unset | UUID = UNSET
    title: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.boolean_attribute_schema_response import BooleanAttributeSchemaResponse
        from ..models.coordinate_attribute_schema_response import CoordinateAttributeSchemaResponse
        from ..models.date_attribute_schema_response import DateAttributeSchemaResponse
        from ..models.date_time_attribute_schema_response import DateTimeAttributeSchemaResponse
        from ..models.float_attribute_schema_response import FloatAttributeSchemaResponse
        from ..models.integer_attribute_schema_response import IntegerAttributeSchemaResponse
        from ..models.json_attribute_schema_response import JSONAttributeSchemaResponse
        from ..models.polygon_attribute_schema_response import PolygonAttributeSchemaResponse
        from ..models.single_select_attribute_schema_response import SingleSelectAttributeSchemaResponse
        from ..models.string_attribute_schema_response import StringAttributeSchemaResponse
        from ..models.table_attribute_schema_response import TableAttributeSchemaResponse
        from ..models.time_attribute_schema_response import TimeAttributeSchemaResponse

        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        attribute: dict[str, Any]
        if isinstance(self.attribute, StringAttributeSchemaResponse):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, IntegerAttributeSchemaResponse):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, FloatAttributeSchemaResponse):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, BooleanAttributeSchemaResponse):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, DateAttributeSchemaResponse):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, DateTimeAttributeSchemaResponse):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, TimeAttributeSchemaResponse):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, CoordinateAttributeSchemaResponse):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, PolygonAttributeSchemaResponse):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, TableAttributeSchemaResponse):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, JSONAttributeSchemaResponse):
            attribute = self.attribute.to_dict()
        elif isinstance(self.attribute, SingleSelectAttributeSchemaResponse):
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
        from ..models.boolean_attribute_schema_response import BooleanAttributeSchemaResponse
        from ..models.coordinate_attribute_schema_response import CoordinateAttributeSchemaResponse
        from ..models.date_attribute_schema_response import DateAttributeSchemaResponse
        from ..models.date_time_attribute_schema_response import DateTimeAttributeSchemaResponse
        from ..models.float_attribute_schema_response import FloatAttributeSchemaResponse
        from ..models.integer_attribute_schema_response import IntegerAttributeSchemaResponse
        from ..models.json_attribute_schema_response import JSONAttributeSchemaResponse
        from ..models.multi_select_attribute_schema_response import MultiSelectAttributeSchemaResponse
        from ..models.polygon_attribute_schema_response import PolygonAttributeSchemaResponse
        from ..models.single_select_attribute_schema_response import SingleSelectAttributeSchemaResponse
        from ..models.string_attribute_schema_response import StringAttributeSchemaResponse
        from ..models.table_attribute_schema_response import TableAttributeSchemaResponse
        from ..models.time_attribute_schema_response import TimeAttributeSchemaResponse
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        def _parse_attribute(
            data: object,
        ) -> (
            BooleanAttributeSchemaResponse
            | CoordinateAttributeSchemaResponse
            | DateAttributeSchemaResponse
            | DateTimeAttributeSchemaResponse
            | FloatAttributeSchemaResponse
            | IntegerAttributeSchemaResponse
            | JSONAttributeSchemaResponse
            | MultiSelectAttributeSchemaResponse
            | PolygonAttributeSchemaResponse
            | SingleSelectAttributeSchemaResponse
            | StringAttributeSchemaResponse
            | TableAttributeSchemaResponse
            | TimeAttributeSchemaResponse
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_0 = StringAttributeSchemaResponse.from_dict(data)

                return componentsschemas_attribute_schema_out_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_1 = IntegerAttributeSchemaResponse.from_dict(data)

                return componentsschemas_attribute_schema_out_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_2 = FloatAttributeSchemaResponse.from_dict(data)

                return componentsschemas_attribute_schema_out_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_3 = BooleanAttributeSchemaResponse.from_dict(data)

                return componentsschemas_attribute_schema_out_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_4 = DateAttributeSchemaResponse.from_dict(data)

                return componentsschemas_attribute_schema_out_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_5 = DateTimeAttributeSchemaResponse.from_dict(data)

                return componentsschemas_attribute_schema_out_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_6 = TimeAttributeSchemaResponse.from_dict(data)

                return componentsschemas_attribute_schema_out_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_7 = CoordinateAttributeSchemaResponse.from_dict(data)

                return componentsschemas_attribute_schema_out_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_8 = PolygonAttributeSchemaResponse.from_dict(data)

                return componentsschemas_attribute_schema_out_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_9 = TableAttributeSchemaResponse.from_dict(data)

                return componentsschemas_attribute_schema_out_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_10 = JSONAttributeSchemaResponse.from_dict(data)

                return componentsschemas_attribute_schema_out_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_schema_out_type_11 = SingleSelectAttributeSchemaResponse.from_dict(data)

                return componentsschemas_attribute_schema_out_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_attribute_schema_out_type_12 = MultiSelectAttributeSchemaResponse.from_dict(data)

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

        attribute_citations_response = cls(
            created_by=created_by,
            updated_by=updated_by,
            attribute=attribute,
            created=created,
            updated=updated,
            citation_type=citation_type,
            id=id,
            title=title,
        )

        attribute_citations_response.additional_properties = d
        return attribute_citations_response

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
