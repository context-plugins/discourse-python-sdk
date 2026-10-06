from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .topic2 import Topic2, Topic2Dict


class TopicList1(SdkBaseModel):
    can_create_topic: Optional[bool] = UNSET
    draft: OptionalNullable[str] = UNSET
    draft_key: Optional[str] = UNSET
    draft_sequence: Optional[int] = UNSET
    per_page: Optional[int] = UNSET
    topics: Optional[list[Topic2]] = UNSET


class TopicList1Dict(TypedDict):
    can_create_topic: NotRequired[bool]
    draft: NotRequired[str | None]
    draft_key: NotRequired[str]
    draft_sequence: NotRequired[int]
    per_page: NotRequired[int]
    topics: NotRequired[list[Topic2Dict]]
