from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .poster import Poster, PosterDict


class Topic1(SdkBaseModel):
    id: int
    title: str
    fancy_title: str
    slug: str
    posts_count: int
    reply_count: int
    highest_post_number: int
    image_url: str | None
    created_at: str
    last_posted_at: str
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
    views: int
    like_count: int
    has_summary: bool
    last_poster_username: str
    category_id: int
    pinned_globally: bool
    featured_link: str | None
    posters: list[Poster]


class Topic1Dict(TypedDict):
    id: int
    title: str
    fancy_title: str
    slug: str
    posts_count: int
    reply_count: int
    highest_post_number: int
    image_url: str | None
    created_at: str
    last_posted_at: str
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
    views: int
    like_count: int
    has_summary: bool
    last_poster_username: str
    category_id: int
    pinned_globally: bool
    featured_link: str | None
    posters: list[Poster | PosterDict]
