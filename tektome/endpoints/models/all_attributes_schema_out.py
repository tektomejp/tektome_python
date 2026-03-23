from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.boolean_attribute_schema_out import BooleanAttributeSchemaOut
    from ..models.coordinate_attribute_schema_out import CoordinateAttributeSchemaOut
    from ..models.date_attribute_schema_out import DateAttributeSchemaOut
    from ..models.date_time_attribute_schema_out import DateTimeAttributeSchemaOut
    from ..models.float_attribute_schema_out import FloatAttributeSchemaOut
    from ..models.integer_attribute_schema_out import IntegerAttributeSchemaOut
    from ..models.json_attribute_schema_out import JSONAttributeSchemaOut
    from ..models.polygon_attribute_schema_out import PolygonAttributeSchemaOut
    from ..models.string_attribute_schema_out import StringAttributeSchemaOut
    from ..models.table_attribute_schema_out import TableAttributeSchemaOut
    from ..models.time_attribute_schema_out import TimeAttributeSchemaOut


T = TypeVar("T", bound="AllAttributesSchemaOut")


@_attrs_define
class AllAttributesSchemaOut:
    """
    Attributes:
        string_attributes (list[StringAttributeSchemaOut]):
        integer_attributes (list[IntegerAttributeSchemaOut]):
        float_attributes (list[FloatAttributeSchemaOut]):
        boolean_attributes (list[BooleanAttributeSchemaOut]):
        date_attributes (list[DateAttributeSchemaOut]):
        datetime_attributes (list[DateTimeAttributeSchemaOut]):
        time_attributes (list[TimeAttributeSchemaOut]):
        coordinate_attributes (list[CoordinateAttributeSchemaOut]):
        polygon_attributes (list[PolygonAttributeSchemaOut]):
        table_attributes (list[TableAttributeSchemaOut]):
        json_attributes (list[JSONAttributeSchemaOut]):
    """

    string_attributes: list[StringAttributeSchemaOut]
    integer_attributes: list[IntegerAttributeSchemaOut]
    float_attributes: list[FloatAttributeSchemaOut]
    boolean_attributes: list[BooleanAttributeSchemaOut]
    date_attributes: list[DateAttributeSchemaOut]
    datetime_attributes: list[DateTimeAttributeSchemaOut]
    time_attributes: list[TimeAttributeSchemaOut]
    coordinate_attributes: list[CoordinateAttributeSchemaOut]
    polygon_attributes: list[PolygonAttributeSchemaOut]
    table_attributes: list[TableAttributeSchemaOut]
    json_attributes: list[JSONAttributeSchemaOut]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        string_attributes = []
        for string_attributes_item_data in self.string_attributes:
            string_attributes_item = string_attributes_item_data.to_dict()
            string_attributes.append(string_attributes_item)

        integer_attributes = []
        for integer_attributes_item_data in self.integer_attributes:
            integer_attributes_item = integer_attributes_item_data.to_dict()
            integer_attributes.append(integer_attributes_item)

        float_attributes = []
        for float_attributes_item_data in self.float_attributes:
            float_attributes_item = float_attributes_item_data.to_dict()
            float_attributes.append(float_attributes_item)

        boolean_attributes = []
        for boolean_attributes_item_data in self.boolean_attributes:
            boolean_attributes_item = boolean_attributes_item_data.to_dict()
            boolean_attributes.append(boolean_attributes_item)

        date_attributes = []
        for date_attributes_item_data in self.date_attributes:
            date_attributes_item = date_attributes_item_data.to_dict()
            date_attributes.append(date_attributes_item)

        datetime_attributes = []
        for datetime_attributes_item_data in self.datetime_attributes:
            datetime_attributes_item = datetime_attributes_item_data.to_dict()
            datetime_attributes.append(datetime_attributes_item)

        time_attributes = []
        for time_attributes_item_data in self.time_attributes:
            time_attributes_item = time_attributes_item_data.to_dict()
            time_attributes.append(time_attributes_item)

        coordinate_attributes = []
        for coordinate_attributes_item_data in self.coordinate_attributes:
            coordinate_attributes_item = coordinate_attributes_item_data.to_dict()
            coordinate_attributes.append(coordinate_attributes_item)

        polygon_attributes = []
        for polygon_attributes_item_data in self.polygon_attributes:
            polygon_attributes_item = polygon_attributes_item_data.to_dict()
            polygon_attributes.append(polygon_attributes_item)

        table_attributes = []
        for table_attributes_item_data in self.table_attributes:
            table_attributes_item = table_attributes_item_data.to_dict()
            table_attributes.append(table_attributes_item)

        json_attributes = []
        for json_attributes_item_data in self.json_attributes:
            json_attributes_item = json_attributes_item_data.to_dict()
            json_attributes.append(json_attributes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "string_attributes": string_attributes,
                "integer_attributes": integer_attributes,
                "float_attributes": float_attributes,
                "boolean_attributes": boolean_attributes,
                "date_attributes": date_attributes,
                "datetime_attributes": datetime_attributes,
                "time_attributes": time_attributes,
                "coordinate_attributes": coordinate_attributes,
                "polygon_attributes": polygon_attributes,
                "table_attributes": table_attributes,
                "json_attributes": json_attributes,
            }
        )

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
        from ..models.polygon_attribute_schema_out import PolygonAttributeSchemaOut
        from ..models.string_attribute_schema_out import StringAttributeSchemaOut
        from ..models.table_attribute_schema_out import TableAttributeSchemaOut
        from ..models.time_attribute_schema_out import TimeAttributeSchemaOut

        d = dict(src_dict)
        string_attributes = []
        _string_attributes = d.pop("string_attributes")
        for string_attributes_item_data in _string_attributes:
            string_attributes_item = StringAttributeSchemaOut.from_dict(string_attributes_item_data)

            string_attributes.append(string_attributes_item)

        integer_attributes = []
        _integer_attributes = d.pop("integer_attributes")
        for integer_attributes_item_data in _integer_attributes:
            integer_attributes_item = IntegerAttributeSchemaOut.from_dict(integer_attributes_item_data)

            integer_attributes.append(integer_attributes_item)

        float_attributes = []
        _float_attributes = d.pop("float_attributes")
        for float_attributes_item_data in _float_attributes:
            float_attributes_item = FloatAttributeSchemaOut.from_dict(float_attributes_item_data)

            float_attributes.append(float_attributes_item)

        boolean_attributes = []
        _boolean_attributes = d.pop("boolean_attributes")
        for boolean_attributes_item_data in _boolean_attributes:
            boolean_attributes_item = BooleanAttributeSchemaOut.from_dict(boolean_attributes_item_data)

            boolean_attributes.append(boolean_attributes_item)

        date_attributes = []
        _date_attributes = d.pop("date_attributes")
        for date_attributes_item_data in _date_attributes:
            date_attributes_item = DateAttributeSchemaOut.from_dict(date_attributes_item_data)

            date_attributes.append(date_attributes_item)

        datetime_attributes = []
        _datetime_attributes = d.pop("datetime_attributes")
        for datetime_attributes_item_data in _datetime_attributes:
            datetime_attributes_item = DateTimeAttributeSchemaOut.from_dict(datetime_attributes_item_data)

            datetime_attributes.append(datetime_attributes_item)

        time_attributes = []
        _time_attributes = d.pop("time_attributes")
        for time_attributes_item_data in _time_attributes:
            time_attributes_item = TimeAttributeSchemaOut.from_dict(time_attributes_item_data)

            time_attributes.append(time_attributes_item)

        coordinate_attributes = []
        _coordinate_attributes = d.pop("coordinate_attributes")
        for coordinate_attributes_item_data in _coordinate_attributes:
            coordinate_attributes_item = CoordinateAttributeSchemaOut.from_dict(coordinate_attributes_item_data)

            coordinate_attributes.append(coordinate_attributes_item)

        polygon_attributes = []
        _polygon_attributes = d.pop("polygon_attributes")
        for polygon_attributes_item_data in _polygon_attributes:
            polygon_attributes_item = PolygonAttributeSchemaOut.from_dict(polygon_attributes_item_data)

            polygon_attributes.append(polygon_attributes_item)

        table_attributes = []
        _table_attributes = d.pop("table_attributes")
        for table_attributes_item_data in _table_attributes:
            table_attributes_item = TableAttributeSchemaOut.from_dict(table_attributes_item_data)

            table_attributes.append(table_attributes_item)

        json_attributes = []
        _json_attributes = d.pop("json_attributes")
        for json_attributes_item_data in _json_attributes:
            json_attributes_item = JSONAttributeSchemaOut.from_dict(json_attributes_item_data)

            json_attributes.append(json_attributes_item)

        all_attributes_schema_out = cls(
            string_attributes=string_attributes,
            integer_attributes=integer_attributes,
            float_attributes=float_attributes,
            boolean_attributes=boolean_attributes,
            date_attributes=date_attributes,
            datetime_attributes=datetime_attributes,
            time_attributes=time_attributes,
            coordinate_attributes=coordinate_attributes,
            polygon_attributes=polygon_attributes,
            table_attributes=table_attributes,
            json_attributes=json_attributes,
        )

        all_attributes_schema_out.additional_properties = d
        return all_attributes_schema_out

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
