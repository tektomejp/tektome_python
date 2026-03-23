from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.recipeschoices import RECIPESCHOICES
from ..types import UNSET, Unset

T = TypeVar("T", bound="LawtalkRequirementChatPostIn")


@_attrs_define
class LawtalkRequirementChatPostIn:
    """Serializer for posting a chat message to a lawtalk requirement chatroom.

    Attributes:
        prompt (str): User's message to the chat
        recipe (RECIPESCHOICES):
        requirement_id (str):
        chatroom_id (None | Unset | UUID):
        resource_group_ids (list[UUID] | Unset):
        auto_generate_specs (bool | Unset): Auto-generate specification table after the Auto Capture process Default:
            False.
    """

    prompt: str
    recipe: RECIPESCHOICES
    requirement_id: str
    chatroom_id: None | Unset | UUID = UNSET
    resource_group_ids: list[UUID] | Unset = UNSET
    auto_generate_specs: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prompt = self.prompt

        recipe = self.recipe.value

        requirement_id = self.requirement_id

        chatroom_id: None | str | Unset
        if isinstance(self.chatroom_id, Unset):
            chatroom_id = UNSET
        elif isinstance(self.chatroom_id, UUID):
            chatroom_id = str(self.chatroom_id)
        else:
            chatroom_id = self.chatroom_id

        resource_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.resource_group_ids, Unset):
            resource_group_ids = []
            for resource_group_ids_item_data in self.resource_group_ids:
                resource_group_ids_item = str(resource_group_ids_item_data)
                resource_group_ids.append(resource_group_ids_item)

        auto_generate_specs = self.auto_generate_specs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt": prompt,
                "recipe": recipe,
                "requirement_id": requirement_id,
            }
        )
        if chatroom_id is not UNSET:
            field_dict["chatroom_id"] = chatroom_id
        if resource_group_ids is not UNSET:
            field_dict["resource_group_ids"] = resource_group_ids
        if auto_generate_specs is not UNSET:
            field_dict["auto_generate_specs"] = auto_generate_specs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prompt = d.pop("prompt")

        recipe = RECIPESCHOICES(d.pop("recipe"))

        requirement_id = d.pop("requirement_id")

        def _parse_chatroom_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                chatroom_id_type_0 = UUID(data)

                return chatroom_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        chatroom_id = _parse_chatroom_id(d.pop("chatroom_id", UNSET))

        _resource_group_ids = d.pop("resource_group_ids", UNSET)
        resource_group_ids: list[UUID] | Unset = UNSET
        if _resource_group_ids is not UNSET:
            resource_group_ids = []
            for resource_group_ids_item_data in _resource_group_ids:
                resource_group_ids_item = UUID(resource_group_ids_item_data)

                resource_group_ids.append(resource_group_ids_item)

        auto_generate_specs = d.pop("auto_generate_specs", UNSET)

        lawtalk_requirement_chat_post_in = cls(
            prompt=prompt,
            recipe=recipe,
            requirement_id=requirement_id,
            chatroom_id=chatroom_id,
            resource_group_ids=resource_group_ids,
            auto_generate_specs=auto_generate_specs,
        )

        lawtalk_requirement_chat_post_in.additional_properties = d
        return lawtalk_requirement_chat_post_in

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
