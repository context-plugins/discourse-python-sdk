from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .notification import Notification, NotificationDict


class NotificationsJsonResponse(SdkBaseModel):
    notifications: Optional[list[Notification]] = UNSET
    total_rows_notifications: Optional[int] = UNSET
    seen_notification_id: Optional[int] = UNSET
    load_more_notifications: Optional[str] = UNSET


class NotificationsJsonResponseDict(TypedDict):
    notifications: NotRequired[list[Notification | NotificationDict]]
    total_rows_notifications: NotRequired[int]
    seen_notification_id: NotRequired[int]
    load_more_notifications: NotRequired[str]
