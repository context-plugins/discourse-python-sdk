from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BadgeGrouping(SdkBaseModel):
    id: int
    name: str
    description: str | None
    position: int
    system: bool


class BadgeGroupingDict(TypedDict):
    id: int
    name: str
    description: str | None
    position: int
    system: bool
