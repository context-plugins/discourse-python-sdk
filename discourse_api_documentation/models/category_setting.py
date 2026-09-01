from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class CategorySetting(SdkBaseModel):
    auto_bump_cooldown_days: Optional[int] = UNSET
    num_auto_bump_daily: OptionalNullable[int] = UNSET
    require_reply_approval: OptionalNullable[bool] = UNSET
    require_topic_approval: OptionalNullable[bool] = UNSET
    nested_replies_default: OptionalNullable[bool] = UNSET
    topic_posting_review_mode: Optional[str] = UNSET
    reply_posting_review_mode: Optional[str] = UNSET


class CategorySettingDict(TypedDict):
    auto_bump_cooldown_days: NotRequired[int]
    num_auto_bump_daily: NotRequired[int | None]
    require_reply_approval: NotRequired[bool | None]
    require_topic_approval: NotRequired[bool | None]
    nested_replies_default: NotRequired[bool | None]
    topic_posting_review_mode: NotRequired[str]
    reply_posting_review_mode: NotRequired[str]
