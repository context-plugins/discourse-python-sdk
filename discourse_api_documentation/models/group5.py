from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Group5(SdkBaseModel):
    id: int
    name: str
    full_name: Optional[str] = UNSET
    display_name: Optional[str] = UNSET
    flair_url: str | None
    flair_bg_color: str | None
    flair_color: str | None
    automatic: bool


class Group5Dict(TypedDict):
    id: int
    name: str
    full_name: NotRequired[str]
    display_name: NotRequired[str]
    flair_url: str | None
    flair_bg_color: str | None
    flair_color: str | None
    automatic: bool
