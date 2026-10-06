from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .actions_summary8 import ActionsSummary8, ActionsSummary8Dict
from .details import Details, DetailsDict
from .post_stream1 import PostStream1, PostStream1Dict
from .suggested_topic import SuggestedTopic, SuggestedTopicDict
from .tag_model import TagModel, TagModelDict


class TJsonResponse(SdkBaseModel):
    post_stream: PostStream1
    timeline_lookup: list[Any]
    suggested_topics: list[SuggestedTopic]
    tags: list[TagModel]
    tags_descriptions: Any
    id: int
    title: str
    fancy_title: str
    posts_count: int
    created_at: str
    views: int
    reply_count: int
    like_count: int
    last_posted_at: str | None
    visible: bool
    closed: bool
    archived: bool
    has_summary: bool
    archetype: str
    slug: str
    category_id: int
    word_count: int | None
    deleted_at: str | None
    user_id: int
    featured_link: str | None
    pinned_globally: bool
    pinned_at: str | None
    pinned_until: str | None
    image_url: str | None
    slow_mode_seconds: int
    draft: str | None
    draft_key: str
    draft_sequence: int
    unpinned: str | None
    pinned: bool
    current_post_number: Optional[int] = UNSET
    highest_post_number: int | None
    deleted_by: str | None
    has_deleted: bool
    actions_summary: list[ActionsSummary8]
    chunk_size: int
    bookmarked: bool
    bookmarks: list[Any]
    topic_timer: str | None
    message_bus_last_id: int
    participant_count: int
    show_read_indicator: bool
    thumbnails: str | None
    slow_mode_enabled_until: str | None
    details: Details


class TJsonResponseDict(TypedDict):
    post_stream: PostStream1Dict
    timeline_lookup: list[Any]
    suggested_topics: list[SuggestedTopicDict]
    tags: list[TagModelDict]
    tags_descriptions: Any
    id: int
    title: str
    fancy_title: str
    posts_count: int
    created_at: str
    views: int
    reply_count: int
    like_count: int
    last_posted_at: str | None
    visible: bool
    closed: bool
    archived: bool
    has_summary: bool
    archetype: str
    slug: str
    category_id: int
    word_count: int | None
    deleted_at: str | None
    user_id: int
    featured_link: str | None
    pinned_globally: bool
    pinned_at: str | None
    pinned_until: str | None
    image_url: str | None
    slow_mode_seconds: int
    draft: str | None
    draft_key: str
    draft_sequence: int
    unpinned: str | None
    pinned: bool
    current_post_number: NotRequired[int]
    highest_post_number: int | None
    deleted_by: str | None
    has_deleted: bool
    actions_summary: list[ActionsSummary8Dict]
    chunk_size: int
    bookmarked: bool
    bookmarks: list[Any]
    topic_timer: str | None
    message_bus_last_id: int
    participant_count: int
    show_read_indicator: bool
    thumbnails: str | None
    slow_mode_enabled_until: str | None
    details: DetailsDict
