from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdminUsersSilenceJsonRequest(SdkBaseModel):
    silenced_till: str
    reason: str
    message: Optional[str] = UNSET
    """Will send an email with this message when present"""

    post_action: Optional[str] = UNSET


class AdminUsersSilenceJsonRequestDict(TypedDict):
    silenced_till: str
    reason: str
    message: NotRequired[str]
    post_action: NotRequired[str]
