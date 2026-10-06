from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .admin_badges import AdminBadges, AdminBadgesDict
from .badge import Badge, BadgeDict
from .badge_grouping import BadgeGrouping, BadgeGroupingDict
from .badge_type import BadgeType, BadgeTypeDict


class AdminBadgesJsonResponse(SdkBaseModel):
    badges: list[Badge]
    badge_types: list[BadgeType]
    badge_groupings: list[BadgeGrouping]
    admin_badges: AdminBadges


class AdminBadgesJsonResponseDict(TypedDict):
    badges: list[BadgeDict]
    badge_types: list[BadgeTypeDict]
    badge_groupings: list[BadgeGroupingDict]
    admin_badges: AdminBadgesDict
