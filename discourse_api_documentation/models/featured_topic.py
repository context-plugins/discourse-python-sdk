from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FeaturedTopic(SdkBaseModel):
    id: int
    title: str
    fancy_title: str
    slug: str
    posts_count: int


class FeaturedTopicDict(TypedDict):
    id: int
    title: str
    fancy_title: str
    slug: str
    posts_count: int
