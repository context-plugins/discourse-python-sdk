from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .group6 import Group6, Group6Dict


class TInviteGroupJsonResponse(SdkBaseModel):
    group: Optional[Group6] = UNSET


class TInviteGroupJsonResponseDict(TypedDict):
    group: NotRequired[Group6 | Group6Dict]
