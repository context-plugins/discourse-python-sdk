from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .data import Data, DataDict


class Notification(SdkBaseModel):
    id: Optional[int] = UNSET
    user_id: Optional[int] = UNSET
    notification_type: Optional[int] = UNSET
    read: Optional[bool] = UNSET
    created_at: Optional[str] = UNSET
    post_number: OptionalNullable[int] = UNSET
    topic_id: OptionalNullable[int] = UNSET
    slug: OptionalNullable[str] = UNSET
    data: Optional[Data] = UNSET


class NotificationDict(TypedDict):
    id: NotRequired[int]
    user_id: NotRequired[int]
    notification_type: NotRequired[int]
    read: NotRequired[bool]
    created_at: NotRequired[str]
    post_number: NotRequired[int | None]
    topic_id: NotRequired[int | None]
    slug: NotRequired[str | None]
    data: NotRequired[DataDict]
