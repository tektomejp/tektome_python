"""Decorators for input/output validation and transformation."""

from beartype import beartype
from pydantic import BaseModel, validate_call
from collections.abc import Callable
from functools import wraps
from typing import Any, ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def parseio(func: Callable[P, T]) -> Callable[P, dict[str, Any]]:
    """Decorator that validates inputs with pydantic and outputs with beartype.

    - Inputs: Validated/coerced using pydantic's @validate_call (dicts become models)
    - Outputs: Type-checked using @beartype
    - Return value: Converted to dict via .model_dump() if it's a Pydantic model, ensureing json-serializability.

    Args:
        func: The function to decorate.

    Returns:
        Decorated function with input validation, output type checking,
        and automatic model_dump() conversion for Pydantic models.
    """
    beartype_func = beartype(func)
    validated_func = validate_call(beartype_func)

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> dict[str, Any]:
        result = validated_func(*args, **kwargs)
        if isinstance(result, BaseModel):
            return result.model_dump()
        if not isinstance(result, dict):
            raise TypeError(
                f"Expected return type to be dict or Pydantic model, got {type(result)}"
            )
        return result

    return wrapper
