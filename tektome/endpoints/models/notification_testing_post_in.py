from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_entity_type import NotificationEntityType
from ..models.notification_type import NotificationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_testing_post_in_extras import NotificationTestingPostInExtras


T = TypeVar("T", bound="NotificationTestingPostIn")


@_attrs_define
class NotificationTestingPostIn:
    """Input schema for creating test notifications.

    Attributes:
        notification_type (NotificationType): Types of notifications for execution lifecycle events.
        entity_type (NotificationEntityType): Types of entities that can be associated with a notification.
        dataspace_id (UUID): The dataspace to associate the notification with. The authenticated user must have access
            to this dataspace.
        entity_id (None | Unset | UUID): The UUID of the entity. Auto-generated if random_values is True.
        target_user_ids (list[UUID] | None | Unset): Optional list of user IDs to receive the notification. The launcher
            is always included. All target users must be members of the specified dataspace.
        aggregated_notification (bool | Unset): Whether to create an aggregated notification. Default: False.
        random_values (bool | Unset): Whether to generate random values for missing content arguments. Default: True.
        extras (NotificationTestingPostInExtras | Unset): Additional keyword arguments for content template formatting.
    """

    notification_type: NotificationType
    entity_type: NotificationEntityType
    dataspace_id: UUID
    entity_id: None | Unset | UUID = UNSET
    target_user_ids: list[UUID] | None | Unset = UNSET
    aggregated_notification: bool | Unset = False
    random_values: bool | Unset = True
    extras: NotificationTestingPostInExtras | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notification_type = self.notification_type.value

        entity_type = self.entity_type.value

        dataspace_id = str(self.dataspace_id)

        entity_id: None | str | Unset
        if isinstance(self.entity_id, Unset):
            entity_id = UNSET
        elif isinstance(self.entity_id, UUID):
            entity_id = str(self.entity_id)
        else:
            entity_id = self.entity_id

        target_user_ids: list[str] | None | Unset
        if isinstance(self.target_user_ids, Unset):
            target_user_ids = UNSET
        elif isinstance(self.target_user_ids, list):
            target_user_ids = []
            for target_user_ids_type_0_item_data in self.target_user_ids:
                target_user_ids_type_0_item = str(target_user_ids_type_0_item_data)
                target_user_ids.append(target_user_ids_type_0_item)

        else:
            target_user_ids = self.target_user_ids

        aggregated_notification = self.aggregated_notification

        random_values = self.random_values

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notification_type": notification_type,
                "entity_type": entity_type,
                "dataspace_id": dataspace_id,
            }
        )
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if target_user_ids is not UNSET:
            field_dict["target_user_ids"] = target_user_ids
        if aggregated_notification is not UNSET:
            field_dict["aggregated_notification"] = aggregated_notification
        if random_values is not UNSET:
            field_dict["random_values"] = random_values
        if extras is not UNSET:
            field_dict["extras"] = extras

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_testing_post_in_extras import NotificationTestingPostInExtras

        d = dict(src_dict)
        notification_type = NotificationType(d.pop("notification_type"))

        entity_type = NotificationEntityType(d.pop("entity_type"))

        dataspace_id = UUID(d.pop("dataspace_id"))

        def _parse_entity_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                entity_id_type_0 = UUID(data)

                return entity_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

        def _parse_target_user_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                target_user_ids_type_0 = []
                _target_user_ids_type_0 = data
                for target_user_ids_type_0_item_data in _target_user_ids_type_0:
                    target_user_ids_type_0_item = UUID(target_user_ids_type_0_item_data)

                    target_user_ids_type_0.append(target_user_ids_type_0_item)

                return target_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        target_user_ids = _parse_target_user_ids(d.pop("target_user_ids", UNSET))

        aggregated_notification = d.pop("aggregated_notification", UNSET)

        random_values = d.pop("random_values", UNSET)

        _extras = d.pop("extras", UNSET)
        extras: NotificationTestingPostInExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = NotificationTestingPostInExtras.from_dict(_extras)

        notification_testing_post_in = cls(
            notification_type=notification_type,
            entity_type=entity_type,
            dataspace_id=dataspace_id,
            entity_id=entity_id,
            target_user_ids=target_user_ids,
            aggregated_notification=aggregated_notification,
            random_values=random_values,
            extras=extras,
        )

        notification_testing_post_in.additional_properties = d
        return notification_testing_post_in

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
