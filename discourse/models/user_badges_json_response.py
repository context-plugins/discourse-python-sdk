from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .badge3 import Badge3, Badge3Dict
from .badge_type import BadgeType, BadgeTypeDict
from .granted_by import GrantedBy, GrantedByDict
from .user_badge import UserBadge, UserBadgeDict


class UserBadgesJsonResponse(SdkBaseModel):
    badges: Optional[list[Badge3]] = UNSET
    badge_types: Optional[list[BadgeType]] = UNSET
    granted_bies: Optional[list[GrantedBy]] = UNSET
    user_badges: list[UserBadge]


class UserBadgesJsonResponseDict(TypedDict):
    badges: NotRequired[list[Badge3 | Badge3Dict]]
    badge_types: NotRequired[list[BadgeType | BadgeTypeDict]]
    granted_bies: NotRequired[list[GrantedBy | GrantedByDict]]
    user_badges: list[UserBadge | UserBadgeDict]
