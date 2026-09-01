from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .topic7 import Topic7, Topic7Dict


class TopicList5(SdkBaseModel):
    can_create_topic: Optional[bool] = UNSET
    draft: OptionalNullable[str] = UNSET
    draft_key: Optional[str] = UNSET
    draft_sequence: Optional[int] = UNSET
    for_period: Optional[str] = UNSET
    per_page: Optional[int] = UNSET
    topics: Optional[list[Topic7]] = UNSET


class TopicList5Dict(TypedDict):
    can_create_topic: NotRequired[bool]
    draft: NotRequired[str | None]
    draft_key: NotRequired[str]
    draft_sequence: NotRequired[int]
    for_period: NotRequired[str]
    per_page: NotRequired[int]
    topics: NotRequired[list[Topic7 | Topic7Dict]]
