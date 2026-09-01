from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class User11(SdkBaseModel):
    id: int
    username: str
    name: str | None
    avatar_template: str
    title: str | None


class User11Dict(TypedDict):
    id: int
    username: str
    name: str | None
    avatar_template: str
    title: str | None
