from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_search_result_hit_attribute import EntitySearchResultHitAttribute


T = TypeVar("T", bound="EntitySearchResultHit")


@_attrs_define
class EntitySearchResultHit:
    """Model for each search hit

    Attributes:
        id (UUID):
        score (float):
        project_id (None | Unset | UUID): The ID of the project, if applicable
        resource_group_id (None | Unset | UUID): The ID of the resource group, if applicable
        resource_id (None | Unset | UUID): The ID of the resource, if applicable
        string_attributes (list[EntitySearchResultHitAttribute] | Unset): The string attributes of the entity
        integer_attributes (list[EntitySearchResultHitAttribute] | Unset): The integer attributes of the entity
        float_attributes (list[EntitySearchResultHitAttribute] | Unset): The float attributes of the entity
        boolean_attributes (list[EntitySearchResultHitAttribute] | Unset): The boolean attributes of the entity
        date_attributes (list[EntitySearchResultHitAttribute] | Unset): The date attributes of the entity
        datetime_attributes (list[EntitySearchResultHitAttribute] | Unset): The datetime attributes of the entity
        time_attributes (list[EntitySearchResultHitAttribute] | Unset): The time attributes of the entity
        coordinate_attributes (list[EntitySearchResultHitAttribute] | Unset): The coordinate attributes of the entity
        polygon_attributes (list[EntitySearchResultHitAttribute] | Unset): The polygon attributes of the entity
        table_attributes (list[EntitySearchResultHitAttribute] | Unset): The table attributes of the entity
    """

    id: UUID
    score: float
    project_id: None | Unset | UUID = UNSET
    resource_group_id: None | Unset | UUID = UNSET
    resource_id: None | Unset | UUID = UNSET
    string_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
    integer_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
    float_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
    boolean_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
    date_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
    datetime_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
    time_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
    coordinate_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
    polygon_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
    table_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        score = self.score

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        elif isinstance(self.project_id, UUID):
            project_id = str(self.project_id)
        else:
            project_id = self.project_id

        resource_group_id: None | str | Unset
        if isinstance(self.resource_group_id, Unset):
            resource_group_id = UNSET
        elif isinstance(self.resource_group_id, UUID):
            resource_group_id = str(self.resource_group_id)
        else:
            resource_group_id = self.resource_group_id

        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        elif isinstance(self.resource_id, UUID):
            resource_id = str(self.resource_id)
        else:
            resource_id = self.resource_id

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

        table_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.table_attributes, Unset):
            table_attributes = []
            for table_attributes_item_data in self.table_attributes:
                table_attributes_item = table_attributes_item_data.to_dict()
                table_attributes.append(table_attributes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "score": score,
            }
        )
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if resource_group_id is not UNSET:
            field_dict["resource_group_id"] = resource_group_id
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
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
        if table_attributes is not UNSET:
            field_dict["table_attributes"] = table_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_search_result_hit_attribute import EntitySearchResultHitAttribute

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        score = d.pop("score")

        def _parse_project_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                project_id_type_0 = UUID(data)

                return project_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_resource_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resource_group_id_type_0 = UUID(data)

                return resource_group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        resource_group_id = _parse_resource_group_id(d.pop("resource_group_id", UNSET))

        def _parse_resource_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resource_id_type_0 = UUID(data)

                return resource_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        resource_id = _parse_resource_id(d.pop("resource_id", UNSET))

        _string_attributes = d.pop("string_attributes", UNSET)
        string_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
        if _string_attributes is not UNSET:
            string_attributes = []
            for string_attributes_item_data in _string_attributes:
                string_attributes_item = EntitySearchResultHitAttribute.from_dict(string_attributes_item_data)

                string_attributes.append(string_attributes_item)

        _integer_attributes = d.pop("integer_attributes", UNSET)
        integer_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
        if _integer_attributes is not UNSET:
            integer_attributes = []
            for integer_attributes_item_data in _integer_attributes:
                integer_attributes_item = EntitySearchResultHitAttribute.from_dict(integer_attributes_item_data)

                integer_attributes.append(integer_attributes_item)

        _float_attributes = d.pop("float_attributes", UNSET)
        float_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
        if _float_attributes is not UNSET:
            float_attributes = []
            for float_attributes_item_data in _float_attributes:
                float_attributes_item = EntitySearchResultHitAttribute.from_dict(float_attributes_item_data)

                float_attributes.append(float_attributes_item)

        _boolean_attributes = d.pop("boolean_attributes", UNSET)
        boolean_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
        if _boolean_attributes is not UNSET:
            boolean_attributes = []
            for boolean_attributes_item_data in _boolean_attributes:
                boolean_attributes_item = EntitySearchResultHitAttribute.from_dict(boolean_attributes_item_data)

                boolean_attributes.append(boolean_attributes_item)

        _date_attributes = d.pop("date_attributes", UNSET)
        date_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
        if _date_attributes is not UNSET:
            date_attributes = []
            for date_attributes_item_data in _date_attributes:
                date_attributes_item = EntitySearchResultHitAttribute.from_dict(date_attributes_item_data)

                date_attributes.append(date_attributes_item)

        _datetime_attributes = d.pop("datetime_attributes", UNSET)
        datetime_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
        if _datetime_attributes is not UNSET:
            datetime_attributes = []
            for datetime_attributes_item_data in _datetime_attributes:
                datetime_attributes_item = EntitySearchResultHitAttribute.from_dict(datetime_attributes_item_data)

                datetime_attributes.append(datetime_attributes_item)

        _time_attributes = d.pop("time_attributes", UNSET)
        time_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
        if _time_attributes is not UNSET:
            time_attributes = []
            for time_attributes_item_data in _time_attributes:
                time_attributes_item = EntitySearchResultHitAttribute.from_dict(time_attributes_item_data)

                time_attributes.append(time_attributes_item)

        _coordinate_attributes = d.pop("coordinate_attributes", UNSET)
        coordinate_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
        if _coordinate_attributes is not UNSET:
            coordinate_attributes = []
            for coordinate_attributes_item_data in _coordinate_attributes:
                coordinate_attributes_item = EntitySearchResultHitAttribute.from_dict(coordinate_attributes_item_data)

                coordinate_attributes.append(coordinate_attributes_item)

        _polygon_attributes = d.pop("polygon_attributes", UNSET)
        polygon_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
        if _polygon_attributes is not UNSET:
            polygon_attributes = []
            for polygon_attributes_item_data in _polygon_attributes:
                polygon_attributes_item = EntitySearchResultHitAttribute.from_dict(polygon_attributes_item_data)

                polygon_attributes.append(polygon_attributes_item)

        _table_attributes = d.pop("table_attributes", UNSET)
        table_attributes: list[EntitySearchResultHitAttribute] | Unset = UNSET
        if _table_attributes is not UNSET:
            table_attributes = []
            for table_attributes_item_data in _table_attributes:
                table_attributes_item = EntitySearchResultHitAttribute.from_dict(table_attributes_item_data)

                table_attributes.append(table_attributes_item)

        entity_search_result_hit = cls(
            id=id,
            score=score,
            project_id=project_id,
            resource_group_id=resource_group_id,
            resource_id=resource_id,
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
        )

        entity_search_result_hit.additional_properties = d
        return entity_search_result_hit

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
