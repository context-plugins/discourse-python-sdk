from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .topic_list2 import TopicList2, TopicList2Dict
from .user2 import User2, User2Dict


class TopicsPrivateMessagesSentJsonResponse(SdkBaseModel):
    users: Optional[list[User2]] = UNSET
    primary_groups: Optional[list[Any]] = UNSET
    topic_list: Optional[TopicList2] = UNSET


class TopicsPrivateMessagesSentJsonResponseDict(TypedDict):
    users: NotRequired[list[User2Dict]]
    primary_groups: NotRequired[list[Any]]
    topic_list: NotRequired[TopicList2Dict]
