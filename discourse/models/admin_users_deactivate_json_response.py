from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AdminUsersDeactivateJsonResponse(SdkBaseModel):
    success: str


class AdminUsersDeactivateJsonResponseDict(TypedDict):
    success: str
