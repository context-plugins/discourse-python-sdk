from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GrantedBy(SdkBaseModel):
    id: int
    username: str
    name: str
    avatar_template: str
    flair_name: str | None
    admin: bool
    moderator: bool
    trust_level: int


class GrantedByDict(TypedDict):
    id: int
    username: str
    name: str
    avatar_template: str
    flair_name: str | None
    admin: bool
    moderator: bool
    trust_level: int
