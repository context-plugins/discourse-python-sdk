from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Badge3(SdkBaseModel):
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
    slug: str
    manually_grantable: bool
    badge_type_id: int


class Badge3Dict(TypedDict):
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
    slug: str
    manually_grantable: bool
    badge_type_id: int
