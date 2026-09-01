from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class UserTheme(SdkBaseModel):
    theme_id: int
    name: str
    default: bool
    color_scheme_id: int | None
    dark_color_scheme_id: OptionalNullable[int] = UNSET
    only_theme_color_schemes: Optional[bool] = UNSET


class UserThemeDict(TypedDict):
    theme_id: int
    name: str
    default: bool
    color_scheme_id: int | None
    dark_color_scheme_id: NotRequired[int | None]
    only_theme_color_schemes: NotRequired[bool]
