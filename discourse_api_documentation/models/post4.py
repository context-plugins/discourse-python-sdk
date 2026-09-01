from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .actions_summary import ActionsSummary, ActionsSummaryDict
from .link_count import LinkCount, LinkCountDict


class Post4(SdkBaseModel):
    id: int
    name: str
    username: str
    avatar_template: str
    created_at: str
    cooked: str
    post_number: int
    post_type: int
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
    display_username: str
    primary_group_name: str | None
    flair_name: str | None
    flair_url: str | None
    flair_bg_color: str | None
    flair_color: str | None
    version: int
    can_edit: bool
    can_delete: bool
    can_recover: bool
    can_see_hidden_post: Optional[bool] = UNSET
    can_wiki: bool
    link_counts: list[LinkCount]
    read: bool
    user_title: str | None
    bookmarked: bool
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
    reviewable_id: int
    reviewable_score_count: int
    reviewable_score_pending_count: int


class Post4Dict(TypedDict):
    id: int
    name: str
    username: str
    avatar_template: str
    created_at: str
    cooked: str
    post_number: int
    post_type: int
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
    display_username: str
    primary_group_name: str | None
    flair_name: str | None
    flair_url: str | None
    flair_bg_color: str | None
    flair_color: str | None
    version: int
    can_edit: bool
    can_delete: bool
    can_recover: bool
    can_see_hidden_post: NotRequired[bool]
    can_wiki: bool
    link_counts: list[LinkCount | LinkCountDict]
    read: bool
    user_title: str | None
    bookmarked: bool
    actions_summary: list[ActionsSummary | ActionsSummaryDict]
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
    reviewable_id: int
    reviewable_score_count: int
    reviewable_score_pending_count: int
