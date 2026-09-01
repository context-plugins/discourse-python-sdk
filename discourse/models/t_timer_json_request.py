from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TTimerJsonRequest(SdkBaseModel):
    time: Optional[str] = UNSET
    status_type: Optional[str] = UNSET
    based_on_last_post: Optional[bool] = UNSET
    category_id: Optional[int] = UNSET


class TTimerJsonRequestDict(TypedDict):
    time: NotRequired[str]
    status_type: NotRequired[str]
    based_on_last_post: NotRequired[bool]
    category_id: NotRequired[int]
