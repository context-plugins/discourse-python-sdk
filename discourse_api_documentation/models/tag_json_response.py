from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .topic_list3 import TopicList3, TopicList3Dict
from .user2 import User2, User2Dict


class TagJsonResponse(SdkBaseModel):
    users: Optional[list[User2]] = UNSET
    primary_groups: Optional[list[Any]] = UNSET
    topic_list: Optional[TopicList3] = UNSET


class TagJsonResponseDict(TypedDict):
    users: NotRequired[list[User2 | User2Dict]]
    primary_groups: NotRequired[list[Any]]
    topic_list: NotRequired[TopicList3 | TopicList3Dict]
