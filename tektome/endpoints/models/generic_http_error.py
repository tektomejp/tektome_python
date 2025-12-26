from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GenericHttpError")


@_attrs_define
class GenericHttpError:
    """GenericHttpError for 4xx
    Usage
    ```
    from ninja.errors import HttpError
    from ninja.responses import codes_4xx

    class ChatroomIdPostPath(Schema):
    chatroom_id: UUID

    @field_validator("chatroom_id")
    def validate_chatroom_id(cls, v):
        if not Chatroom.objects.filter(id=v).exists():
            raise HttpError(404, "Chatroom not found")

        return v


    @router.post(
        "/chatrooms/{chatroom_id}/messages/",
        response={
            200: dict,
            codes_4xx: GenericHttpError,
        },
    )
    def post_chatrooms_id_messages(request, chatroom_id: UUID):
        ...
    ```

        Attributes:
            status_code (int):
            message (str):
    """

    status_code: int
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_code = self.status_code

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status_code": status_code,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status_code = d.pop("status_code")

        message = d.pop("message")

        generic_http_error = cls(
            status_code=status_code,
            message=message,
        )

        generic_http_error.additional_properties = d
        return generic_http_error

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
