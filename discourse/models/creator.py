from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Creator(SdkBaseModel):
    id: int
    username: str
    name: OptionalNullable[str] = UNSET
    avatar_template: str


class CreatorDict(TypedDict):
    id: int
    username: str
    name: NotRequired[str | None]
    avatar_template: str
