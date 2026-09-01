from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class NotificationsMarkReadJsonResponse(SdkBaseModel):
    success: Optional[str] = UNSET


class NotificationsMarkReadJsonResponseDict(TypedDict):
    success: NotRequired[str]
