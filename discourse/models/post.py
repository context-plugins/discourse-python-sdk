from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .topic import Topic, TopicDict


class Post(SdkBaseModel):
    id: int
    post_number: int
    url: str
    category_slug: str
    topic: Topic


class PostDict(TypedDict):
    id: int
    post_number: int
    url: str
    category_slug: str
    topic: TopicDict
