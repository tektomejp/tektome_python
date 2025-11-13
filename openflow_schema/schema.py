"""
These classes are used to convert dictonary provided by openflow input to pydantic dataclass with validation.
# Example usage:
```
from openflow_schema import Resource
from pydantic import validate_call


@validate_call  # validate_call attempts to convert input dict to Resource class
def main(resource: Resource):
    print(f"resource is of type: {type(resource)}")  # resource is of type: <class 'Resource'>
```
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, ConfigDict, Field


class Resource(BaseModel):
    """
    Represents a single OpenFlow resource.
    
    This class is used to validate and convert dictionary inputs from OpenFlow
    into a strongly-typed Pydantic model.
    """
    
    model_config = ConfigDict(
        extra="allow",  # Allow additional fields not explicitly defined
        populate_by_name=True
    )
    
    id: Optional[str] = Field(None, description="Unique identifier for the resource")
    name: str = Field(..., description="Name of the resource")
    type: Optional[str] = Field(None, description="Type of the resource")
    description: Optional[str] = Field(None, description="Description of the resource")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Additional metadata")


class Resources(BaseModel):
    """
    Represents a collection of OpenFlow resources.
    
    This class is used to validate and convert dictionary inputs containing
    multiple resources from OpenFlow into a strongly-typed Pydantic model.
    """
    
    model_config = ConfigDict(
        extra="allow",  # Allow additional fields not explicitly defined
        populate_by_name=True
    )
    
    resources: List[Resource] = Field(default_factory=list, description="List of resources")
    total: Optional[int] = Field(None, description="Total count of resources")
