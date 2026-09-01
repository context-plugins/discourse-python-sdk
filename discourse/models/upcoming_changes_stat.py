from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.reason import ReasonOrStr


class UpcomingChangesStat(SdkBaseModel):
    name: str
    humanized_name: str
    description: str
    enabled: bool
    specific_groups: list[str]
    reason: ReasonOrStr


class UpcomingChangesStatDict(TypedDict):
    name: str
    humanized_name: str
    description: str
    enabled: bool
    specific_groups: list[str]
    reason: ReasonOrStr
