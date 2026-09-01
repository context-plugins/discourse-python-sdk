from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UPreferencesUsernameJsonRequest(SdkBaseModel):
    new_username: str


class UPreferencesUsernameJsonRequestDict(TypedDict):
    new_username: str
