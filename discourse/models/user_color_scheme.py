from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class UserColorScheme(SdkBaseModel):
    id: int
    name: str
    is_dark: bool
    theme_id: OptionalNullable[int] = UNSET
    colors: list[Any]


class UserColorSchemeDict(TypedDict):
    id: int
    name: str
    is_dark: bool
    theme_id: NotRequired[int | None]
    colors: list[Any]
