from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Data(SdkBaseModel):
    badge_id: Optional[int] = UNSET
    badge_name: Optional[str] = UNSET
    badge_slug: Optional[str] = UNSET
    badge_title: Optional[bool] = UNSET
    username: Optional[str] = UNSET


class DataDict(TypedDict):
    badge_id: NotRequired[int]
    badge_name: NotRequired[str]
    badge_slug: NotRequired[str]
    badge_title: NotRequired[bool]
    username: NotRequired[str]
