from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.boolean_search_condition import BooleanSearchCondition
    from ..models.date_search_condition import DateSearchCondition
    from ..models.date_time_search_condition import DateTimeSearchCondition
    from ..models.dynamic_boolean_search_condition import DynamicBooleanSearchCondition
    from ..models.dynamic_date_search_condition import DynamicDateSearchCondition
    from ..models.dynamic_date_time_search_condition import DynamicDateTimeSearchCondition
    from ..models.dynamic_float_search_condition import DynamicFloatSearchCondition
    from ..models.dynamic_integer_search_condition import DynamicIntegerSearchCondition
    from ..models.dynamic_string_search_condition import DynamicStringSearchCondition
    from ..models.dynamic_table_search_condition import DynamicTableSearchCondition
    from ..models.dynamic_time_search_condition import DynamicTimeSearchCondition
    from ..models.float_search_condition import FloatSearchCondition
    from ..models.integer_search_condition import IntegerSearchCondition
    from ..models.string_search_condition import StringSearchCondition
    from ..models.table_search_condition import TableSearchCondition
    from ..models.time_search_condition import TimeSearchCondition


T = TypeVar("T", bound="DynamicEntitySearchRequest")


@_attrs_define
class DynamicEntitySearchRequest:
    """Search request for entity searches with dynamic conditions.

    Attributes:
        project (list[BooleanSearchCondition | DateSearchCondition | DateTimeSearchCondition |
            DynamicBooleanSearchCondition | DynamicDateSearchCondition | DynamicDateTimeSearchCondition |
            DynamicFloatSearchCondition | DynamicIntegerSearchCondition | DynamicStringSearchCondition |
            DynamicTableSearchCondition | DynamicTimeSearchCondition | FloatSearchCondition | IntegerSearchCondition |
            StringSearchCondition | TableSearchCondition | TimeSearchCondition] | Unset): The search condition for the
            project
        resource_group (list[BooleanSearchCondition | DateSearchCondition | DateTimeSearchCondition |
            DynamicBooleanSearchCondition | DynamicDateSearchCondition | DynamicDateTimeSearchCondition |
            DynamicFloatSearchCondition | DynamicIntegerSearchCondition | DynamicStringSearchCondition |
            DynamicTableSearchCondition | DynamicTimeSearchCondition | FloatSearchCondition | IntegerSearchCondition |
            StringSearchCondition | TableSearchCondition | TimeSearchCondition] | Unset): The search condition for the
            resource group
        resource (list[BooleanSearchCondition | DateSearchCondition | DateTimeSearchCondition |
            DynamicBooleanSearchCondition | DynamicDateSearchCondition | DynamicDateTimeSearchCondition |
            DynamicFloatSearchCondition | DynamicIntegerSearchCondition | DynamicStringSearchCondition |
            DynamicTableSearchCondition | DynamicTimeSearchCondition | FloatSearchCondition | IntegerSearchCondition |
            StringSearchCondition | TableSearchCondition | TimeSearchCondition] | Unset): The search condition for the
            subscription
    """

    project: (
        list[
            BooleanSearchCondition
            | DateSearchCondition
            | DateTimeSearchCondition
            | DynamicBooleanSearchCondition
            | DynamicDateSearchCondition
            | DynamicDateTimeSearchCondition
            | DynamicFloatSearchCondition
            | DynamicIntegerSearchCondition
            | DynamicStringSearchCondition
            | DynamicTableSearchCondition
            | DynamicTimeSearchCondition
            | FloatSearchCondition
            | IntegerSearchCondition
            | StringSearchCondition
            | TableSearchCondition
            | TimeSearchCondition
        ]
        | Unset
    ) = UNSET
    resource_group: (
        list[
            BooleanSearchCondition
            | DateSearchCondition
            | DateTimeSearchCondition
            | DynamicBooleanSearchCondition
            | DynamicDateSearchCondition
            | DynamicDateTimeSearchCondition
            | DynamicFloatSearchCondition
            | DynamicIntegerSearchCondition
            | DynamicStringSearchCondition
            | DynamicTableSearchCondition
            | DynamicTimeSearchCondition
            | FloatSearchCondition
            | IntegerSearchCondition
            | StringSearchCondition
            | TableSearchCondition
            | TimeSearchCondition
        ]
        | Unset
    ) = UNSET
    resource: (
        list[
            BooleanSearchCondition
            | DateSearchCondition
            | DateTimeSearchCondition
            | DynamicBooleanSearchCondition
            | DynamicDateSearchCondition
            | DynamicDateTimeSearchCondition
            | DynamicFloatSearchCondition
            | DynamicIntegerSearchCondition
            | DynamicStringSearchCondition
            | DynamicTableSearchCondition
            | DynamicTimeSearchCondition
            | FloatSearchCondition
            | IntegerSearchCondition
            | StringSearchCondition
            | TableSearchCondition
            | TimeSearchCondition
        ]
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.boolean_search_condition import BooleanSearchCondition
        from ..models.date_search_condition import DateSearchCondition
        from ..models.date_time_search_condition import DateTimeSearchCondition
        from ..models.dynamic_boolean_search_condition import DynamicBooleanSearchCondition
        from ..models.dynamic_date_search_condition import DynamicDateSearchCondition
        from ..models.dynamic_date_time_search_condition import DynamicDateTimeSearchCondition
        from ..models.dynamic_float_search_condition import DynamicFloatSearchCondition
        from ..models.dynamic_integer_search_condition import DynamicIntegerSearchCondition
        from ..models.dynamic_string_search_condition import DynamicStringSearchCondition
        from ..models.dynamic_time_search_condition import DynamicTimeSearchCondition
        from ..models.float_search_condition import FloatSearchCondition
        from ..models.integer_search_condition import IntegerSearchCondition
        from ..models.string_search_condition import StringSearchCondition
        from ..models.table_search_condition import TableSearchCondition
        from ..models.time_search_condition import TimeSearchCondition

        project: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = []
            for project_item_data in self.project:
                project_item: dict[str, Any]
                if isinstance(project_item_data, StringSearchCondition):
                    project_item = project_item_data.to_dict()
                elif isinstance(project_item_data, IntegerSearchCondition):
                    project_item = project_item_data.to_dict()
                elif isinstance(project_item_data, FloatSearchCondition):
                    project_item = project_item_data.to_dict()
                elif isinstance(project_item_data, BooleanSearchCondition):
                    project_item = project_item_data.to_dict()
                elif isinstance(project_item_data, DateSearchCondition):
                    project_item = project_item_data.to_dict()
                elif isinstance(project_item_data, DateTimeSearchCondition):
                    project_item = project_item_data.to_dict()
                elif isinstance(project_item_data, TimeSearchCondition):
                    project_item = project_item_data.to_dict()
                elif isinstance(project_item_data, TableSearchCondition):
                    project_item = project_item_data.to_dict()
                elif isinstance(project_item_data, DynamicStringSearchCondition):
                    project_item = project_item_data.to_dict()
                elif isinstance(project_item_data, DynamicIntegerSearchCondition):
                    project_item = project_item_data.to_dict()
                elif isinstance(project_item_data, DynamicFloatSearchCondition):
                    project_item = project_item_data.to_dict()
                elif isinstance(project_item_data, DynamicBooleanSearchCondition):
                    project_item = project_item_data.to_dict()
                elif isinstance(project_item_data, DynamicDateSearchCondition):
                    project_item = project_item_data.to_dict()
                elif isinstance(project_item_data, DynamicDateTimeSearchCondition):
                    project_item = project_item_data.to_dict()
                elif isinstance(project_item_data, DynamicTimeSearchCondition):
                    project_item = project_item_data.to_dict()
                else:
                    project_item = project_item_data.to_dict()

                project.append(project_item)

        resource_group: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resource_group, Unset):
            resource_group = []
            for resource_group_item_data in self.resource_group:
                resource_group_item: dict[str, Any]
                if isinstance(resource_group_item_data, StringSearchCondition):
                    resource_group_item = resource_group_item_data.to_dict()
                elif isinstance(resource_group_item_data, IntegerSearchCondition):
                    resource_group_item = resource_group_item_data.to_dict()
                elif isinstance(resource_group_item_data, FloatSearchCondition):
                    resource_group_item = resource_group_item_data.to_dict()
                elif isinstance(resource_group_item_data, BooleanSearchCondition):
                    resource_group_item = resource_group_item_data.to_dict()
                elif isinstance(resource_group_item_data, DateSearchCondition):
                    resource_group_item = resource_group_item_data.to_dict()
                elif isinstance(resource_group_item_data, DateTimeSearchCondition):
                    resource_group_item = resource_group_item_data.to_dict()
                elif isinstance(resource_group_item_data, TimeSearchCondition):
                    resource_group_item = resource_group_item_data.to_dict()
                elif isinstance(resource_group_item_data, TableSearchCondition):
                    resource_group_item = resource_group_item_data.to_dict()
                elif isinstance(resource_group_item_data, DynamicStringSearchCondition):
                    resource_group_item = resource_group_item_data.to_dict()
                elif isinstance(resource_group_item_data, DynamicIntegerSearchCondition):
                    resource_group_item = resource_group_item_data.to_dict()
                elif isinstance(resource_group_item_data, DynamicFloatSearchCondition):
                    resource_group_item = resource_group_item_data.to_dict()
                elif isinstance(resource_group_item_data, DynamicBooleanSearchCondition):
                    resource_group_item = resource_group_item_data.to_dict()
                elif isinstance(resource_group_item_data, DynamicDateSearchCondition):
                    resource_group_item = resource_group_item_data.to_dict()
                elif isinstance(resource_group_item_data, DynamicDateTimeSearchCondition):
                    resource_group_item = resource_group_item_data.to_dict()
                elif isinstance(resource_group_item_data, DynamicTimeSearchCondition):
                    resource_group_item = resource_group_item_data.to_dict()
                else:
                    resource_group_item = resource_group_item_data.to_dict()

                resource_group.append(resource_group_item)

        resource: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resource, Unset):
            resource = []
            for resource_item_data in self.resource:
                resource_item: dict[str, Any]
                if isinstance(resource_item_data, StringSearchCondition):
                    resource_item = resource_item_data.to_dict()
                elif isinstance(resource_item_data, IntegerSearchCondition):
                    resource_item = resource_item_data.to_dict()
                elif isinstance(resource_item_data, FloatSearchCondition):
                    resource_item = resource_item_data.to_dict()
                elif isinstance(resource_item_data, BooleanSearchCondition):
                    resource_item = resource_item_data.to_dict()
                elif isinstance(resource_item_data, DateSearchCondition):
                    resource_item = resource_item_data.to_dict()
                elif isinstance(resource_item_data, DateTimeSearchCondition):
                    resource_item = resource_item_data.to_dict()
                elif isinstance(resource_item_data, TimeSearchCondition):
                    resource_item = resource_item_data.to_dict()
                elif isinstance(resource_item_data, TableSearchCondition):
                    resource_item = resource_item_data.to_dict()
                elif isinstance(resource_item_data, DynamicStringSearchCondition):
                    resource_item = resource_item_data.to_dict()
                elif isinstance(resource_item_data, DynamicIntegerSearchCondition):
                    resource_item = resource_item_data.to_dict()
                elif isinstance(resource_item_data, DynamicFloatSearchCondition):
                    resource_item = resource_item_data.to_dict()
                elif isinstance(resource_item_data, DynamicBooleanSearchCondition):
                    resource_item = resource_item_data.to_dict()
                elif isinstance(resource_item_data, DynamicDateSearchCondition):
                    resource_item = resource_item_data.to_dict()
                elif isinstance(resource_item_data, DynamicDateTimeSearchCondition):
                    resource_item = resource_item_data.to_dict()
                elif isinstance(resource_item_data, DynamicTimeSearchCondition):
                    resource_item = resource_item_data.to_dict()
                else:
                    resource_item = resource_item_data.to_dict()

                resource.append(resource_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project is not UNSET:
            field_dict["project"] = project
        if resource_group is not UNSET:
            field_dict["resource_group"] = resource_group
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.boolean_search_condition import BooleanSearchCondition
        from ..models.date_search_condition import DateSearchCondition
        from ..models.date_time_search_condition import DateTimeSearchCondition
        from ..models.dynamic_boolean_search_condition import DynamicBooleanSearchCondition
        from ..models.dynamic_date_search_condition import DynamicDateSearchCondition
        from ..models.dynamic_date_time_search_condition import DynamicDateTimeSearchCondition
        from ..models.dynamic_float_search_condition import DynamicFloatSearchCondition
        from ..models.dynamic_integer_search_condition import DynamicIntegerSearchCondition
        from ..models.dynamic_string_search_condition import DynamicStringSearchCondition
        from ..models.dynamic_table_search_condition import DynamicTableSearchCondition
        from ..models.dynamic_time_search_condition import DynamicTimeSearchCondition
        from ..models.float_search_condition import FloatSearchCondition
        from ..models.integer_search_condition import IntegerSearchCondition
        from ..models.string_search_condition import StringSearchCondition
        from ..models.table_search_condition import TableSearchCondition
        from ..models.time_search_condition import TimeSearchCondition

        d = dict(src_dict)
        _project = d.pop("project", UNSET)
        project: (
            list[
                BooleanSearchCondition
                | DateSearchCondition
                | DateTimeSearchCondition
                | DynamicBooleanSearchCondition
                | DynamicDateSearchCondition
                | DynamicDateTimeSearchCondition
                | DynamicFloatSearchCondition
                | DynamicIntegerSearchCondition
                | DynamicStringSearchCondition
                | DynamicTableSearchCondition
                | DynamicTimeSearchCondition
                | FloatSearchCondition
                | IntegerSearchCondition
                | StringSearchCondition
                | TableSearchCondition
                | TimeSearchCondition
            ]
            | Unset
        ) = UNSET
        if _project is not UNSET:
            project = []
            for project_item_data in _project:

                def _parse_project_item(
                    data: object,
                ) -> (
                    BooleanSearchCondition
                    | DateSearchCondition
                    | DateTimeSearchCondition
                    | DynamicBooleanSearchCondition
                    | DynamicDateSearchCondition
                    | DynamicDateTimeSearchCondition
                    | DynamicFloatSearchCondition
                    | DynamicIntegerSearchCondition
                    | DynamicStringSearchCondition
                    | DynamicTableSearchCondition
                    | DynamicTimeSearchCondition
                    | FloatSearchCondition
                    | IntegerSearchCondition
                    | StringSearchCondition
                    | TableSearchCondition
                    | TimeSearchCondition
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        project_item_type_0 = StringSearchCondition.from_dict(data)

                        return project_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        project_item_type_1 = IntegerSearchCondition.from_dict(data)

                        return project_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        project_item_type_2 = FloatSearchCondition.from_dict(data)

                        return project_item_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        project_item_type_3 = BooleanSearchCondition.from_dict(data)

                        return project_item_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        project_item_type_4 = DateSearchCondition.from_dict(data)

                        return project_item_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        project_item_type_5 = DateTimeSearchCondition.from_dict(data)

                        return project_item_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        project_item_type_6 = TimeSearchCondition.from_dict(data)

                        return project_item_type_6
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        project_item_type_7 = TableSearchCondition.from_dict(data)

                        return project_item_type_7
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        project_item_type_8 = DynamicStringSearchCondition.from_dict(data)

                        return project_item_type_8
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        project_item_type_9 = DynamicIntegerSearchCondition.from_dict(data)

                        return project_item_type_9
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        project_item_type_10 = DynamicFloatSearchCondition.from_dict(data)

                        return project_item_type_10
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        project_item_type_11 = DynamicBooleanSearchCondition.from_dict(data)

                        return project_item_type_11
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        project_item_type_12 = DynamicDateSearchCondition.from_dict(data)

                        return project_item_type_12
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        project_item_type_13 = DynamicDateTimeSearchCondition.from_dict(data)

                        return project_item_type_13
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        project_item_type_14 = DynamicTimeSearchCondition.from_dict(data)

                        return project_item_type_14
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    project_item_type_15 = DynamicTableSearchCondition.from_dict(data)

                    return project_item_type_15

                project_item = _parse_project_item(project_item_data)

                project.append(project_item)

        _resource_group = d.pop("resource_group", UNSET)
        resource_group: (
            list[
                BooleanSearchCondition
                | DateSearchCondition
                | DateTimeSearchCondition
                | DynamicBooleanSearchCondition
                | DynamicDateSearchCondition
                | DynamicDateTimeSearchCondition
                | DynamicFloatSearchCondition
                | DynamicIntegerSearchCondition
                | DynamicStringSearchCondition
                | DynamicTableSearchCondition
                | DynamicTimeSearchCondition
                | FloatSearchCondition
                | IntegerSearchCondition
                | StringSearchCondition
                | TableSearchCondition
                | TimeSearchCondition
            ]
            | Unset
        ) = UNSET
        if _resource_group is not UNSET:
            resource_group = []
            for resource_group_item_data in _resource_group:

                def _parse_resource_group_item(
                    data: object,
                ) -> (
                    BooleanSearchCondition
                    | DateSearchCondition
                    | DateTimeSearchCondition
                    | DynamicBooleanSearchCondition
                    | DynamicDateSearchCondition
                    | DynamicDateTimeSearchCondition
                    | DynamicFloatSearchCondition
                    | DynamicIntegerSearchCondition
                    | DynamicStringSearchCondition
                    | DynamicTableSearchCondition
                    | DynamicTimeSearchCondition
                    | FloatSearchCondition
                    | IntegerSearchCondition
                    | StringSearchCondition
                    | TableSearchCondition
                    | TimeSearchCondition
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_group_item_type_0 = StringSearchCondition.from_dict(data)

                        return resource_group_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_group_item_type_1 = IntegerSearchCondition.from_dict(data)

                        return resource_group_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_group_item_type_2 = FloatSearchCondition.from_dict(data)

                        return resource_group_item_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_group_item_type_3 = BooleanSearchCondition.from_dict(data)

                        return resource_group_item_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_group_item_type_4 = DateSearchCondition.from_dict(data)

                        return resource_group_item_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_group_item_type_5 = DateTimeSearchCondition.from_dict(data)

                        return resource_group_item_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_group_item_type_6 = TimeSearchCondition.from_dict(data)

                        return resource_group_item_type_6
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_group_item_type_7 = TableSearchCondition.from_dict(data)

                        return resource_group_item_type_7
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_group_item_type_8 = DynamicStringSearchCondition.from_dict(data)

                        return resource_group_item_type_8
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_group_item_type_9 = DynamicIntegerSearchCondition.from_dict(data)

                        return resource_group_item_type_9
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_group_item_type_10 = DynamicFloatSearchCondition.from_dict(data)

                        return resource_group_item_type_10
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_group_item_type_11 = DynamicBooleanSearchCondition.from_dict(data)

                        return resource_group_item_type_11
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_group_item_type_12 = DynamicDateSearchCondition.from_dict(data)

                        return resource_group_item_type_12
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_group_item_type_13 = DynamicDateTimeSearchCondition.from_dict(data)

                        return resource_group_item_type_13
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_group_item_type_14 = DynamicTimeSearchCondition.from_dict(data)

                        return resource_group_item_type_14
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    resource_group_item_type_15 = DynamicTableSearchCondition.from_dict(data)

                    return resource_group_item_type_15

                resource_group_item = _parse_resource_group_item(resource_group_item_data)

                resource_group.append(resource_group_item)

        _resource = d.pop("resource", UNSET)
        resource: (
            list[
                BooleanSearchCondition
                | DateSearchCondition
                | DateTimeSearchCondition
                | DynamicBooleanSearchCondition
                | DynamicDateSearchCondition
                | DynamicDateTimeSearchCondition
                | DynamicFloatSearchCondition
                | DynamicIntegerSearchCondition
                | DynamicStringSearchCondition
                | DynamicTableSearchCondition
                | DynamicTimeSearchCondition
                | FloatSearchCondition
                | IntegerSearchCondition
                | StringSearchCondition
                | TableSearchCondition
                | TimeSearchCondition
            ]
            | Unset
        ) = UNSET
        if _resource is not UNSET:
            resource = []
            for resource_item_data in _resource:

                def _parse_resource_item(
                    data: object,
                ) -> (
                    BooleanSearchCondition
                    | DateSearchCondition
                    | DateTimeSearchCondition
                    | DynamicBooleanSearchCondition
                    | DynamicDateSearchCondition
                    | DynamicDateTimeSearchCondition
                    | DynamicFloatSearchCondition
                    | DynamicIntegerSearchCondition
                    | DynamicStringSearchCondition
                    | DynamicTableSearchCondition
                    | DynamicTimeSearchCondition
                    | FloatSearchCondition
                    | IntegerSearchCondition
                    | StringSearchCondition
                    | TableSearchCondition
                    | TimeSearchCondition
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_item_type_0 = StringSearchCondition.from_dict(data)

                        return resource_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_item_type_1 = IntegerSearchCondition.from_dict(data)

                        return resource_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_item_type_2 = FloatSearchCondition.from_dict(data)

                        return resource_item_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_item_type_3 = BooleanSearchCondition.from_dict(data)

                        return resource_item_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_item_type_4 = DateSearchCondition.from_dict(data)

                        return resource_item_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_item_type_5 = DateTimeSearchCondition.from_dict(data)

                        return resource_item_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_item_type_6 = TimeSearchCondition.from_dict(data)

                        return resource_item_type_6
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_item_type_7 = TableSearchCondition.from_dict(data)

                        return resource_item_type_7
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_item_type_8 = DynamicStringSearchCondition.from_dict(data)

                        return resource_item_type_8
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_item_type_9 = DynamicIntegerSearchCondition.from_dict(data)

                        return resource_item_type_9
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_item_type_10 = DynamicFloatSearchCondition.from_dict(data)

                        return resource_item_type_10
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_item_type_11 = DynamicBooleanSearchCondition.from_dict(data)

                        return resource_item_type_11
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_item_type_12 = DynamicDateSearchCondition.from_dict(data)

                        return resource_item_type_12
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_item_type_13 = DynamicDateTimeSearchCondition.from_dict(data)

                        return resource_item_type_13
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        resource_item_type_14 = DynamicTimeSearchCondition.from_dict(data)

                        return resource_item_type_14
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    resource_item_type_15 = DynamicTableSearchCondition.from_dict(data)

                    return resource_item_type_15

                resource_item = _parse_resource_item(resource_item_data)

                resource.append(resource_item)

        dynamic_entity_search_request = cls(
            project=project,
            resource_group=resource_group,
            resource=resource,
        )

        dynamic_entity_search_request.additional_properties = d
        return dynamic_entity_search_request

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
