from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UserBadge(SdkBaseModel):
    id: int
    granted_at: str
    grouping_position: int
    is_favorite: str | None
    can_favorite: bool
    badge_id: int
    granted_by_id: int


class UserBadgeDict(TypedDict):
    id: int
    granted_at: str
    grouping_position: int
    is_favorite: str | None
    can_favorite: bool
    badge_id: int
    granted_by_id: int
