from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UserTips(SdkBaseModel):
    first_notification: int
    topic_timeline: int
    post_menu: int
    topic_notification_levels: int
    suggested_topics: int


class UserTipsDict(TypedDict):
    first_notification: int
    topic_timeline: int
    post_menu: int
    topic_notification_levels: int
    suggested_topics: int
