from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LastPoster(SdkBaseModel):
    id: int
    username: str
    name: str
    avatar_template: str


class LastPosterDict(TypedDict):
    id: int
    username: str
    name: str
    avatar_template: str
