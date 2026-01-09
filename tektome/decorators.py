"""Decorators for input/output validation and transformation."""

from pydantic import BaseModel, validate_call
from collections.abc import Callable
from functools import wraps
from typing import Any, ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def parseio(func: Callable[P, T]) -> Callable[P, dict[str, Any]]:
    """Decorator that validates inputs with pydantic and outputs with beartype.

    - Inputs: Validated/coerced using pydantic's @validate_call (dicts become models)
    - Outputs: If return type is a Pydantic model and result is a dict, validates against the model
    - Return value: Converted to dict via .model_dump() if it's a Pydantic model, ensuring json-serializability.

    Args:
        func: The function to decorate.

    Returns:
        Decorated function with input validation, output type checking,
        and automatic model_dump() conversion for Pydantic models.
    """
    validated_func = validate_call(func)

    # Get the return type annotation
    return_type = func.__annotations__.get("return")
    return_is_pydantic_model = isinstance(return_type, type) and issubclass(
        return_type, BaseModel
    )

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> dict[str, Any]:
        result = validated_func(*args, **kwargs)
        if isinstance(result, BaseModel):
            return result.model_dump()
        if isinstance(result, dict):
            # If return type is a Pydantic model, validate the dict against it
            if return_is_pydantic_model:
                return return_type.model_validate(result).model_dump()  # type: ignore
            return result
        raise TypeError(
            f"Expected return type to be dict or Pydantic model, got {type(result)}"
        )

    return wrapper
