from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TStatusJsonResponse(SdkBaseModel):
    success: Optional[str] = UNSET
    topic_status_update: OptionalNullable[str] = UNSET


class TStatusJsonResponseDict(TypedDict):
    success: NotRequired[str]
    topic_status_update: NotRequired[str | None]
