from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .badge1 import Badge1, Badge1Dict
from .badge_type import BadgeType, BadgeTypeDict


class AdminBadgesJsonResponse1(SdkBaseModel):
    badge_types: list[BadgeType]
    badge: Badge1


class AdminBadgesJsonResponse1Dict(TypedDict):
    badge_types: list[BadgeTypeDict]
    badge: Badge1Dict
