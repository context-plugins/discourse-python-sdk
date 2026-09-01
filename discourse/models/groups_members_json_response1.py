from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GroupsMembersJsonResponse1(SdkBaseModel):
    success: str
    usernames: list[Any]
    emails: list[Any]


class GroupsMembersJsonResponse1Dict(TypedDict):
    success: str
    usernames: list[Any]
    emails: list[Any]
