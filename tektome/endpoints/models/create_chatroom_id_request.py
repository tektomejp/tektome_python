from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.recipe_choices import RecipeChoices

T = TypeVar("T", bound="CreateChatroomIdRequest")


@_attrs_define
class CreateChatroomIdRequest:
    """
    Attributes:
        recipe (RecipeChoices): Supported recipe choices for agent configuration.
        prompt (str): User's message to the LLM agent
    """

    recipe: RecipeChoices
    prompt: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recipe = self.recipe.value

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
        recipe = RecipeChoices(d.pop("recipe"))

        prompt = d.pop("prompt")

        create_chatroom_id_request = cls(
            recipe=recipe,
            prompt=prompt,
        )

        create_chatroom_id_request.additional_properties = d
        return create_chatroom_id_request

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
