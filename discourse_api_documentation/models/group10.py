from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Group10(SdkBaseModel):
    id: int
    automatic: bool
    name: str
    display_name: str
    user_count: int
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
    flair_group_id: OptionalNullable[int] = UNSET
    bio_raw: str | None
    bio_cooked: str | None
    bio_excerpt: str | None
    public_admission: bool
    public_exit: bool
    allow_membership_requests: bool
    full_name: str | None
    default_notification_level: int
    membership_request_template: str | None
    members_visibility_level: int
    can_see_members: bool
    can_admin_group: bool
    publish_read_state: bool


class Group10Dict(TypedDict):
    id: int
    automatic: bool
    name: str
    display_name: str
    user_count: int
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
    flair_group_id: NotRequired[int | None]
    bio_raw: str | None
    bio_cooked: str | None
    bio_excerpt: str | None
    public_admission: bool
    public_exit: bool
    allow_membership_requests: bool
    full_name: str | None
    default_notification_level: int
    membership_request_template: str | None
    members_visibility_level: int
    can_see_members: bool
    can_admin_group: bool
    publish_read_state: bool
