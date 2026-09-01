from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UPreferencesAvatarPickJsonResponse(SdkBaseModel):
    success: str


class UPreferencesAvatarPickJsonResponseDict(TypedDict):
    success: str
