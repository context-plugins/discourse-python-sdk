from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Owner(SdkBaseModel):
    id: int
    username: str
    name: str | None
    avatar_template: str
    title: str | None
    last_posted_at: str
    last_seen_at: str
    added_at: str
    timezone: str


class OwnerDict(TypedDict):
    id: int
    username: str
    name: str | None
    avatar_template: str
    title: str | None
    last_posted_at: str
    last_seen_at: str
    added_at: str
    timezone: str
