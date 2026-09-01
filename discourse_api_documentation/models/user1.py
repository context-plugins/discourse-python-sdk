from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class User1(SdkBaseModel):
    id: Optional[int] = UNSET
    username: Optional[str] = UNSET
    name: Optional[str] = UNSET
    avatar_template: Optional[str] = UNSET


class User1Dict(TypedDict):
    id: NotRequired[int]
    username: NotRequired[str]
    name: NotRequired[str]
    avatar_template: NotRequired[str]
