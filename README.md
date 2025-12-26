# tektome
Utilities for handling Tektome Resources

## Available Classes

- `BaseSchema` - Base class for all schemas (forbids extra fields)
- `Resource` - Single resource with UUID and kind validation
- `Resources` - Collection of resource UUIDs
- `Project` - Single project with UUID and kind validation
- `Projects` - Collection of project UUIDs
- `AttributeDefinitions` - Collection of attribute definition UUIDs
- `Context` - Execution context with API key, base URL, and execution ID
- `Date` - Date value with kind validation
- `DateTime` - DateTime value with kind validation

## Installation

You can install this package directly from GitHub:

```bash
pip install git+https://github.com/tektomejp/tektome_python.git@main
```

## Usage

These classes are used to convert dictionary provided by openflow input to pydantic dataclass with validation.

### The `@parseio` Decorator

The `@parseio` decorator from `tektome.decorators` handles input validation and output serialization:

**Input (arguments):**
- Validates and coerces using Pydantic's `@validate_call` (dicts become models)
- Runtime type-checked via `@beartype`

**Output (return value):**
- Runtime type-checked via `@beartype`
- Pydantic models automatically converted to dict via `.model_dump()`

```python
# requirements:
# git+https://github.com/tektomejp/tektome_python.git@main

from tektome import Resource, Context
from tektome.decorators import parseio
from tektome.endpoints.api.project import create_core_project
from tektome.endpoints.models import CoreProjectPostIn
from pydantic import BaseModel

class Output(BaseModel):
    status: str
    project_id: str

@parseio
def main(ctx: Context, r: Resource, project_name: str) -> Output:
    print(f"type of ctx is: {type(ctx)} with the following data available")
    print(ctx.model_dump())
    print(f"type of r is: {type(r)} with the following data available")
    print(r.model_dump())

    # Create authenticated client from context
    with ctx.client() as client:
        # Create a new project with payload
        payload = CoreProjectPostIn(name=project_name)
        response = create_core_project.sync(client=client, body=payload)
        print(f"Created project: {response}")

    return Output(status="success", project_id=str(response.id))
```

## Development

To install in development mode:

```bash
git clone https://github.com/tektomejp/tektome_python.git
cd tektome_python
uv sync
```
