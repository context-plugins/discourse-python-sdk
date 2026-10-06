from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .topic_list import TopicList, TopicListDict
from .user import User, UserDict


class CJsonResponse(SdkBaseModel):
    users: Optional[list[User]] = UNSET
    primary_groups: Optional[list[Any]] = UNSET
    topic_list: TopicList


class CJsonResponseDict(TypedDict):
    users: NotRequired[list[UserDict]]
    primary_groups: NotRequired[list[Any]]
    topic_list: TopicListDict
