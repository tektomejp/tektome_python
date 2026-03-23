from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lawtalk_bool_attribute_schema import LawtalkBoolAttributeSchema
    from ..models.lawtalk_coordinate_attribute_schema import LawtalkCoordinateAttributeSchema
    from ..models.lawtalk_date_attribute_schema import LawtalkDateAttributeSchema
    from ..models.lawtalk_datetime_attribute_schema import LawtalkDatetimeAttributeSchema
    from ..models.lawtalk_float_attribute_schema import LawtalkFloatAttributeSchema
    from ..models.lawtalk_int_attribute_schema import LawtalkIntAttributeSchema
    from ..models.lawtalk_list_string_attribute_schema import LawtalkListStringAttributeSchema
    from ..models.lawtalk_string_attribute_schema import LawtalkStringAttributeSchema


T = TypeVar("T", bound="LawtalkAttributeBodyPutIn")


@_attrs_define
class LawtalkAttributeBodyPutIn:
    """
    Attributes:
        boolean_attributes (list[LawtalkBoolAttributeSchema] | Unset):
        string_attributes (list[LawtalkStringAttributeSchema] | Unset):
        integer_attributes (list[LawtalkIntAttributeSchema] | Unset):
        float_attributes (list[LawtalkFloatAttributeSchema] | Unset):
        date_attributes (list[LawtalkDateAttributeSchema] | Unset):
        datetime_attributes (list[LawtalkDatetimeAttributeSchema] | Unset):
        coordinate_attributes (list[LawtalkCoordinateAttributeSchema] | Unset):
        list_string_attributes (list[LawtalkListStringAttributeSchema] | Unset):
    """

    boolean_attributes: list[LawtalkBoolAttributeSchema] | Unset = UNSET
    string_attributes: list[LawtalkStringAttributeSchema] | Unset = UNSET
    integer_attributes: list[LawtalkIntAttributeSchema] | Unset = UNSET
    float_attributes: list[LawtalkFloatAttributeSchema] | Unset = UNSET
    date_attributes: list[LawtalkDateAttributeSchema] | Unset = UNSET
    datetime_attributes: list[LawtalkDatetimeAttributeSchema] | Unset = UNSET
    coordinate_attributes: list[LawtalkCoordinateAttributeSchema] | Unset = UNSET
    list_string_attributes: list[LawtalkListStringAttributeSchema] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        boolean_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.boolean_attributes, Unset):
            boolean_attributes = []
            for boolean_attributes_item_data in self.boolean_attributes:
                boolean_attributes_item = boolean_attributes_item_data.to_dict()
                boolean_attributes.append(boolean_attributes_item)

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

        coordinate_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.coordinate_attributes, Unset):
            coordinate_attributes = []
            for coordinate_attributes_item_data in self.coordinate_attributes:
                coordinate_attributes_item = coordinate_attributes_item_data.to_dict()
                coordinate_attributes.append(coordinate_attributes_item)

        list_string_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.list_string_attributes, Unset):
            list_string_attributes = []
            for list_string_attributes_item_data in self.list_string_attributes:
                list_string_attributes_item = list_string_attributes_item_data.to_dict()
                list_string_attributes.append(list_string_attributes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if boolean_attributes is not UNSET:
            field_dict["boolean_attributes"] = boolean_attributes
        if string_attributes is not UNSET:
            field_dict["string_attributes"] = string_attributes
        if integer_attributes is not UNSET:
            field_dict["integer_attributes"] = integer_attributes
        if float_attributes is not UNSET:
            field_dict["float_attributes"] = float_attributes
        if date_attributes is not UNSET:
            field_dict["date_attributes"] = date_attributes
        if datetime_attributes is not UNSET:
            field_dict["datetime_attributes"] = datetime_attributes
        if coordinate_attributes is not UNSET:
            field_dict["coordinate_attributes"] = coordinate_attributes
        if list_string_attributes is not UNSET:
            field_dict["list_string_attributes"] = list_string_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lawtalk_bool_attribute_schema import LawtalkBoolAttributeSchema
        from ..models.lawtalk_coordinate_attribute_schema import LawtalkCoordinateAttributeSchema
        from ..models.lawtalk_date_attribute_schema import LawtalkDateAttributeSchema
        from ..models.lawtalk_datetime_attribute_schema import LawtalkDatetimeAttributeSchema
        from ..models.lawtalk_float_attribute_schema import LawtalkFloatAttributeSchema
        from ..models.lawtalk_int_attribute_schema import LawtalkIntAttributeSchema
        from ..models.lawtalk_list_string_attribute_schema import LawtalkListStringAttributeSchema
        from ..models.lawtalk_string_attribute_schema import LawtalkStringAttributeSchema

        d = dict(src_dict)
        _boolean_attributes = d.pop("boolean_attributes", UNSET)
        boolean_attributes: list[LawtalkBoolAttributeSchema] | Unset = UNSET
        if _boolean_attributes is not UNSET:
            boolean_attributes = []
            for boolean_attributes_item_data in _boolean_attributes:
                boolean_attributes_item = LawtalkBoolAttributeSchema.from_dict(boolean_attributes_item_data)

                boolean_attributes.append(boolean_attributes_item)

        _string_attributes = d.pop("string_attributes", UNSET)
        string_attributes: list[LawtalkStringAttributeSchema] | Unset = UNSET
        if _string_attributes is not UNSET:
            string_attributes = []
            for string_attributes_item_data in _string_attributes:
                string_attributes_item = LawtalkStringAttributeSchema.from_dict(string_attributes_item_data)

                string_attributes.append(string_attributes_item)

        _integer_attributes = d.pop("integer_attributes", UNSET)
        integer_attributes: list[LawtalkIntAttributeSchema] | Unset = UNSET
        if _integer_attributes is not UNSET:
            integer_attributes = []
            for integer_attributes_item_data in _integer_attributes:
                integer_attributes_item = LawtalkIntAttributeSchema.from_dict(integer_attributes_item_data)

                integer_attributes.append(integer_attributes_item)

        _float_attributes = d.pop("float_attributes", UNSET)
        float_attributes: list[LawtalkFloatAttributeSchema] | Unset = UNSET
        if _float_attributes is not UNSET:
            float_attributes = []
            for float_attributes_item_data in _float_attributes:
                float_attributes_item = LawtalkFloatAttributeSchema.from_dict(float_attributes_item_data)

                float_attributes.append(float_attributes_item)

        _date_attributes = d.pop("date_attributes", UNSET)
        date_attributes: list[LawtalkDateAttributeSchema] | Unset = UNSET
        if _date_attributes is not UNSET:
            date_attributes = []
            for date_attributes_item_data in _date_attributes:
                date_attributes_item = LawtalkDateAttributeSchema.from_dict(date_attributes_item_data)

                date_attributes.append(date_attributes_item)

        _datetime_attributes = d.pop("datetime_attributes", UNSET)
        datetime_attributes: list[LawtalkDatetimeAttributeSchema] | Unset = UNSET
        if _datetime_attributes is not UNSET:
            datetime_attributes = []
            for datetime_attributes_item_data in _datetime_attributes:
                datetime_attributes_item = LawtalkDatetimeAttributeSchema.from_dict(datetime_attributes_item_data)

                datetime_attributes.append(datetime_attributes_item)

        _coordinate_attributes = d.pop("coordinate_attributes", UNSET)
        coordinate_attributes: list[LawtalkCoordinateAttributeSchema] | Unset = UNSET
        if _coordinate_attributes is not UNSET:
            coordinate_attributes = []
            for coordinate_attributes_item_data in _coordinate_attributes:
                coordinate_attributes_item = LawtalkCoordinateAttributeSchema.from_dict(coordinate_attributes_item_data)

                coordinate_attributes.append(coordinate_attributes_item)

        _list_string_attributes = d.pop("list_string_attributes", UNSET)
        list_string_attributes: list[LawtalkListStringAttributeSchema] | Unset = UNSET
        if _list_string_attributes is not UNSET:
            list_string_attributes = []
            for list_string_attributes_item_data in _list_string_attributes:
                list_string_attributes_item = LawtalkListStringAttributeSchema.from_dict(
                    list_string_attributes_item_data
                )

                list_string_attributes.append(list_string_attributes_item)

        lawtalk_attribute_body_put_in = cls(
            boolean_attributes=boolean_attributes,
            string_attributes=string_attributes,
            integer_attributes=integer_attributes,
            float_attributes=float_attributes,
            date_attributes=date_attributes,
            datetime_attributes=datetime_attributes,
            coordinate_attributes=coordinate_attributes,
            list_string_attributes=list_string_attributes,
        )

        lawtalk_attribute_body_put_in.additional_properties = d
        return lawtalk_attribute_body_put_in

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
