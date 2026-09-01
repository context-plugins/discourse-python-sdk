from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UsersPasswordResetJsonRequest(SdkBaseModel):
    username: str
    password: str


class UsersPasswordResetJsonRequestDict(TypedDict):
    username: str
    password: str
