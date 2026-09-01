from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class NotificationsMarkReadJsonRequest(SdkBaseModel):
    id: Optional[int] = UNSET
    """(optional) Leave off to mark all notifications as read"""


class NotificationsMarkReadJsonRequestDict(TypedDict):
    id: NotRequired[int]
