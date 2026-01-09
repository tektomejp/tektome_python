# Decorators

## `@parseio`

The `@parseio` decorator provides input validation and output serialization for functions working with Tektome resources.

::: tektome.decorators.parseio

## Overview

The decorator handles:

**Input (arguments):**

- Validates and coerces using Pydantic's `@validate_call` (dicts become models)

**Output (return value):**

- Pydantic models automatically converted to dict via `.model_dump()`
- If return type is annotated as a Pydantic model but a dict is returned, the dict is validated against the model
- JSON serializability is validated by default

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `return_dict` | `bool` | `True` | If `True`, convert Pydantic models to dict. If `False`, return the model instance. |
| `validate_json_serializable` | `bool` | `True` | If `True`, validate that the return value is JSON serializable. |

## Usage Styles

```python
from tektome.decorators import parseio

@parseio                    # Uses defaults
def func1(): ...

@parseio()                  # Same as above
def func2(): ...

@parseio(return_dict=False) # Return Pydantic model instead of dict
def func3(): ...

@parseio(validate_json_serializable=False)  # Skip JSON validation
def func4(): ...
```

## Examples

### Basic Usage

```python
from tektome import Resource, Context
from tektome.decorators import parseio
from pydantic import BaseModel

class Output(BaseModel):
    status: str
    resource_id: str

@parseio
def process_resource(ctx: Context, r: Resource) -> Output:
    # ctx and r are validated Pydantic models
    # Input dicts are automatically coerced to models
    return Output(status="success", resource_id=str(r.id))

# Call with dicts - automatically validated and coerced
result = process_resource(
    ctx={"api_key": "key", "base_url": "url", "execution_id": "id"},
    r={"id": "123e4567-e89b-12d3-a456-426614174000", "kind": "resource"}
)
# result is a dict: {"status": "success", "resource_id": "123e4567-..."}
```

### Returning Dict Instead of Model

```python
@parseio
def process(x: int) -> Output:
    # Can return a dict - it will be validated against Output
    return {"status": "ok", "resource_id": "abc"}

# The dict is validated and returned as-is
result = process(42)
```

### Keeping Pydantic Model

```python
@parseio(return_dict=False)
def process(x: int) -> Output:
    return Output(status="ok", resource_id="abc")

# Returns the actual Pydantic model instance
result = process(42)
assert isinstance(result, Output)
```

### Skipping JSON Validation

```python
@parseio(validate_json_serializable=False)
def process() -> dict:
    # This would fail with default settings (functions aren't JSON serializable)
    return {"callback": lambda x: x * 2}

result = process()  # Works because JSON validation is disabled
```

## Error Handling

### Invalid Input

```python
from pydantic import ValidationError

@parseio
def func(data: Resource) -> dict:
    return {"id": str(data.id)}

try:
    func({"id": "not-a-uuid", "kind": "resource"})
except ValidationError as e:
    print(f"Input validation failed: {e}")
```

### Invalid Output

```python
@parseio
def func() -> dict:
    return {"data": {1, 2, 3}}  # Sets are not JSON serializable

try:
    func()
except TypeError as e:
    print(f"Output not JSON serializable: {e}")
```

### Wrong Return Type

```python
@parseio
def func() -> str:  # Must return dict or Pydantic model
    return "hello"

try:
    func()
except TypeError as e:
    print(f"Invalid return type: {e}")
```
