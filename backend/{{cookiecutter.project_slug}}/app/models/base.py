import re
from datetime import datetime, timezone
from typing import Generic, List, TypeVar

from pydantic.generics import GenericModel

T = TypeVar("T")


def to_camel(snake_str: str) -> str:
    words = snake_str.split("_")
    return words[0] + "".join(w.title() for w in words[1:])


def to_snake(camel_str: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", camel_str).lower()


def convert_datetime_to_realworld(dt: datetime) -> str:
    return dt.replace(tzinfo=timezone.utc).isoformat().replace("+00:00", "Z")


class DateTimeModelMixin(GenericModel, Generic[T]):
    created_at: T
    updated_at: T

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class Page(GenericModel, Generic[T]):
    items: List[T]
    total: int

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
