from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TTimerJsonResponse(SdkBaseModel):
    success: Optional[str] = UNSET
    execute_at: Optional[str] = UNSET
    duration: OptionalNullable[str] = UNSET
    based_on_last_post: Optional[bool] = UNSET
    closed: Optional[bool] = UNSET
    category_id: OptionalNullable[int] = UNSET


class TTimerJsonResponseDict(TypedDict):
    success: NotRequired[str]
    execute_at: NotRequired[str]
    duration: NotRequired[str | None]
    based_on_last_post: NotRequired[bool]
    closed: NotRequired[bool]
    category_id: NotRequired[int | None]
