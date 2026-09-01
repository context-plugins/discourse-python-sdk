from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .poster4 import Poster4, Poster4Dict
from .tag import Tag, TagDict


class SuggestedTopic(SdkBaseModel):
    id: int
    title: str
    fancy_title: str
    slug: str
    posts_count: int
    reply_count: int
    highest_post_number: int
    image_url: str | None
    created_at: str
    last_posted_at: str | None
    bumped: bool
    bumped_at: str
    archetype: str
    unseen: bool
    pinned: bool
    unpinned: str | None
    excerpt: str
    visible: bool
    closed: bool
    archived: bool
    bookmarked: str | None
    liked: str | None
    tags: list[Tag]
    tags_descriptions: Any
    like_count: int
    views: int
    category_id: int
    featured_link: str | None
    posters: list[Poster4]


class SuggestedTopicDict(TypedDict):
    id: int
    title: str
    fancy_title: str
    slug: str
    posts_count: int
    reply_count: int
    highest_post_number: int
    image_url: str | None
    created_at: str
    last_posted_at: str | None
    bumped: bool
    bumped_at: str
    archetype: str
    unseen: bool
    pinned: bool
    unpinned: str | None
    excerpt: str
    visible: bool
    closed: bool
    archived: bool
    bookmarked: str | None
    liked: str | None
    tags: list[Tag | TagDict]
    tags_descriptions: Any
    like_count: int
    views: int
    category_id: int
    featured_link: str | None
    posters: list[Poster4 | Poster4Dict]
