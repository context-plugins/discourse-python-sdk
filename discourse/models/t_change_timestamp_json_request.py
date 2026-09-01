from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TChangeTimestampJsonRequest(SdkBaseModel):
    timestamp: str


class TChangeTimestampJsonRequestDict(TypedDict):
    timestamp: str
