from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class InvitesJsonResponse(SdkBaseModel):
    id: int
    invite_key: str
    link: str
    description: str | None
    email: str
    domain: str | None
    emailed: bool
    can_delete_invite: bool
    custom_message: str | None
    created_at: str
    updated_at: str
    expires_at: str
    expired: bool
    grants_admin: bool
    grants_moderator: bool
    topics: list[Any]
    groups: list[Any]


class InvitesJsonResponseDict(TypedDict):
    id: int
    invite_key: str
    link: str
    description: str | None
    email: str
    domain: str | None
    emailed: bool
    can_delete_invite: bool
    custom_message: str | None
    created_at: str
    updated_at: str
    expires_at: str
    expired: bool
    grants_admin: bool
    grants_moderator: bool
    topics: list[Any]
    groups: list[Any]
