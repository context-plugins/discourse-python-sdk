from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .triggers import Triggers, TriggersDict


class AdminBadges(SdkBaseModel):
    protected_system_fields: list[Any]
    triggers: Triggers
    badge_ids: list[Any]
    badge_grouping_ids: list[Any]
    badge_type_ids: list[Any]


class AdminBadgesDict(TypedDict):
    protected_system_fields: list[Any]
    triggers: Triggers | TriggersDict
    badge_ids: list[Any]
    badge_grouping_ids: list[Any]
    badge_type_ids: list[Any]
