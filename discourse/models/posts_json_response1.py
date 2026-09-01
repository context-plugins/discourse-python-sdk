from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .actions_summary import ActionsSummary, ActionsSummaryDict


class PostsJsonResponse1(SdkBaseModel):
    id: int
    name: str | None
    username: str
    avatar_template: str
    created_at: str
    raw: Optional[str] = UNSET
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
    display_username: str | None
    primary_group_name: str | None
    flair_name: str | None
    flair_url: str | None
    flair_bg_color: str | None
    flair_color: str | None
    flair_group_id: OptionalNullable[int] = UNSET
    badges_granted: Optional[list[Any]] = UNSET
    version: int
    can_edit: bool
    can_delete: bool
    can_recover: bool
    can_see_hidden_post: Optional[bool] = UNSET
    can_wiki: bool
    user_title: str | None
    bookmarked: bool
    actions_summary: list[ActionsSummary]
    moderator: bool
    admin: bool
    staff: bool
    user_id: int
    draft_sequence: int
    hidden: bool
    trust_level: int
    deleted_at: str | None
    user_deleted: bool
    edit_reason: str | None
    can_view_edit_history: bool
    wiki: bool
    reviewable_id: int | None
    reviewable_score_count: int
    reviewable_score_pending_count: int
    post_url: str
    post_localizations: Optional[list[Any]] = UNSET
    mentioned_users: Optional[list[Any]] = UNSET


class PostsJsonResponse1Dict(TypedDict):
    id: int
    name: str | None
    username: str
    avatar_template: str
    created_at: str
    raw: NotRequired[str]
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
    display_username: str | None
    primary_group_name: str | None
    flair_name: str | None
    flair_url: str | None
    flair_bg_color: str | None
    flair_color: str | None
    flair_group_id: NotRequired[int | None]
    badges_granted: NotRequired[list[Any]]
    version: int
    can_edit: bool
    can_delete: bool
    can_recover: bool
    can_see_hidden_post: NotRequired[bool]
    can_wiki: bool
    user_title: str | None
    bookmarked: bool
    actions_summary: list[ActionsSummary | ActionsSummaryDict]
    moderator: bool
    admin: bool
    staff: bool
    user_id: int
    draft_sequence: int
    hidden: bool
    trust_level: int
    deleted_at: str | None
    user_deleted: bool
    edit_reason: str | None
    can_view_edit_history: bool
    wiki: bool
    reviewable_id: int | None
    reviewable_score_count: int
    reviewable_score_pending_count: int
    post_url: str
    post_localizations: NotRequired[list[Any]]
    mentioned_users: NotRequired[list[Any]]
