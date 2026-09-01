from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .topic_list1 import TopicList1, TopicList1Dict
from .user1 import User1, User1Dict


class TopicsPrivateMessagesJsonResponse(SdkBaseModel):
    users: Optional[list[User1]] = UNSET
    primary_groups: Optional[list[Any]] = UNSET
    topic_list: Optional[TopicList1] = UNSET


class TopicsPrivateMessagesJsonResponseDict(TypedDict):
    users: NotRequired[list[User1 | User1Dict]]
    primary_groups: NotRequired[list[Any]]
    topic_list: NotRequired[TopicList1 | TopicList1Dict]
