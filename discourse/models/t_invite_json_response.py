from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .user1 import User1, User1Dict


class TInviteJsonResponse(SdkBaseModel):
    user: Optional[User1] = UNSET


class TInviteJsonResponseDict(TypedDict):
    user: NotRequired[User1Dict]
