from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_fields import CustomFields, CustomFieldsDict
from .featured_topic import FeaturedTopic, FeaturedTopicDict
from .group7 import Group7, Group7Dict
from .group_user import GroupUser, GroupUserDict
from .user_auth_token import UserAuthToken, UserAuthTokenDict
from .user_notification_schedule import UserNotificationSchedule, UserNotificationScheduleDict
from .user_option import UserOption, UserOptionDict


class User8(SdkBaseModel):
    id: int
    username: str
    name: str
    avatar_template: str
    last_posted_at: str | None
    last_seen_at: str | None
    created_at: str
    ignored: bool
    muted: bool
    can_ignore_user: bool
    can_ignore_users: Optional[bool] = UNSET
    can_mute_user: bool
    can_mute_users: Optional[bool] = UNSET
    can_send_private_messages: bool
    can_send_private_message_to_user: bool
    trust_level: int
    moderator: bool
    admin: bool
    title: str | None
    badge_count: int
    second_factor_backup_enabled: Optional[bool] = UNSET
    user_fields: Optional[dict[str, str]] = UNSET
    custom_fields: CustomFields
    time_read: int
    recent_time_read: int
    primary_group_id: int | None
    primary_group_name: str | None
    flair_group_id: int | None
    flair_name: str | None
    flair_url: str | None
    flair_bg_color: str | None
    flair_color: str | None
    featured_topic: FeaturedTopic
    staged: bool
    can_edit: bool
    can_edit_username: bool
    can_edit_email: bool
    can_edit_name: bool
    uploaded_avatar_id: int | None
    has_title_badges: bool
    pending_count: int
    pending_posts_count: Optional[int] = UNSET
    profile_view_count: int
    second_factor_enabled: bool
    can_upload_profile_header: bool
    can_upload_user_card_background: bool
    post_count: int
    topic_count: int
    can_be_deleted: bool
    can_delete_all_posts: bool
    locale: str | None
    muted_category_ids: list[Any]
    regular_category_ids: list[Any]
    watched_tags: list[Any]
    watching_first_post_tags: list[Any]
    tracked_tags: list[Any]
    muted_tags: list[Any]
    tracked_category_ids: list[Any]
    watched_category_ids: list[Any]
    watched_first_post_category_ids: list[Any]
    system_avatar_upload_id: str | None
    system_avatar_template: str
    muted_usernames: list[Any]
    ignored_usernames: list[Any]
    allowed_pm_usernames: list[Any]
    mailing_list_posts_per_day: int
    can_change_bio: bool
    can_change_location: bool
    can_change_website: bool
    can_change_tracking_preferences: bool
    user_api_keys: str | None
    user_passkeys: Optional[list[Any]] = UNSET
    sidebar_tags: Optional[list[Any]] = UNSET
    sidebar_category_ids: Optional[list[Any]] = UNSET
    display_sidebar_tags: Optional[bool] = UNSET
    can_pick_theme_with_custom_homepage: Optional[bool] = UNSET
    user_auth_tokens: list[UserAuthToken]
    user_notification_schedule: UserNotificationSchedule
    use_logo_small_as_avatar: bool
    featured_user_badge_ids: list[Any]
    invited_by: str | None
    groups: list[Group7]
    group_users: list[GroupUser]
    user_option: UserOption


class User8Dict(TypedDict):
    id: int
    username: str
    name: str
    avatar_template: str
    last_posted_at: str | None
    last_seen_at: str | None
    created_at: str
    ignored: bool
    muted: bool
    can_ignore_user: bool
    can_ignore_users: NotRequired[bool]
    can_mute_user: bool
    can_mute_users: NotRequired[bool]
    can_send_private_messages: bool
    can_send_private_message_to_user: bool
    trust_level: int
    moderator: bool
    admin: bool
    title: str | None
    badge_count: int
    second_factor_backup_enabled: NotRequired[bool]
    user_fields: NotRequired[dict[str, str]]
    custom_fields: CustomFieldsDict
    time_read: int
    recent_time_read: int
    primary_group_id: int | None
    primary_group_name: str | None
    flair_group_id: int | None
    flair_name: str | None
    flair_url: str | None
    flair_bg_color: str | None
    flair_color: str | None
    featured_topic: FeaturedTopicDict
    staged: bool
    can_edit: bool
    can_edit_username: bool
    can_edit_email: bool
    can_edit_name: bool
    uploaded_avatar_id: int | None
    has_title_badges: bool
    pending_count: int
    pending_posts_count: NotRequired[int]
    profile_view_count: int
    second_factor_enabled: bool
    can_upload_profile_header: bool
    can_upload_user_card_background: bool
    post_count: int
    topic_count: int
    can_be_deleted: bool
    can_delete_all_posts: bool
    locale: str | None
    muted_category_ids: list[Any]
    regular_category_ids: list[Any]
    watched_tags: list[Any]
    watching_first_post_tags: list[Any]
    tracked_tags: list[Any]
    muted_tags: list[Any]
    tracked_category_ids: list[Any]
    watched_category_ids: list[Any]
    watched_first_post_category_ids: list[Any]
    system_avatar_upload_id: str | None
    system_avatar_template: str
    muted_usernames: list[Any]
    ignored_usernames: list[Any]
    allowed_pm_usernames: list[Any]
    mailing_list_posts_per_day: int
    can_change_bio: bool
    can_change_location: bool
    can_change_website: bool
    can_change_tracking_preferences: bool
    user_api_keys: str | None
    user_passkeys: NotRequired[list[Any]]
    sidebar_tags: NotRequired[list[Any]]
    sidebar_category_ids: NotRequired[list[Any]]
    display_sidebar_tags: NotRequired[bool]
    can_pick_theme_with_custom_homepage: NotRequired[bool]
    user_auth_tokens: list[UserAuthTokenDict]
    user_notification_schedule: UserNotificationScheduleDict
    use_logo_small_as_avatar: bool
    featured_user_badge_ids: list[Any]
    invited_by: str | None
    groups: list[Group7Dict]
    group_users: list[GroupUserDict]
    user_option: UserOptionDict
