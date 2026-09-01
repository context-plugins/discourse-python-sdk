from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Group1(SdkBaseModel):
    id: int
    automatic: bool
    name: str
    user_count: Optional[int] = UNSET
    mentionable_level: int
    messageable_level: int
    visibility_level: int
    primary_group: bool
    title: str | None
    grant_trust_level: str | None
    incoming_email: str | None
    has_messages: bool
    flair_url: str | None
    flair_bg_color: str | None
    flair_color: str | None
    bio_raw: str | None
    bio_cooked: str | None
    bio_excerpt: str | None
    public_admission: bool
    public_exit: bool
    allow_membership_requests: bool
    full_name: str | None
    default_notification_level: int
    membership_request_template: str | None
    is_group_user: bool
    members_visibility_level: int
    can_see_members: bool
    can_admin_group: bool
    can_edit_group: Optional[bool] = UNSET
    publish_read_state: bool
    is_group_owner_display: bool
    mentionable: bool
    messageable: bool
    automatic_membership_email_domains: str | None
    smtp_updated_at: OptionalNullable[str] = UNSET
    smtp_updated_by: OptionalNullable[Any] = UNSET
    smtp_enabled: Optional[bool] = UNSET
    smtp_server: str | None
    smtp_port: str | None
    smtp_ssl_mode: int | None
    email_username: str | None
    email_from_alias: OptionalNullable[str] = UNSET
    email_password: str | None
    message_count: int
    allow_unknown_sender_topic_replies: bool
    associated_group_ids: Optional[list[Any]] = UNSET
    watching_category_ids: list[Any]
    tracking_category_ids: list[Any]
    watching_first_post_category_ids: list[Any]
    regular_category_ids: list[Any]
    muted_category_ids: list[Any]
    watching_tags: Optional[list[Any]] = UNSET
    watching_first_post_tags: Optional[list[Any]] = UNSET
    tracking_tags: Optional[list[Any]] = UNSET
    regular_tags: Optional[list[Any]] = UNSET
    muted_tags: Optional[list[Any]] = UNSET


class Group1Dict(TypedDict):
    id: int
    automatic: bool
    name: str
    user_count: NotRequired[int]
    mentionable_level: int
    messageable_level: int
    visibility_level: int
    primary_group: bool
    title: str | None
    grant_trust_level: str | None
    incoming_email: str | None
    has_messages: bool
    flair_url: str | None
    flair_bg_color: str | None
    flair_color: str | None
    bio_raw: str | None
    bio_cooked: str | None
    bio_excerpt: str | None
    public_admission: bool
    public_exit: bool
    allow_membership_requests: bool
    full_name: str | None
    default_notification_level: int
    membership_request_template: str | None
    is_group_user: bool
    members_visibility_level: int
    can_see_members: bool
    can_admin_group: bool
    can_edit_group: NotRequired[bool]
    publish_read_state: bool
    is_group_owner_display: bool
    mentionable: bool
    messageable: bool
    automatic_membership_email_domains: str | None
    smtp_updated_at: NotRequired[str | None]
    smtp_updated_by: NotRequired[Any | None]
    smtp_enabled: NotRequired[bool]
    smtp_server: str | None
    smtp_port: str | None
    smtp_ssl_mode: int | None
    email_username: str | None
    email_from_alias: NotRequired[str | None]
    email_password: str | None
    message_count: int
    allow_unknown_sender_topic_replies: bool
    associated_group_ids: NotRequired[list[Any]]
    watching_category_ids: list[Any]
    tracking_category_ids: list[Any]
    watching_first_post_category_ids: list[Any]
    regular_category_ids: list[Any]
    muted_category_ids: list[Any]
    watching_tags: NotRequired[list[Any]]
    watching_first_post_tags: NotRequired[list[Any]]
    tracking_tags: NotRequired[list[Any]]
    regular_tags: NotRequired[list[Any]]
    muted_tags: NotRequired[list[Any]]
