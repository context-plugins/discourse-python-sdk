from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .tag4 import Tag4, Tag4Dict
from .topic4 import Topic4, Topic4Dict


class TopicList3(SdkBaseModel):
    can_create_topic: Optional[bool] = UNSET
    draft: OptionalNullable[str] = UNSET
    draft_key: Optional[str] = UNSET
    draft_sequence: Optional[int] = UNSET
    per_page: Optional[int] = UNSET
    tags: Optional[list[Tag4]] = UNSET
    topics: Optional[list[Topic4]] = UNSET


class TopicList3Dict(TypedDict):
    can_create_topic: NotRequired[bool]
    draft: NotRequired[str | None]
    draft_key: NotRequired[str]
    draft_sequence: NotRequired[int]
    per_page: NotRequired[int]
    tags: NotRequired[list[Tag4Dict]]
    topics: NotRequired[list[Topic4Dict]]
