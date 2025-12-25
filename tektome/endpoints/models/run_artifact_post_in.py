from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run_artifact_post_in_body_type_0 import RunArtifactPostInBodyType0


T = TypeVar("T", bound="RunArtifactPostIn")


@_attrs_define
class RunArtifactPostIn:
    """
    Attributes:
        result_artifact_id (None | Unset | UUID): The ID of target artifact to save the result to. If not provided, a
            new artifact will be created.
        result_artifact_name (None | str | Unset): The name of the artifact to create for the result.
        result_artifact_extension (Literal['json'] | None | Unset): The extension of the artifact to create. E.g. 'json'
        body (None | RunArtifactPostInBodyType0 | Unset): The body to pass to the artifact when running it. This is the
            input data in Windmill flow/Script
    """

    result_artifact_id: None | Unset | UUID = UNSET
    result_artifact_name: None | str | Unset = UNSET
    result_artifact_extension: Literal["json"] | None | Unset = UNSET
    body: None | RunArtifactPostInBodyType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.run_artifact_post_in_body_type_0 import RunArtifactPostInBodyType0

        result_artifact_id: None | str | Unset
        if isinstance(self.result_artifact_id, Unset):
            result_artifact_id = UNSET
        elif isinstance(self.result_artifact_id, UUID):
            result_artifact_id = str(self.result_artifact_id)
        else:
            result_artifact_id = self.result_artifact_id

        result_artifact_name: None | str | Unset
        if isinstance(self.result_artifact_name, Unset):
            result_artifact_name = UNSET
        else:
            result_artifact_name = self.result_artifact_name

        result_artifact_extension: Literal["json"] | None | Unset
        if isinstance(self.result_artifact_extension, Unset):
            result_artifact_extension = UNSET
        else:
            result_artifact_extension = self.result_artifact_extension

        body: dict[str, Any] | None | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        elif isinstance(self.body, RunArtifactPostInBodyType0):
            body = self.body.to_dict()
        else:
            body = self.body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result_artifact_id is not UNSET:
            field_dict["result_artifact_id"] = result_artifact_id
        if result_artifact_name is not UNSET:
            field_dict["result_artifact_name"] = result_artifact_name
        if result_artifact_extension is not UNSET:
            field_dict["result_artifact_extension"] = result_artifact_extension
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_artifact_post_in_body_type_0 import RunArtifactPostInBodyType0

        d = dict(src_dict)

        def _parse_result_artifact_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                result_artifact_id_type_0 = UUID(data)

                return result_artifact_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        result_artifact_id = _parse_result_artifact_id(d.pop("result_artifact_id", UNSET))

        def _parse_result_artifact_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        result_artifact_name = _parse_result_artifact_name(d.pop("result_artifact_name", UNSET))

        def _parse_result_artifact_extension(data: object) -> Literal["json"] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            result_artifact_extension_type_0 = cast(Literal["json"], data)
            if result_artifact_extension_type_0 != "json":
                raise ValueError(
                    f"result_artifact_extension_type_0 must match const 'json', got '{result_artifact_extension_type_0}'"
                )
            return result_artifact_extension_type_0
            return cast(Literal["json"] | None | Unset, data)

        result_artifact_extension = _parse_result_artifact_extension(d.pop("result_artifact_extension", UNSET))

        def _parse_body(data: object) -> None | RunArtifactPostInBodyType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                body_type_0 = RunArtifactPostInBodyType0.from_dict(data)

                return body_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunArtifactPostInBodyType0 | Unset, data)

        body = _parse_body(d.pop("body", UNSET))

        run_artifact_post_in = cls(
            result_artifact_id=result_artifact_id,
            result_artifact_name=result_artifact_name,
            result_artifact_extension=result_artifact_extension,
            body=body,
        )

        run_artifact_post_in.additional_properties = d
        return run_artifact_post_in

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
