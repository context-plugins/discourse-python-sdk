from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.notification_level import NotificationLevelOrStr


class TNotificationsJsonRequest(SdkBaseModel):
    notification_level: NotificationLevelOrStr


class TNotificationsJsonRequestDict(TypedDict):
    notification_level: NotificationLevelOrStr
