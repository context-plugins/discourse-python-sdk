from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReplyToUser(SdkBaseModel):
    id: Optional[int] = UNSET
    username: str
    name: Optional[str] = UNSET
    avatar_template: str


class ReplyToUserDict(TypedDict):
    id: NotRequired[int]
    username: str
    name: NotRequired[str]
    avatar_template: str
