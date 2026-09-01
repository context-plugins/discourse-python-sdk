from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Triggers(SdkBaseModel):
    user_change: int
    none: int
    post_revision: int
    trust_level_change: int
    post_action: int


class TriggersDict(TypedDict):
    user_change: int
    none: int
    post_revision: int
    trust_level_change: int
    post_action: int
