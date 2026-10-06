from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .topic_list5 import TopicList5, TopicList5Dict
from .user1 import User1, User1Dict


class TopJsonResponse(SdkBaseModel):
    users: Optional[list[User1]] = UNSET
    primary_groups: Optional[list[Any]] = UNSET
    topic_list: Optional[TopicList5] = UNSET


class TopJsonResponseDict(TypedDict):
    users: NotRequired[list[User1Dict]]
    primary_groups: NotRequired[list[Any]]
    topic_list: NotRequired[TopicList5Dict]
