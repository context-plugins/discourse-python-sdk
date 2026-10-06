from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .user11 import User11, User11Dict


class DirectoryItem(SdkBaseModel):
    id: int
    likes_received: int
    likes_given: int
    topics_entered: int
    topic_count: int
    post_count: int
    posts_read: int
    days_visited: int
    user: User11


class DirectoryItemDict(TypedDict):
    id: int
    likes_received: int
    likes_given: int
    topics_entered: int
    topic_count: int
    post_count: int
    posts_read: int
    days_visited: int
    user: User11Dict
