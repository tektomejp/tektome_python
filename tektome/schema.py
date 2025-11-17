"""Schema classes for Tektome resources and projects."""

from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator, AnyHttpUrl


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
    """

    user_api_key: str = Field(
        ...,
        description='User\'s API key. Include as "Authorization": Bearer <key> in the header to authenticate as the current user.',
    )
    base_url: AnyHttpUrl = Field(
        ..., description="Tektome's deployment base url ex: https://domain.tld"
    )
    execution_id: UUID = Field(
        ..., description="Execution id used to obtain additional extraction context"
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