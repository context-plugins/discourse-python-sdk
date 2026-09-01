from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class User2(SdkBaseModel):
    id: Optional[int] = UNSET
    username: Optional[str] = UNSET
    name: OptionalNullable[str] = UNSET
    avatar_template: Optional[str] = UNSET


class User2Dict(TypedDict):
    id: NotRequired[int]
    username: NotRequired[str]
    name: NotRequired[str | None]
    avatar_template: NotRequired[str]
