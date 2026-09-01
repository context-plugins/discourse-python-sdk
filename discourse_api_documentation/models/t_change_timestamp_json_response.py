from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TChangeTimestampJsonResponse(SdkBaseModel):
    success: Optional[str] = UNSET


class TChangeTimestampJsonResponseDict(TypedDict):
    success: NotRequired[str]
