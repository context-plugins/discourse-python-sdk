from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .actions_summary import ActionsSummary, ActionsSummaryDict


class LatestPost(SdkBaseModel):
    id: int
    name: str | None
    username: str
    avatar_template: str
    created_at: str
    cooked: str
    post_number: int
    post_type: int
    posts_count: int
    updated_at: str
    reply_count: int
    reply_to_post_number: str | None
    quote_count: int
    incoming_link_count: int
    reads: int
    readers_count: int
    score: float
    yours: bool
    topic_id: int
    topic_slug: str
    topic_title: str
    topic_html_title: str
    category_id: int
    display_username: str | None
    primary_group_name: str | None
    flair_name: str | None
    flair_url: str | None
    flair_bg_color: str | None
    flair_color: str | None
    flair_group_id: str | None
    badges_granted: list[Any]
    version: int
    can_edit: bool
    can_delete: bool
    can_recover: bool
    can_see_hidden_post: bool
    can_wiki: bool
    user_title: str | None
    bookmarked: bool
    raw: str
    actions_summary: list[ActionsSummary]
    moderator: bool
    admin: bool
    staff: bool
    user_id: int
    hidden: bool
    trust_level: int
    deleted_at: str | None
    user_deleted: bool
    edit_reason: str | None
    can_view_edit_history: bool
    wiki: bool
    excerpt: str
    truncated: bool
    reviewable_id: str | None
    reviewable_score_count: int
    reviewable_score_pending_count: int
    post_url: str


class LatestPostDict(TypedDict):
    id: int
    name: str | None
    username: str
    avatar_template: str
    created_at: str
    cooked: str
    post_number: int
    post_type: int
    posts_count: int
    updated_at: str
    reply_count: int
    reply_to_post_number: str | None
    quote_count: int
    incoming_link_count: int
    reads: int
    readers_count: int
    score: float
    yours: bool
    topic_id: int
    topic_slug: str
    topic_title: str
    topic_html_title: str
    category_id: int
    display_username: str | None
    primary_group_name: str | None
    flair_name: str | None
    flair_url: str | None
    flair_bg_color: str | None
    flair_color: str | None
    flair_group_id: str | None
    badges_granted: list[Any]
    version: int
    can_edit: bool
    can_delete: bool
    can_recover: bool
    can_see_hidden_post: bool
    can_wiki: bool
    user_title: str | None
    bookmarked: bool
    raw: str
    actions_summary: list[ActionsSummaryDict]
    moderator: bool
    admin: bool
    staff: bool
    user_id: int
    hidden: bool
    trust_level: int
    deleted_at: str | None
    user_deleted: bool
    edit_reason: str | None
    can_view_edit_history: bool
    wiki: bool
    excerpt: str
    truncated: bool
    reviewable_id: str | None
    reviewable_score_count: int
    reviewable_score_pending_count: int
    post_url: str
