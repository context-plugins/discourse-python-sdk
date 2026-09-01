from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Badge1(SdkBaseModel):
    id: int
    name: str
    description: str
    grant_count: int
    allow_title: bool
    multiple_grant: bool
    icon: str
    image_url: str | None
    image_upload_id: int | None
    listable: bool
    enabled: bool
    badge_grouping_id: int
    system: bool
    long_description: str
    slug: str
    manually_grantable: bool
    query: str | None
    trigger: str | None
    target_posts: bool
    auto_revoke: bool
    show_posts: bool
    badge_type_id: int
    show_in_post_header: bool


class Badge1Dict(TypedDict):
    id: int
    name: str
    description: str
    grant_count: int
    allow_title: bool
    multiple_grant: bool
    icon: str
    image_url: str | None
    image_upload_id: int | None
    listable: bool
    enabled: bool
    badge_grouping_id: int
    system: bool
    long_description: str
    slug: str
    manually_grantable: bool
    query: str | None
    trigger: str | None
    target_posts: bool
    auto_revoke: bool
    show_posts: bool
    badge_type_id: int
    show_in_post_header: bool
