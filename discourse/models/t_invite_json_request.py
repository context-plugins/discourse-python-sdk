from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TInviteJsonRequest(SdkBaseModel):
    user: Optional[str] = UNSET
    email: Optional[str] = UNSET


class TInviteJsonRequestDict(TypedDict):
    user: NotRequired[str]
    email: NotRequired[str]
