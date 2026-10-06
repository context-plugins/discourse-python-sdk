from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .top_tag import TopTag, TopTagDict
from .topic1 import Topic1, Topic1Dict


class TopicList(SdkBaseModel):
    can_create_topic: bool
    per_page: int
    top_tags: Optional[list[TopTag]] = UNSET
    topics: list[Topic1]


class TopicListDict(TypedDict):
    can_create_topic: bool
    per_page: int
    top_tags: NotRequired[list[TopTagDict]]
    topics: list[Topic1Dict]
