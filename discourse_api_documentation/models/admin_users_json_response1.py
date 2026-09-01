from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AdminUsersJsonResponse1(SdkBaseModel):
    deleted: bool


class AdminUsersJsonResponse1Dict(TypedDict):
    deleted: bool
