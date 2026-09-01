from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class NotificationTypes(SdkBaseModel):
    mentioned: int
    replied: int
    quoted: int
    edited: int
    liked: int
    private_message: int
    invited_to_private_message: int
    invitee_accepted: int
    posted: int
    watching_category_or_tag: int
    new_features: Optional[int] = UNSET
    admin_problems: Optional[int] = UNSET
    moved_post: int
    linked: int
    granted_badge: int
    invited_to_topic: int
    custom: int
    group_mentioned: int
    group_message_summary: int
    watching_first_post: int
    topic_reminder: int
    liked_consolidated: int
    linked_consolidated: int
    post_approved: int
    code_review_commit_approved: int
    membership_request_accepted: int
    membership_request_consolidated: int
    bookmark_reminder: int
    reaction: int
    votes_released: int
    event_reminder: int
    event_invitation: int
    chat_mention: int
    chat_message: int
    chat_invitation: int
    chat_group_mention: int
    chat_quoted: Optional[int] = UNSET
    chat_watched_thread: Optional[int] = UNSET
    upcoming_change_available: Optional[int] = UNSET
    upcoming_change_automatically_promoted: Optional[int] = UNSET
    assigned: Optional[int] = UNSET
    question_answer_user_commented: Optional[int] = UNSET
    following: Optional[int] = UNSET
    following_created_topic: Optional[int] = UNSET
    following_replied: Optional[int] = UNSET
    circles_activity: Optional[int] = UNSET
    boost: Optional[int] = UNSET
    suggested_edit_created: Optional[int] = UNSET
    suggested_edit_accepted: Optional[int] = UNSET


class NotificationTypesDict(TypedDict):
    mentioned: int
    replied: int
    quoted: int
    edited: int
    liked: int
    private_message: int
    invited_to_private_message: int
    invitee_accepted: int
    posted: int
    watching_category_or_tag: int
    new_features: NotRequired[int]
    admin_problems: NotRequired[int]
    moved_post: int
    linked: int
    granted_badge: int
    invited_to_topic: int
    custom: int
    group_mentioned: int
    group_message_summary: int
    watching_first_post: int
    topic_reminder: int
    liked_consolidated: int
    linked_consolidated: int
    post_approved: int
    code_review_commit_approved: int
    membership_request_accepted: int
    membership_request_consolidated: int
    bookmark_reminder: int
    reaction: int
    votes_released: int
    event_reminder: int
    event_invitation: int
    chat_mention: int
    chat_message: int
    chat_invitation: int
    chat_group_mention: int
    chat_quoted: NotRequired[int]
    chat_watched_thread: NotRequired[int]
    upcoming_change_available: NotRequired[int]
    upcoming_change_automatically_promoted: NotRequired[int]
    assigned: NotRequired[int]
    question_answer_user_commented: NotRequired[int]
    following: NotRequired[int]
    following_created_topic: NotRequired[int]
    following_replied: NotRequired[int]
    circles_activity: NotRequired[int]
    boost: NotRequired[int]
    suggested_edit_created: NotRequired[int]
    suggested_edit_accepted: NotRequired[int]
