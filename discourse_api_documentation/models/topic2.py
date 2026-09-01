from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .participant import Participant, ParticipantDict
from .poster1 import Poster1, Poster1Dict


class Topic2(SdkBaseModel):
    id: Optional[int] = UNSET
    title: Optional[str] = UNSET
    fancy_title: Optional[str] = UNSET
    slug: Optional[str] = UNSET
    posts_count: Optional[int] = UNSET
    reply_count: Optional[int] = UNSET
    highest_post_number: Optional[int] = UNSET
    image_url: OptionalNullable[str] = UNSET
    created_at: Optional[str] = UNSET
    last_posted_at: Optional[str] = UNSET
    bumped: Optional[bool] = UNSET
    bumped_at: Optional[str] = UNSET
    archetype: Optional[str] = UNSET
    unseen: Optional[bool] = UNSET
    last_read_post_number: Optional[int] = UNSET
    unread_posts: Optional[int] = UNSET
    pinned: Optional[bool] = UNSET
    unpinned: OptionalNullable[str] = UNSET
    visible: Optional[bool] = UNSET
    closed: Optional[bool] = UNSET
    archived: Optional[bool] = UNSET
    notification_level: Optional[int] = UNSET
    bookmarked: Optional[bool] = UNSET
    liked: Optional[bool] = UNSET
    views: Optional[int] = UNSET
    like_count: Optional[int] = UNSET
    has_summary: Optional[bool] = UNSET
    last_poster_username: Optional[str] = UNSET
    category_id: OptionalNullable[str] = UNSET
    pinned_globally: Optional[bool] = UNSET
    featured_link: OptionalNullable[str] = UNSET
    allowed_user_count: Optional[int] = UNSET
    posters: Optional[list[Poster1]] = UNSET
    participants: Optional[list[Participant]] = UNSET


class Topic2Dict(TypedDict):
    id: NotRequired[int]
    title: NotRequired[str]
    fancy_title: NotRequired[str]
    slug: NotRequired[str]
    posts_count: NotRequired[int]
    reply_count: NotRequired[int]
    highest_post_number: NotRequired[int]
    image_url: NotRequired[str | None]
    created_at: NotRequired[str]
    last_posted_at: NotRequired[str]
    bumped: NotRequired[bool]
    bumped_at: NotRequired[str]
    archetype: NotRequired[str]
    unseen: NotRequired[bool]
    last_read_post_number: NotRequired[int]
    unread_posts: NotRequired[int]
    pinned: NotRequired[bool]
    unpinned: NotRequired[str | None]
    visible: NotRequired[bool]
    closed: NotRequired[bool]
    archived: NotRequired[bool]
    notification_level: NotRequired[int]
    bookmarked: NotRequired[bool]
    liked: NotRequired[bool]
    views: NotRequired[int]
    like_count: NotRequired[int]
    has_summary: NotRequired[bool]
    last_poster_username: NotRequired[str]
    category_id: NotRequired[str | None]
    pinned_globally: NotRequired[bool]
    featured_link: NotRequired[str | None]
    allowed_user_count: NotRequired[int]
    posters: NotRequired[list[Poster1 | Poster1Dict]]
    participants: NotRequired[list[Participant | ParticipantDict]]
