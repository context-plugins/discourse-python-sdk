from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .actions_summary6 import ActionsSummary6, ActionsSummary6Dict


class Post3(SdkBaseModel):
    id: Optional[int] = UNSET
    name: OptionalNullable[str] = UNSET
    username: Optional[str] = UNSET
    avatar_template: Optional[str] = UNSET
    created_at: Optional[str] = UNSET
    cooked: Optional[str] = UNSET
    post_number: Optional[int] = UNSET
    post_type: Optional[int] = UNSET
    updated_at: Optional[str] = UNSET
    reply_count: Optional[int] = UNSET
    reply_to_post_number: OptionalNullable[str] = UNSET
    quote_count: Optional[int] = UNSET
    incoming_link_count: Optional[int] = UNSET
    reads: Optional[int] = UNSET
    readers_count: Optional[int] = UNSET
    score: Optional[float] = UNSET
    yours: Optional[bool] = UNSET
    topic_id: Optional[int] = UNSET
    topic_slug: Optional[str] = UNSET
    display_username: OptionalNullable[str] = UNSET
    primary_group_name: OptionalNullable[str] = UNSET
    flair_name: OptionalNullable[str] = UNSET
    flair_url: OptionalNullable[str] = UNSET
    flair_bg_color: OptionalNullable[str] = UNSET
    flair_color: OptionalNullable[str] = UNSET
    version: Optional[int] = UNSET
    can_edit: Optional[bool] = UNSET
    can_delete: Optional[bool] = UNSET
    can_recover: Optional[bool] = UNSET
    can_wiki: Optional[bool] = UNSET
    read: Optional[bool] = UNSET
    user_title: OptionalNullable[str] = UNSET
    actions_summary: Optional[list[ActionsSummary6]] = UNSET
    moderator: Optional[bool] = UNSET
    admin: Optional[bool] = UNSET
    staff: Optional[bool] = UNSET
    user_id: Optional[int] = UNSET
    hidden: Optional[bool] = UNSET
    trust_level: Optional[int] = UNSET
    deleted_at: OptionalNullable[str] = UNSET
    user_deleted: Optional[bool] = UNSET
    edit_reason: OptionalNullable[str] = UNSET
    can_view_edit_history: Optional[bool] = UNSET
    wiki: Optional[bool] = UNSET
    reviewable_id: Optional[int] = UNSET
    reviewable_score_count: Optional[int] = UNSET
    reviewable_score_pending_count: Optional[int] = UNSET


class Post3Dict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str | None]
    username: NotRequired[str]
    avatar_template: NotRequired[str]
    created_at: NotRequired[str]
    cooked: NotRequired[str]
    post_number: NotRequired[int]
    post_type: NotRequired[int]
    updated_at: NotRequired[str]
    reply_count: NotRequired[int]
    reply_to_post_number: NotRequired[str | None]
    quote_count: NotRequired[int]
    incoming_link_count: NotRequired[int]
    reads: NotRequired[int]
    readers_count: NotRequired[int]
    score: NotRequired[float]
    yours: NotRequired[bool]
    topic_id: NotRequired[int]
    topic_slug: NotRequired[str]
    display_username: NotRequired[str | None]
    primary_group_name: NotRequired[str | None]
    flair_name: NotRequired[str | None]
    flair_url: NotRequired[str | None]
    flair_bg_color: NotRequired[str | None]
    flair_color: NotRequired[str | None]
    version: NotRequired[int]
    can_edit: NotRequired[bool]
    can_delete: NotRequired[bool]
    can_recover: NotRequired[bool]
    can_wiki: NotRequired[bool]
    read: NotRequired[bool]
    user_title: NotRequired[str | None]
    actions_summary: NotRequired[list[ActionsSummary6 | ActionsSummary6Dict]]
    moderator: NotRequired[bool]
    admin: NotRequired[bool]
    staff: NotRequired[bool]
    user_id: NotRequired[int]
    hidden: NotRequired[bool]
    trust_level: NotRequired[int]
    deleted_at: NotRequired[str | None]
    user_deleted: NotRequired[bool]
    edit_reason: NotRequired[str | None]
    can_view_edit_history: NotRequired[bool]
    wiki: NotRequired[bool]
    reviewable_id: NotRequired[int]
    reviewable_score_count: NotRequired[int]
    reviewable_score_pending_count: NotRequired[int]
