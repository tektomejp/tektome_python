from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.any_attribute_schema_request import AnyAttributeSchemaRequest
    from ..models.boolean_attribute_schema_request import BooleanAttributeSchemaRequest
    from ..models.coordinate_attribute_schema_request import CoordinateAttributeSchemaRequest
    from ..models.date_attribute_schema_request import DateAttributeSchemaRequest
    from ..models.date_time_attribute_schema_request import DateTimeAttributeSchemaRequest
    from ..models.float_attribute_schema_request import FloatAttributeSchemaRequest
    from ..models.integer_attribute_schema_request import IntegerAttributeSchemaRequest
    from ..models.json_attribute_schema_request import JSONAttributeSchemaRequest
    from ..models.multi_select_attribute_schema_request import MultiSelectAttributeSchemaRequest
    from ..models.polygon_attribute_schema_request import PolygonAttributeSchemaRequest
    from ..models.single_select_attribute_schema_request import SingleSelectAttributeSchemaRequest
    from ..models.string_attribute_schema_request import StringAttributeSchemaRequest
    from ..models.time_attribute_schema_request import TimeAttributeSchemaRequest


T = TypeVar("T", bound="ReplaceLawtalkGeneralAttributeBodyRequest")


@_attrs_define
class ReplaceLawtalkGeneralAttributeBodyRequest:
    """
    Attributes:
        string_attributes (list[StringAttributeSchemaRequest] | Unset):
        integer_attributes (list[IntegerAttributeSchemaRequest] | Unset):
        float_attributes (list[FloatAttributeSchemaRequest] | Unset):
        boolean_attributes (list[BooleanAttributeSchemaRequest] | Unset):
        date_attributes (list[DateAttributeSchemaRequest] | Unset):
        datetime_attributes (list[DateTimeAttributeSchemaRequest] | Unset):
        time_attributes (list[TimeAttributeSchemaRequest] | Unset):
        coordinate_attributes (list[CoordinateAttributeSchemaRequest] | Unset):
        polygon_attributes (list[PolygonAttributeSchemaRequest] | Unset):
        list_object_attributes (list[AnyAttributeSchemaRequest] | Unset):
        json_attributes (list[JSONAttributeSchemaRequest] | Unset):
        single_select_attributes (list[SingleSelectAttributeSchemaRequest] | Unset):
        multi_select_attributes (list[MultiSelectAttributeSchemaRequest] | Unset):
        table_attributes (list[AnyAttributeSchemaRequest] | Unset):
    """

    string_attributes: list[StringAttributeSchemaRequest] | Unset = UNSET
    integer_attributes: list[IntegerAttributeSchemaRequest] | Unset = UNSET
    float_attributes: list[FloatAttributeSchemaRequest] | Unset = UNSET
    boolean_attributes: list[BooleanAttributeSchemaRequest] | Unset = UNSET
    date_attributes: list[DateAttributeSchemaRequest] | Unset = UNSET
    datetime_attributes: list[DateTimeAttributeSchemaRequest] | Unset = UNSET
    time_attributes: list[TimeAttributeSchemaRequest] | Unset = UNSET
    coordinate_attributes: list[CoordinateAttributeSchemaRequest] | Unset = UNSET
    polygon_attributes: list[PolygonAttributeSchemaRequest] | Unset = UNSET
    list_object_attributes: list[AnyAttributeSchemaRequest] | Unset = UNSET
    json_attributes: list[JSONAttributeSchemaRequest] | Unset = UNSET
    single_select_attributes: list[SingleSelectAttributeSchemaRequest] | Unset = UNSET
    multi_select_attributes: list[MultiSelectAttributeSchemaRequest] | Unset = UNSET
    table_attributes: list[AnyAttributeSchemaRequest] | Unset = UNSET
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
        from ..models.any_attribute_schema_request import AnyAttributeSchemaRequest
        from ..models.boolean_attribute_schema_request import BooleanAttributeSchemaRequest
        from ..models.coordinate_attribute_schema_request import CoordinateAttributeSchemaRequest
        from ..models.date_attribute_schema_request import DateAttributeSchemaRequest
        from ..models.date_time_attribute_schema_request import DateTimeAttributeSchemaRequest
        from ..models.float_attribute_schema_request import FloatAttributeSchemaRequest
        from ..models.integer_attribute_schema_request import IntegerAttributeSchemaRequest
        from ..models.json_attribute_schema_request import JSONAttributeSchemaRequest
        from ..models.multi_select_attribute_schema_request import MultiSelectAttributeSchemaRequest
        from ..models.polygon_attribute_schema_request import PolygonAttributeSchemaRequest
        from ..models.single_select_attribute_schema_request import SingleSelectAttributeSchemaRequest
        from ..models.string_attribute_schema_request import StringAttributeSchemaRequest
        from ..models.time_attribute_schema_request import TimeAttributeSchemaRequest

        d = dict(src_dict)
        _string_attributes = d.pop("string_attributes", UNSET)
        string_attributes: list[StringAttributeSchemaRequest] | Unset = UNSET
        if _string_attributes is not UNSET:
            string_attributes = []
            for string_attributes_item_data in _string_attributes:
                string_attributes_item = StringAttributeSchemaRequest.from_dict(string_attributes_item_data)

                string_attributes.append(string_attributes_item)

        _integer_attributes = d.pop("integer_attributes", UNSET)
        integer_attributes: list[IntegerAttributeSchemaRequest] | Unset = UNSET
        if _integer_attributes is not UNSET:
            integer_attributes = []
            for integer_attributes_item_data in _integer_attributes:
                integer_attributes_item = IntegerAttributeSchemaRequest.from_dict(integer_attributes_item_data)

                integer_attributes.append(integer_attributes_item)

        _float_attributes = d.pop("float_attributes", UNSET)
        float_attributes: list[FloatAttributeSchemaRequest] | Unset = UNSET
        if _float_attributes is not UNSET:
            float_attributes = []
            for float_attributes_item_data in _float_attributes:
                float_attributes_item = FloatAttributeSchemaRequest.from_dict(float_attributes_item_data)

                float_attributes.append(float_attributes_item)

        _boolean_attributes = d.pop("boolean_attributes", UNSET)
        boolean_attributes: list[BooleanAttributeSchemaRequest] | Unset = UNSET
        if _boolean_attributes is not UNSET:
            boolean_attributes = []
            for boolean_attributes_item_data in _boolean_attributes:
                boolean_attributes_item = BooleanAttributeSchemaRequest.from_dict(boolean_attributes_item_data)

                boolean_attributes.append(boolean_attributes_item)

        _date_attributes = d.pop("date_attributes", UNSET)
        date_attributes: list[DateAttributeSchemaRequest] | Unset = UNSET
        if _date_attributes is not UNSET:
            date_attributes = []
            for date_attributes_item_data in _date_attributes:
                date_attributes_item = DateAttributeSchemaRequest.from_dict(date_attributes_item_data)

                date_attributes.append(date_attributes_item)

        _datetime_attributes = d.pop("datetime_attributes", UNSET)
        datetime_attributes: list[DateTimeAttributeSchemaRequest] | Unset = UNSET
        if _datetime_attributes is not UNSET:
            datetime_attributes = []
            for datetime_attributes_item_data in _datetime_attributes:
                datetime_attributes_item = DateTimeAttributeSchemaRequest.from_dict(datetime_attributes_item_data)

                datetime_attributes.append(datetime_attributes_item)

        _time_attributes = d.pop("time_attributes", UNSET)
        time_attributes: list[TimeAttributeSchemaRequest] | Unset = UNSET
        if _time_attributes is not UNSET:
            time_attributes = []
            for time_attributes_item_data in _time_attributes:
                time_attributes_item = TimeAttributeSchemaRequest.from_dict(time_attributes_item_data)

                time_attributes.append(time_attributes_item)

        _coordinate_attributes = d.pop("coordinate_attributes", UNSET)
        coordinate_attributes: list[CoordinateAttributeSchemaRequest] | Unset = UNSET
        if _coordinate_attributes is not UNSET:
            coordinate_attributes = []
            for coordinate_attributes_item_data in _coordinate_attributes:
                coordinate_attributes_item = CoordinateAttributeSchemaRequest.from_dict(coordinate_attributes_item_data)

                coordinate_attributes.append(coordinate_attributes_item)

        _polygon_attributes = d.pop("polygon_attributes", UNSET)
        polygon_attributes: list[PolygonAttributeSchemaRequest] | Unset = UNSET
        if _polygon_attributes is not UNSET:
            polygon_attributes = []
            for polygon_attributes_item_data in _polygon_attributes:
                polygon_attributes_item = PolygonAttributeSchemaRequest.from_dict(polygon_attributes_item_data)

                polygon_attributes.append(polygon_attributes_item)

        _list_object_attributes = d.pop("list_object_attributes", UNSET)
        list_object_attributes: list[AnyAttributeSchemaRequest] | Unset = UNSET
        if _list_object_attributes is not UNSET:
            list_object_attributes = []
            for list_object_attributes_item_data in _list_object_attributes:
                list_object_attributes_item = AnyAttributeSchemaRequest.from_dict(list_object_attributes_item_data)

                list_object_attributes.append(list_object_attributes_item)

        _json_attributes = d.pop("json_attributes", UNSET)
        json_attributes: list[JSONAttributeSchemaRequest] | Unset = UNSET
        if _json_attributes is not UNSET:
            json_attributes = []
            for json_attributes_item_data in _json_attributes:
                json_attributes_item = JSONAttributeSchemaRequest.from_dict(json_attributes_item_data)

                json_attributes.append(json_attributes_item)

        _single_select_attributes = d.pop("single_select_attributes", UNSET)
        single_select_attributes: list[SingleSelectAttributeSchemaRequest] | Unset = UNSET
        if _single_select_attributes is not UNSET:
            single_select_attributes = []
            for single_select_attributes_item_data in _single_select_attributes:
                single_select_attributes_item = SingleSelectAttributeSchemaRequest.from_dict(
                    single_select_attributes_item_data
                )

                single_select_attributes.append(single_select_attributes_item)

        _multi_select_attributes = d.pop("multi_select_attributes", UNSET)
        multi_select_attributes: list[MultiSelectAttributeSchemaRequest] | Unset = UNSET
        if _multi_select_attributes is not UNSET:
            multi_select_attributes = []
            for multi_select_attributes_item_data in _multi_select_attributes:
                multi_select_attributes_item = MultiSelectAttributeSchemaRequest.from_dict(
                    multi_select_attributes_item_data
                )

                multi_select_attributes.append(multi_select_attributes_item)

        _table_attributes = d.pop("table_attributes", UNSET)
        table_attributes: list[AnyAttributeSchemaRequest] | Unset = UNSET
        if _table_attributes is not UNSET:
            table_attributes = []
            for table_attributes_item_data in _table_attributes:
                table_attributes_item = AnyAttributeSchemaRequest.from_dict(table_attributes_item_data)

                table_attributes.append(table_attributes_item)

        replace_lawtalk_general_attribute_body_request = cls(
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

        replace_lawtalk_general_attribute_body_request.additional_properties = d
        return replace_lawtalk_general_attribute_body_request

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
