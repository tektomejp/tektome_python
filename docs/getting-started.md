# Getting Started

## Installation

You can install Tektome directly from GitHub:

```bash
pip install git+https://github.com/tektomejp/tektome_python.git@main
```

For a specific version:

```bash
pip install git+https://github.com/tektomejp/tektome_python.git@v0.3.0
```

## Basic Usage

These classes are used to convert dictionaries provided by OpenFlow input to Pydantic dataclasses with validation.

### Working with Resources

```python
from tektome import Resource

# Create a resource from a dictionary
resource_data = {
    "uuid": "123e4567-e89b-12d3-a456-426614174000",
    "kind": "resource"
}
resource = Resource(**resource_data)

# Access the data
print(resource.uuid)  # UUID object
print(resource.kind)  # "resource"

# Convert back to dict
data = resource.model_dump()
```

### Working with Context

```python
from tektome import Context

context = Context(
    api_key="your-api-key",
    base_url="https://api.example.com",
    execution_id="exec-123"
)

print(context.api_key)
print(context.base_url)
```

### Working with Collections

```python
from tektome import Resources, Projects

# Resources collection
resources = Resources(
    uuids=["123e4567-e89b-12d3-a456-426614174000"]
)

# Projects collection
projects = Projects(
    uuids=["123e4567-e89b-12d3-a456-426614174001"]
)
```

### Working with Date and DateTime

```python
from tektome import Date, DateTime

# Date
date = Date(value="2025-11-19")
print(date.value)  # "2025-11-19"
print(date.kind)   # "date"

# DateTime
dt = DateTime(value="2025-11-19T10:30:00Z")
print(dt.value)  # "2025-11-19T10:30:00Z"
print(dt.kind)   # "datetime"
```

### Using the `@parseio` Decorator

The `@parseio` decorator handles input validation and output serialization:

```python
from tektome import Resource, Context
from tektome.decorators import parseio
from pydantic import BaseModel

class Output(BaseModel):
    status: str
    resource_id: str

@parseio
def process_resource(ctx: Context, resource: Resource) -> Output:
    """
    This function will automatically:
    - Validate and coerce inputs (dicts become models)
    - Validate output against the Output model
    - Convert output to JSON-serializable dict
    """
    print(f"Processing resource {resource.id}")
    print(f"Using API key: {ctx.api_key}")
    return Output(status="success", resource_id=str(resource.id))

# Call with dicts - automatically validated and coerced
result = process_resource(
    ctx={"api_key": "key", "base_url": "url", "execution_id": "id"},
    resource={"id": "123e4567-e89b-12d3-a456-426614174000", "kind": "resource"}
)
# result is a dict: {"status": "success", "resource_id": "123e4567-..."}

# Call with invalid data - raises ValidationError
try:
    result = process_resource(
        ctx={"api_key": "key", "base_url": "url", "execution_id": "id"},
        resource={"id": "not-a-uuid", "kind": "resource"}
    )
except Exception as e:
    print(f"Validation error: {e}")
```

#### Decorator Options

```python
# Return Pydantic model instead of dict
@parseio(return_dict=False)
def get_model() -> Output:
    return Output(status="ok", resource_id="abc")

# Skip JSON serialization validation
@parseio(validate_json_serializable=False)
def allow_non_json() -> dict:
    return {"callback": lambda x: x}
```

## Development Setup

To contribute or develop with Tektome:

```bash
# Clone the repository
git clone https://github.com/tektomejp/tektome_python.git
cd tektome_python

# Install dependencies
uv sync

# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=tektome
```

## Next Steps

- Explore the [API Reference](api/index.md) for detailed documentation
- Check out the [Contributing Guide](contributing.md) to contribute to the project
