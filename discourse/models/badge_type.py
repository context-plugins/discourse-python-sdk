from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BadgeType(SdkBaseModel):
    id: int
    name: str
    sort_order: int


class BadgeTypeDict(TypedDict):
    id: int
    name: str
    sort_order: int
