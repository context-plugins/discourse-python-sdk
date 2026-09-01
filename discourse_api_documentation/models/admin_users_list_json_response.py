from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdminUsersListJsonResponse(SdkBaseModel):
    id: int
    username: str
    name: str | None
    avatar_template: str
    email: Optional[str] = UNSET
    secondary_emails: Optional[list[Any]] = UNSET
    active: bool
    admin: bool
    moderator: bool
    last_seen_at: str | None
    last_emailed_at: str | None
    created_at: str
    last_seen_age: float | None
    last_emailed_age: float | None
    created_at_age: float | None
    trust_level: int
    manual_locked_trust_level: str | None
    title: str | None
    time_read: int
    staged: bool
    days_visited: int
    posts_read_count: int
    topics_entered: int
    post_count: int


class AdminUsersListJsonResponseDict(TypedDict):
    id: int
    username: str
    name: str | None
    avatar_template: str
    email: NotRequired[str]
    secondary_emails: NotRequired[list[Any]]
    active: bool
    admin: bool
    moderator: bool
    last_seen_at: str | None
    last_emailed_at: str | None
    created_at: str
    last_seen_age: float | None
    last_emailed_age: float | None
    created_at_age: float | None
    trust_level: int
    manual_locked_trust_level: str | None
    title: str | None
    time_read: int
    staged: bool
    days_visited: int
    posts_read_count: int
    topics_entered: int
    post_count: int
