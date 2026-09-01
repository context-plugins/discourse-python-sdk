from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AdminUsersAnonymizeJsonResponse(SdkBaseModel):
    success: str
    username: str


class AdminUsersAnonymizeJsonResponseDict(TypedDict):
    success: str
    username: str
