"""Schema classes for Tektome resources and projects."""

import ssl
from datetime import date, datetime
from typing import Any, ClassVar
from uuid import UUID

import httpx
from pydantic import BaseModel, ConfigDict, Field, field_validator, AnyHttpUrl

from tektome.endpoints.client import AuthenticatedClient


class BaseSchema(BaseModel):
    """
    Base schema class for all Tektome models.
    Forbids extra fields and provides common configuration.
    """

    model_config = ConfigDict(extra="forbid")


class Resource(BaseSchema):
    """
    Represents a single resource.
    """

    id: UUID = Field(..., description="The unique identifier for the resource")
    kind: str = Field(..., description="The kind of the schema, must be 'resource")

    @field_validator("kind")
    def validate_kind(cls, v):
        if v != "resource":
            raise ValueError("kind must be 'resource'")

        return v


class Resources(BaseSchema):
    """
    Represents a single resource.
    """

    ids: list[UUID] = Field(..., description="The unique identifier for the resource")
    kind: str = Field(..., description="The kind of the schema, must be 'resource[]")

    @field_validator("kind")
    def validate_kind(cls, v):
        if v != "resource[]":
            raise ValueError("kind must be 'resource[]'")

        return v


class Project(BaseSchema):
    """
    Represents a single project.
    """

    id: UUID = Field(..., description="The unique identifier for the project")
    kind: str = Field(..., description="The kind of the schema, must be 'project'")

    @field_validator("kind")
    def validate_kind(cls, v):
        if v != "project":
            raise ValueError("kind must be 'project'")

        return v


class Projects(BaseSchema):
    """
    Represents a single project.
    """

    ids: list[UUID] = Field(..., description="The unique identifier for the project")
    kind: str = Field(..., description="The kind of the schema, must be 'project[]'")

    @field_validator("kind")
    def validate_kind(cls, v):
        if v != "project[]":
            raise ValueError("kind must be 'project[]'")

        return v


class AttributeDefinitions(BaseSchema):
    """
    Represents definition of a resource or project.
    """

    ids: list[UUID] = Field(..., description="The unique identifier for the attributes")
    kind: str = Field(
        ..., description="The kind of the schema, must be 'attribute_definition[]'"
    )

    @field_validator("kind")
    def validate_kind(cls, v):
        if v != "attribute_definition[]":
            raise ValueError("kind must be 'attribute_definition[]'")

        return v


class Context(BaseSchema):
    """
    Represents context configuration automatically inserted by the system.
    Contains authentication and deployment information.

    Guarded fields (system_chatroom_id, system_execution_id, system_dataspace_id,
    system_project_id, system_resource_id) raise AttributeError when accessed if None,
    so no explicit None checks are needed.

    Guarded fields are intended to provide additional context when available,
    but may not be present depending on where the execution started.
    Example: system_chatroom_id is only present when invoked from a chatroom.
    """

    system_user_api_key: str = Field(
        ...,
        description='User\'s API key. Include as "Authorization": Bearer <key> in the header to authenticate as the current user.',
    )
    system_base_url: AnyHttpUrl = Field(
        ...,
        description="Tektome's deployment base url ex: https://domain.tld",
    )
    system_chatroom_id: UUID | None = Field(
        None,
        description="The chatroom that this code is being invoked from, if applicable",
    )
    system_execution_id: UUID | None = Field(
        None,
        description="Execution id used to obtain additional extraction context",
    )
    system_dataspace_id: UUID | None = Field(
        None,
        description="Dataspace id used to obtain dataspace-specific settings",
    )
    system_project_id: UUID | None = Field(
        None,
        description="Project id used to obtain project-specific settings",
    )
    system_resource_id: UUID | None = Field(
        None,
        description="Resource id used to obtain resource-specific settings",
    )
    system_attribute_definition_ids: list[UUID] | None = Field(
        None,
        description="Attribute definition ids used to obtain attribute-specific settings",
    )

    _guarded_fields: ClassVar[set[str]] = {
        "system_chatroom_id",
        "system_execution_id",
        "system_dataspace_id",
        "system_project_id",
        "system_resource_id",
    }

    def __getattribute__(self, name: str) -> Any:
        if name in type(self)._guarded_fields:
            value = super().__getattribute__(name)
            if value is None:
                raise AttributeError(f"{name} is not available in this context")
            return value
        return super().__getattribute__(name)

    def client(
        self,
        *,
        cookies: dict[str, str] | None = None,
        headers: dict[str, str] | None = None,
        timeout: httpx.Timeout | None = None,
        verify_ssl: str | bool | ssl.SSLContext = True,
        follow_redirects: bool = False,
        httpx_args: dict[str, Any] | None = None,
        raise_on_unexpected_status: bool = True,
    ) -> AuthenticatedClient:
        """
        Tektome API client initialized with the context's base_url and user_api_key.

        Args:
            cookies: A dictionary of cookies to be sent with every request.
            headers: A dictionary of headers to be sent with every request.
            timeout: The maximum amount of time a request can take.
            verify_ssl: Whether to verify the SSL certificate of the API server.
            follow_redirects: Whether to follow redirects.
            httpx_args: Additional arguments passed to httpx.Client/AsyncClient.
            raise_on_unexpected_status: Whether to raise on undocumented status codes.
        """
        return AuthenticatedClient(
            base_url=str(self.system_base_url),
            token=self.system_user_api_key,
            cookies=cookies or {},
            headers=headers or {},
            timeout=timeout,
            verify_ssl=verify_ssl,
            follow_redirects=follow_redirects,
            httpx_args=httpx_args or {},
            raise_on_unexpected_status=raise_on_unexpected_status,
        )


class Date(BaseSchema):
    """
    Represents a date value.
    """

    value: date = Field(..., description="The date value")
    kind: str = Field(..., description="The kind of the schema, must be 'date'")

    @field_validator("kind")
    def validate_kind(cls, v):
        if v != "date":
            raise ValueError("kind must be 'date'")

        return v


class DateTime(BaseSchema):
    """
    Represents a datetime value.
    """

    value: datetime = Field(..., description="The datetime value")
    kind: str = Field(..., description="The kind of the schema, must be 'datetime'")

    @field_validator("kind")
    def validate_kind(cls, v):
        if v != "datetime":
            raise ValueError("kind must be 'datetime'")

        return v
