from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class UserOption(SdkBaseModel):
    user_id: int
    mailing_list_mode: bool
    mailing_list_mode_frequency: int
    email_digests: bool
    email_level: int
    email_messages_level: int
    external_links_in_new_tab: bool
    bookmark_auto_delete_preference: Optional[int] = UNSET
    color_scheme_id: str | None
    dark_scheme_id: str | None
    dynamic_favicon: bool
    enable_quoting: bool
    enable_smart_lists: bool
    enable_markdown_monospace_font: bool
    enable_defer: bool
    digest_after_minutes: int
    automatically_unpin_topics: bool
    auto_track_topics_after_msecs: int
    notification_level_when_replying: int
    new_topic_duration_minutes: int
    email_previous_replies: int
    email_in_reply_to: bool
    like_notification_frequency: int
    notify_on_linked_posts: bool
    push_notification_level: str
    enable_upcoming_change_available_notifications: bool
    include_tl0_in_digests: bool
    theme_ids: list[Any]
    theme_key_seq: int
    allow_private_messages: bool
    enable_allowed_pm_users: bool
    homepage_id: str | None
    hide_profile_and_presence: bool
    hide_profile: bool
    hide_presence: bool
    text_size: str
    text_size_seq: int
    title_count_mode: str
    timezone: str | None
    skip_new_user_tips: bool
    default_calendar: Optional[str] = UNSET
    oldest_search_log_date: OptionalNullable[str] = UNSET
    sidebar_link_to_filtered_list: Optional[bool] = UNSET
    sidebar_show_count_of_new_items: Optional[bool] = UNSET
    watched_precedence_over_muted: Optional[bool] = UNSET
    seen_popups: OptionalNullable[str] = UNSET
    topics_unread_when_closed: bool
    composition_mode: Optional[int] = UNSET
    interface_color_mode: int
    show_original_content: bool


class UserOptionDict(TypedDict):
    user_id: int
    mailing_list_mode: bool
    mailing_list_mode_frequency: int
    email_digests: bool
    email_level: int
    email_messages_level: int
    external_links_in_new_tab: bool
    bookmark_auto_delete_preference: NotRequired[int]
    color_scheme_id: str | None
    dark_scheme_id: str | None
    dynamic_favicon: bool
    enable_quoting: bool
    enable_smart_lists: bool
    enable_markdown_monospace_font: bool
    enable_defer: bool
    digest_after_minutes: int
    automatically_unpin_topics: bool
    auto_track_topics_after_msecs: int
    notification_level_when_replying: int
    new_topic_duration_minutes: int
    email_previous_replies: int
    email_in_reply_to: bool
    like_notification_frequency: int
    notify_on_linked_posts: bool
    push_notification_level: str
    enable_upcoming_change_available_notifications: bool
    include_tl0_in_digests: bool
    theme_ids: list[Any]
    theme_key_seq: int
    allow_private_messages: bool
    enable_allowed_pm_users: bool
    homepage_id: str | None
    hide_profile_and_presence: bool
    hide_profile: bool
    hide_presence: bool
    text_size: str
    text_size_seq: int
    title_count_mode: str
    timezone: str | None
    skip_new_user_tips: bool
    default_calendar: NotRequired[str]
    oldest_search_log_date: NotRequired[str | None]
    sidebar_link_to_filtered_list: NotRequired[bool]
    sidebar_show_count_of_new_items: NotRequired[bool]
    watched_precedence_over_muted: NotRequired[bool]
    seen_popups: NotRequired[str | None]
    topics_unread_when_closed: bool
    composition_mode: NotRequired[int]
    interface_color_mode: int
    show_original_content: bool
