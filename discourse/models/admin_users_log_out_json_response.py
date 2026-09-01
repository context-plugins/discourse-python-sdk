from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AdminUsersLogOutJsonResponse(SdkBaseModel):
    success: str


class AdminUsersLogOutJsonResponseDict(TypedDict):
    success: str
