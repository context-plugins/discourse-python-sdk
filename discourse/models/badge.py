from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Badge(SdkBaseModel):
    id: int
    name: str
    description: str
    grant_count: int
    allow_title: bool
    multiple_grant: bool
    icon: str
    image_url: str | None
    listable: bool
    enabled: bool
    badge_grouping_id: int
    system: bool
    long_description: str
    slug: str
    manually_grantable: bool
    query: str | None
    trigger: int | None
    target_posts: bool
    auto_revoke: bool
    show_posts: bool
    i18n_name: OptionalNullable[str] = UNSET
    image_upload_id: int | None
    badge_type_id: int
    show_in_post_header: bool


class BadgeDict(TypedDict):
    id: int
    name: str
    description: str
    grant_count: int
    allow_title: bool
    multiple_grant: bool
    icon: str
    image_url: str | None
    listable: bool
    enabled: bool
    badge_grouping_id: int
    system: bool
    long_description: str
    slug: str
    manually_grantable: bool
    query: str | None
    trigger: int | None
    target_posts: bool
    auto_revoke: bool
    show_posts: bool
    i18n_name: NotRequired[str | None]
    image_upload_id: int | None
    badge_type_id: int
    show_in_post_header: bool
