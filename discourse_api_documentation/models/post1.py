from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Post1(SdkBaseModel):
    raw: str
    edit_reason: Optional[str] = UNSET


class Post1Dict(TypedDict):
    raw: str
    edit_reason: NotRequired[str]
