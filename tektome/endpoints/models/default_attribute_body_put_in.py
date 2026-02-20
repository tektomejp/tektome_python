from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.any_attribute_schema_in import AnyAttributeSchemaIn
    from ..models.boolean_attribute_schema_in import BooleanAttributeSchemaIn
    from ..models.coordinate_attribute_schema_in import CoordinateAttributeSchemaIn
    from ..models.date_attribute_schema_in import DateAttributeSchemaIn
    from ..models.date_time_attribute_schema_in import DateTimeAttributeSchemaIn
    from ..models.float_attribute_schema_in import FloatAttributeSchemaIn
    from ..models.integer_attribute_schema_in import IntegerAttributeSchemaIn
    from ..models.json_attribute_schema_in import JSONAttributeSchemaIn
    from ..models.multi_select_attribute_schema_in import MultiSelectAttributeSchemaIn
    from ..models.polygon_attribute_schema_in import PolygonAttributeSchemaIn
    from ..models.single_select_attribute_schema_in import SingleSelectAttributeSchemaIn
    from ..models.string_attribute_schema_in import StringAttributeSchemaIn
    from ..models.time_attribute_schema_in import TimeAttributeSchemaIn


T = TypeVar("T", bound="DefaultAttributeBodyPutIn")


@_attrs_define
class DefaultAttributeBodyPutIn:
    """
    Attributes:
        string_attributes (list[StringAttributeSchemaIn] | Unset):
        integer_attributes (list[IntegerAttributeSchemaIn] | Unset):
        float_attributes (list[FloatAttributeSchemaIn] | Unset):
        boolean_attributes (list[BooleanAttributeSchemaIn] | Unset):
        date_attributes (list[DateAttributeSchemaIn] | Unset):
        datetime_attributes (list[DateTimeAttributeSchemaIn] | Unset):
        time_attributes (list[TimeAttributeSchemaIn] | Unset):
        coordinate_attributes (list[CoordinateAttributeSchemaIn] | Unset):
        polygon_attributes (list[PolygonAttributeSchemaIn] | Unset):
        list_object_attributes (list[AnyAttributeSchemaIn] | Unset):
        json_attributes (list[JSONAttributeSchemaIn] | Unset):
        single_select_attributes (list[SingleSelectAttributeSchemaIn] | Unset):
        multi_select_attributes (list[MultiSelectAttributeSchemaIn] | Unset):
        table_attributes (list[AnyAttributeSchemaIn] | Unset):
    """

    string_attributes: list[StringAttributeSchemaIn] | Unset = UNSET
    integer_attributes: list[IntegerAttributeSchemaIn] | Unset = UNSET
    float_attributes: list[FloatAttributeSchemaIn] | Unset = UNSET
    boolean_attributes: list[BooleanAttributeSchemaIn] | Unset = UNSET
    date_attributes: list[DateAttributeSchemaIn] | Unset = UNSET
    datetime_attributes: list[DateTimeAttributeSchemaIn] | Unset = UNSET
    time_attributes: list[TimeAttributeSchemaIn] | Unset = UNSET
    coordinate_attributes: list[CoordinateAttributeSchemaIn] | Unset = UNSET
    polygon_attributes: list[PolygonAttributeSchemaIn] | Unset = UNSET
    list_object_attributes: list[AnyAttributeSchemaIn] | Unset = UNSET
    json_attributes: list[JSONAttributeSchemaIn] | Unset = UNSET
    single_select_attributes: list[SingleSelectAttributeSchemaIn] | Unset = UNSET
    multi_select_attributes: list[MultiSelectAttributeSchemaIn] | Unset = UNSET
    table_attributes: list[AnyAttributeSchemaIn] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        string_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.string_attributes, Unset):
            string_attributes = []
            for string_attributes_item_data in self.string_attributes:
                string_attributes_item = string_attributes_item_data.to_dict()
                string_attributes.append(string_attributes_item)

        integer_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.integer_attributes, Unset):
            integer_attributes = []
            for integer_attributes_item_data in self.integer_attributes:
                integer_attributes_item = integer_attributes_item_data.to_dict()
                integer_attributes.append(integer_attributes_item)

        float_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.float_attributes, Unset):
            float_attributes = []
            for float_attributes_item_data in self.float_attributes:
                float_attributes_item = float_attributes_item_data.to_dict()
                float_attributes.append(float_attributes_item)

        boolean_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.boolean_attributes, Unset):
            boolean_attributes = []
            for boolean_attributes_item_data in self.boolean_attributes:
                boolean_attributes_item = boolean_attributes_item_data.to_dict()
                boolean_attributes.append(boolean_attributes_item)

        date_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.date_attributes, Unset):
            date_attributes = []
            for date_attributes_item_data in self.date_attributes:
                date_attributes_item = date_attributes_item_data.to_dict()
                date_attributes.append(date_attributes_item)

        datetime_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.datetime_attributes, Unset):
            datetime_attributes = []
            for datetime_attributes_item_data in self.datetime_attributes:
                datetime_attributes_item = datetime_attributes_item_data.to_dict()
                datetime_attributes.append(datetime_attributes_item)

        time_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.time_attributes, Unset):
            time_attributes = []
            for time_attributes_item_data in self.time_attributes:
                time_attributes_item = time_attributes_item_data.to_dict()
                time_attributes.append(time_attributes_item)

        coordinate_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.coordinate_attributes, Unset):
            coordinate_attributes = []
            for coordinate_attributes_item_data in self.coordinate_attributes:
                coordinate_attributes_item = coordinate_attributes_item_data.to_dict()
                coordinate_attributes.append(coordinate_attributes_item)

        polygon_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.polygon_attributes, Unset):
            polygon_attributes = []
            for polygon_attributes_item_data in self.polygon_attributes:
                polygon_attributes_item = polygon_attributes_item_data.to_dict()
                polygon_attributes.append(polygon_attributes_item)

        list_object_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.list_object_attributes, Unset):
            list_object_attributes = []
            for list_object_attributes_item_data in self.list_object_attributes:
                list_object_attributes_item = list_object_attributes_item_data.to_dict()
                list_object_attributes.append(list_object_attributes_item)

        json_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.json_attributes, Unset):
            json_attributes = []
            for json_attributes_item_data in self.json_attributes:
                json_attributes_item = json_attributes_item_data.to_dict()
                json_attributes.append(json_attributes_item)

        single_select_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.single_select_attributes, Unset):
            single_select_attributes = []
            for single_select_attributes_item_data in self.single_select_attributes:
                single_select_attributes_item = single_select_attributes_item_data.to_dict()
                single_select_attributes.append(single_select_attributes_item)

        multi_select_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.multi_select_attributes, Unset):
            multi_select_attributes = []
            for multi_select_attributes_item_data in self.multi_select_attributes:
                multi_select_attributes_item = multi_select_attributes_item_data.to_dict()
                multi_select_attributes.append(multi_select_attributes_item)

        table_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.table_attributes, Unset):
            table_attributes = []
            for table_attributes_item_data in self.table_attributes:
                table_attributes_item = table_attributes_item_data.to_dict()
                table_attributes.append(table_attributes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if string_attributes is not UNSET:
            field_dict["string_attributes"] = string_attributes
        if integer_attributes is not UNSET:
            field_dict["integer_attributes"] = integer_attributes
        if float_attributes is not UNSET:
            field_dict["float_attributes"] = float_attributes
        if boolean_attributes is not UNSET:
            field_dict["boolean_attributes"] = boolean_attributes
        if date_attributes is not UNSET:
            field_dict["date_attributes"] = date_attributes
        if datetime_attributes is not UNSET:
            field_dict["datetime_attributes"] = datetime_attributes
        if time_attributes is not UNSET:
            field_dict["time_attributes"] = time_attributes
        if coordinate_attributes is not UNSET:
            field_dict["coordinate_attributes"] = coordinate_attributes
        if polygon_attributes is not UNSET:
            field_dict["polygon_attributes"] = polygon_attributes
        if list_object_attributes is not UNSET:
            field_dict["list_object_attributes"] = list_object_attributes
        if json_attributes is not UNSET:
            field_dict["json_attributes"] = json_attributes
        if single_select_attributes is not UNSET:
            field_dict["single_select_attributes"] = single_select_attributes
        if multi_select_attributes is not UNSET:
            field_dict["multi_select_attributes"] = multi_select_attributes
        if table_attributes is not UNSET:
            field_dict["table_attributes"] = table_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.any_attribute_schema_in import AnyAttributeSchemaIn
        from ..models.boolean_attribute_schema_in import BooleanAttributeSchemaIn
        from ..models.coordinate_attribute_schema_in import CoordinateAttributeSchemaIn
        from ..models.date_attribute_schema_in import DateAttributeSchemaIn
        from ..models.date_time_attribute_schema_in import DateTimeAttributeSchemaIn
        from ..models.float_attribute_schema_in import FloatAttributeSchemaIn
        from ..models.integer_attribute_schema_in import IntegerAttributeSchemaIn
        from ..models.json_attribute_schema_in import JSONAttributeSchemaIn
        from ..models.multi_select_attribute_schema_in import MultiSelectAttributeSchemaIn
        from ..models.polygon_attribute_schema_in import PolygonAttributeSchemaIn
        from ..models.single_select_attribute_schema_in import SingleSelectAttributeSchemaIn
        from ..models.string_attribute_schema_in import StringAttributeSchemaIn
        from ..models.time_attribute_schema_in import TimeAttributeSchemaIn

        d = dict(src_dict)
        _string_attributes = d.pop("string_attributes", UNSET)
        string_attributes: list[StringAttributeSchemaIn] | Unset = UNSET
        if _string_attributes is not UNSET:
            string_attributes = []
            for string_attributes_item_data in _string_attributes:
                string_attributes_item = StringAttributeSchemaIn.from_dict(string_attributes_item_data)

                string_attributes.append(string_attributes_item)

        _integer_attributes = d.pop("integer_attributes", UNSET)
        integer_attributes: list[IntegerAttributeSchemaIn] | Unset = UNSET
        if _integer_attributes is not UNSET:
            integer_attributes = []
            for integer_attributes_item_data in _integer_attributes:
                integer_attributes_item = IntegerAttributeSchemaIn.from_dict(integer_attributes_item_data)

                integer_attributes.append(integer_attributes_item)

        _float_attributes = d.pop("float_attributes", UNSET)
        float_attributes: list[FloatAttributeSchemaIn] | Unset = UNSET
        if _float_attributes is not UNSET:
            float_attributes = []
            for float_attributes_item_data in _float_attributes:
                float_attributes_item = FloatAttributeSchemaIn.from_dict(float_attributes_item_data)

                float_attributes.append(float_attributes_item)

        _boolean_attributes = d.pop("boolean_attributes", UNSET)
        boolean_attributes: list[BooleanAttributeSchemaIn] | Unset = UNSET
        if _boolean_attributes is not UNSET:
            boolean_attributes = []
            for boolean_attributes_item_data in _boolean_attributes:
                boolean_attributes_item = BooleanAttributeSchemaIn.from_dict(boolean_attributes_item_data)

                boolean_attributes.append(boolean_attributes_item)

        _date_attributes = d.pop("date_attributes", UNSET)
        date_attributes: list[DateAttributeSchemaIn] | Unset = UNSET
        if _date_attributes is not UNSET:
            date_attributes = []
            for date_attributes_item_data in _date_attributes:
                date_attributes_item = DateAttributeSchemaIn.from_dict(date_attributes_item_data)

                date_attributes.append(date_attributes_item)

        _datetime_attributes = d.pop("datetime_attributes", UNSET)
        datetime_attributes: list[DateTimeAttributeSchemaIn] | Unset = UNSET
        if _datetime_attributes is not UNSET:
            datetime_attributes = []
            for datetime_attributes_item_data in _datetime_attributes:
                datetime_attributes_item = DateTimeAttributeSchemaIn.from_dict(datetime_attributes_item_data)

                datetime_attributes.append(datetime_attributes_item)

        _time_attributes = d.pop("time_attributes", UNSET)
        time_attributes: list[TimeAttributeSchemaIn] | Unset = UNSET
        if _time_attributes is not UNSET:
            time_attributes = []
            for time_attributes_item_data in _time_attributes:
                time_attributes_item = TimeAttributeSchemaIn.from_dict(time_attributes_item_data)

                time_attributes.append(time_attributes_item)

        _coordinate_attributes = d.pop("coordinate_attributes", UNSET)
        coordinate_attributes: list[CoordinateAttributeSchemaIn] | Unset = UNSET
        if _coordinate_attributes is not UNSET:
            coordinate_attributes = []
            for coordinate_attributes_item_data in _coordinate_attributes:
                coordinate_attributes_item = CoordinateAttributeSchemaIn.from_dict(coordinate_attributes_item_data)

                coordinate_attributes.append(coordinate_attributes_item)

        _polygon_attributes = d.pop("polygon_attributes", UNSET)
        polygon_attributes: list[PolygonAttributeSchemaIn] | Unset = UNSET
        if _polygon_attributes is not UNSET:
            polygon_attributes = []
            for polygon_attributes_item_data in _polygon_attributes:
                polygon_attributes_item = PolygonAttributeSchemaIn.from_dict(polygon_attributes_item_data)

                polygon_attributes.append(polygon_attributes_item)

        _list_object_attributes = d.pop("list_object_attributes", UNSET)
        list_object_attributes: list[AnyAttributeSchemaIn] | Unset = UNSET
        if _list_object_attributes is not UNSET:
            list_object_attributes = []
            for list_object_attributes_item_data in _list_object_attributes:
                list_object_attributes_item = AnyAttributeSchemaIn.from_dict(list_object_attributes_item_data)

                list_object_attributes.append(list_object_attributes_item)

        _json_attributes = d.pop("json_attributes", UNSET)
        json_attributes: list[JSONAttributeSchemaIn] | Unset = UNSET
        if _json_attributes is not UNSET:
            json_attributes = []
            for json_attributes_item_data in _json_attributes:
                json_attributes_item = JSONAttributeSchemaIn.from_dict(json_attributes_item_data)

                json_attributes.append(json_attributes_item)

        _single_select_attributes = d.pop("single_select_attributes", UNSET)
        single_select_attributes: list[SingleSelectAttributeSchemaIn] | Unset = UNSET
        if _single_select_attributes is not UNSET:
            single_select_attributes = []
            for single_select_attributes_item_data in _single_select_attributes:
                single_select_attributes_item = SingleSelectAttributeSchemaIn.from_dict(
                    single_select_attributes_item_data
                )

                single_select_attributes.append(single_select_attributes_item)

        _multi_select_attributes = d.pop("multi_select_attributes", UNSET)
        multi_select_attributes: list[MultiSelectAttributeSchemaIn] | Unset = UNSET
        if _multi_select_attributes is not UNSET:
            multi_select_attributes = []
            for multi_select_attributes_item_data in _multi_select_attributes:
                multi_select_attributes_item = MultiSelectAttributeSchemaIn.from_dict(multi_select_attributes_item_data)

                multi_select_attributes.append(multi_select_attributes_item)

        _table_attributes = d.pop("table_attributes", UNSET)
        table_attributes: list[AnyAttributeSchemaIn] | Unset = UNSET
        if _table_attributes is not UNSET:
            table_attributes = []
            for table_attributes_item_data in _table_attributes:
                table_attributes_item = AnyAttributeSchemaIn.from_dict(table_attributes_item_data)

                table_attributes.append(table_attributes_item)

        default_attribute_body_put_in = cls(
            string_attributes=string_attributes,
            integer_attributes=integer_attributes,
            float_attributes=float_attributes,
            boolean_attributes=boolean_attributes,
            date_attributes=date_attributes,
            datetime_attributes=datetime_attributes,
            time_attributes=time_attributes,
            coordinate_attributes=coordinate_attributes,
            polygon_attributes=polygon_attributes,
            list_object_attributes=list_object_attributes,
            json_attributes=json_attributes,
            single_select_attributes=single_select_attributes,
            multi_select_attributes=multi_select_attributes,
            table_attributes=table_attributes,
        )

        default_attribute_body_put_in.additional_properties = d
        return default_attribute_body_put_in

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
