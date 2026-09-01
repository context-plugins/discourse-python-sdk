from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Poster6(SdkBaseModel):
    extras: OptionalNullable[str] = UNSET
    description: Optional[str] = UNSET
    user_id: Optional[int] = UNSET
    primary_group_id: OptionalNullable[int] = UNSET


class Poster6Dict(TypedDict):
    extras: NotRequired[str | None]
    description: NotRequired[str]
    user_id: NotRequired[int]
    primary_group_id: NotRequired[int | None]
