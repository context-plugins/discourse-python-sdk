from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Participant1(SdkBaseModel):
    id: int
    username: str
    name: str
    avatar_template: str
    post_count: int
    primary_group_name: str | None
    flair_name: str | None
    flair_url: str | None
    flair_color: str | None
    flair_bg_color: str | None
    flair_group_id: OptionalNullable[int] = UNSET
    admin: bool
    moderator: bool
    trust_level: int


class Participant1Dict(TypedDict):
    id: int
    username: str
    name: str
    avatar_template: str
    post_count: int
    primary_group_name: str | None
    flair_name: str | None
    flair_url: str | None
    flair_color: str | None
    flair_bg_color: str | None
    flair_group_id: NotRequired[int | None]
    admin: bool
    moderator: bool
    trust_level: int
