from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.recipe_choices import RecipeChoices
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_chatroom_id_request_user_context_type_0 import CreateChatroomIdRequestUserContextType0


T = TypeVar("T", bound="CreateChatroomIdRequest")


@_attrs_define
class CreateChatroomIdRequest:
    """
    Attributes:
        prompt (str): User's message to the LLM agent
        recipe (None | RecipeChoices | Unset): The recipe to use for the chat. If not provided, defaults based on
            chatroom type: general -> tektome-os-v1, process_creator -> tektome-os-process-creator-v1.
        user_context (CreateChatroomIdRequestUserContextType0 | None | Unset): Optional client-supplied context about
            the user's current state (e.g., current page, dataspace id, focus). Forwarded verbatim into the LLM's system
            prompt under a <UserContext> section so the agent can disambiguate intent without asking the user for IDs.
    """

    prompt: str
    recipe: None | RecipeChoices | Unset = UNSET
    user_context: CreateChatroomIdRequestUserContextType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_chatroom_id_request_user_context_type_0 import CreateChatroomIdRequestUserContextType0

        prompt = self.prompt

        recipe: None | str | Unset
        if isinstance(self.recipe, Unset):
            recipe = UNSET
        elif isinstance(self.recipe, RecipeChoices):
            recipe = self.recipe.value
        else:
            recipe = self.recipe

        user_context: dict[str, Any] | None | Unset
        if isinstance(self.user_context, Unset):
            user_context = UNSET
        elif isinstance(self.user_context, CreateChatroomIdRequestUserContextType0):
            user_context = self.user_context.to_dict()
        else:
            user_context = self.user_context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt": prompt,
            }
        )
        if recipe is not UNSET:
            field_dict["recipe"] = recipe
        if user_context is not UNSET:
            field_dict["user_context"] = user_context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_chatroom_id_request_user_context_type_0 import CreateChatroomIdRequestUserContextType0

        d = dict(src_dict)
        prompt = d.pop("prompt")

        def _parse_recipe(data: object) -> None | RecipeChoices | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recipe_type_0 = RecipeChoices(data)

                return recipe_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RecipeChoices | Unset, data)

        recipe = _parse_recipe(d.pop("recipe", UNSET))

        def _parse_user_context(data: object) -> CreateChatroomIdRequestUserContextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_context_type_0 = CreateChatroomIdRequestUserContextType0.from_dict(data)

                return user_context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateChatroomIdRequestUserContextType0 | None | Unset, data)

        user_context = _parse_user_context(d.pop("user_context", UNSET))

        create_chatroom_id_request = cls(
            prompt=prompt,
            recipe=recipe,
            user_context=user_context,
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
