from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ChatroomIdPostIn")


@_attrs_define
class ChatroomIdPostIn:
    """
    Attributes:
        recipe (Literal['tektome-os-v1']):
        prompt (str): User's message to the LLM agent
    """

    recipe: Literal["tektome-os-v1"]
    prompt: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recipe = self.recipe

        prompt = self.prompt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recipe": recipe,
                "prompt": prompt,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        recipe = cast(Literal["tektome-os-v1"], d.pop("recipe"))
        if recipe != "tektome-os-v1":
            raise ValueError(f"recipe must match const 'tektome-os-v1', got '{recipe}'")

        prompt = d.pop("prompt")

        chatroom_id_post_in = cls(
            recipe=recipe,
            prompt=prompt,
        )

        chatroom_id_post_in.additional_properties = d
        return chatroom_id_post_in

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
