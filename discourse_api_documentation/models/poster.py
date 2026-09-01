from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Poster(SdkBaseModel):
    extras: str
    description: str
    user_id: int
    primary_group_id: int | None


class PosterDict(TypedDict):
    extras: str
    description: str
    user_id: int
    primary_group_id: int | None
