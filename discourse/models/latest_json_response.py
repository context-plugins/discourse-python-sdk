from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .topic_list4 import TopicList4, TopicList4Dict
from .user2 import User2, User2Dict


class LatestJsonResponse(SdkBaseModel):
    users: Optional[list[User2]] = UNSET
    primary_groups: Optional[list[Any]] = UNSET
    topic_list: Optional[TopicList4] = UNSET


class LatestJsonResponseDict(TypedDict):
    users: NotRequired[list[User2Dict]]
    primary_groups: NotRequired[list[Any]]
    topic_list: NotRequired[TopicList4Dict]
