from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TNotificationsJsonResponse(SdkBaseModel):
    success: Optional[str] = UNSET


class TNotificationsJsonResponseDict(TypedDict):
    success: NotRequired[str]
