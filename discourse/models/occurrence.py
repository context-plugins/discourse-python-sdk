from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Occurrence(SdkBaseModel):
    starts_at: str | None
    ends_at: str | None


class OccurrenceDict(TypedDict):
    starts_at: str | None
    ends_at: str | None
