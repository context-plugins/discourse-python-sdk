from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsersJsonResponse(SdkBaseModel):
    success: bool
    active: bool
    message: str
    user_id: Optional[int] = UNSET


class UsersJsonResponseDict(TypedDict):
    success: bool
    active: bool
    message: str
    user_id: NotRequired[int]
