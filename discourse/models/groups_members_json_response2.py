from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GroupsMembersJsonResponse2(SdkBaseModel):
    success: str
    usernames: list[Any]
    skipped_usernames: list[Any]


class GroupsMembersJsonResponse2Dict(TypedDict):
    success: str
    usernames: list[Any]
    skipped_usernames: list[Any]
