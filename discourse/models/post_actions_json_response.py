from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .actions_summary5 import ActionsSummary5, ActionsSummary5Dict


class PostActionsJsonResponse(SdkBaseModel):
    id: int
    """The ID of the post"""

    name: str
    """The name of the post author"""

    username: str
    """The username of the post author"""

    avatar_template: str
    """Template for the author's avatar URL"""

    created_at: str
    """When the post was created"""

    cooked: str
    """The HTML content of the post"""

    post_number: int
    """The post number within the topic"""

    post_type: int
    """The type of post"""

    posts_count: int
    """Total posts count for the user"""

    updated_at: str
    """When the post was last updated"""

    reply_count: int
    """Number of replies to this post"""

    reply_to_post_number: str | None
    """Post number this post is replying to"""

    quote_count: int
    """Number of times this post has been quoted"""

    incoming_link_count: int
    """Number of incoming links to this post"""

    reads: int
    """Number of reads"""

    readers_count: int
    """Number of readers"""

    score: float
    """Post score"""

    yours: bool
    """Whether this post belongs to the current user"""

    topic_id: int
    """ID of the topic this post belongs to"""

    topic_slug: str
    """Slug of the topic this post belongs to"""

    display_username: str
    """Display username of the post author"""

    primary_group_name: str | None
    """Primary group name of the author"""

    flair_name: str | None
    """Flair name of the author"""

    flair_url: str | None
    """Flair URL of the author"""

    flair_bg_color: str | None
    """Flair background color of the author"""

    flair_color: str | None
    """Flair color of the author"""

    flair_group_id: int | None
    """Flair group ID of the author"""

    badges_granted: list[Any]
    """Badges granted to the user"""

    version: int
    """Version number of the post"""

    can_edit: bool
    """Whether the current user can edit this post"""

    can_delete: bool
    """Whether the current user can delete this post"""

    can_recover: bool
    """Whether the current user can recover this post"""

    can_see_hidden_post: bool
    """Whether the current user can see hidden posts"""

    can_wiki: bool
    """Whether the current user can wiki this post"""

    user_title: str | None
    """Title of the post author"""

    bookmarked: bool
    """Whether the post is bookmarked by the current user"""

    actions_summary: list[ActionsSummary5]
    """Summary of actions performed on this post"""

    moderator: bool
    """Whether the post author is a moderator"""

    admin: bool
    """Whether the post author is an admin"""

    staff: bool
    """Whether the post author is staff"""

    user_id: int
    """ID of the post author"""

    hidden: bool
    """Whether the post is hidden"""

    trust_level: int
    """Trust level of the post author"""

    deleted_at: str | None
    """When the post was deleted"""

    user_deleted: bool
    """Whether the post was deleted by the user"""

    edit_reason: str | None
    """Reason for the last edit"""

    can_view_edit_history: bool
    """Whether the current user can view edit history"""

    wiki: bool
    """Whether this is a wiki post"""

    reviewable_id: int | None
    """ID of the reviewable if this post is under review"""

    reviewable_score_count: int
    """Number of reviewable scores"""

    reviewable_score_pending_count: int
    """Number of pending reviewable scores"""

    post_url: str
    """URL of the post"""


class PostActionsJsonResponseDict(TypedDict):
    id: int
    name: str
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
    display_username: str
    primary_group_name: str | None
    flair_name: str | None
    flair_url: str | None
    flair_bg_color: str | None
    flair_color: str | None
    flair_group_id: int | None
    badges_granted: list[Any]
    version: int
    can_edit: bool
    can_delete: bool
    can_recover: bool
    can_see_hidden_post: bool
    can_wiki: bool
    user_title: str | None
    bookmarked: bool
    actions_summary: list[ActionsSummary5Dict]
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
    reviewable_id: int | None
    reviewable_score_count: int
    reviewable_score_pending_count: int
    post_url: str
