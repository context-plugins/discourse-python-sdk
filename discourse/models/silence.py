from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .silenced_by import SilencedBy, SilencedByDict


class Silence(SdkBaseModel):
    silenced: bool
    silence_reason: str
    full_silence_reason: str
    silenced_till: str
    silenced_at: str
    silenced_by: SilencedBy


class SilenceDict(TypedDict):
    silenced: bool
    silence_reason: str
    full_silence_reason: str
    silenced_till: str
    silenced_at: str
    silenced_by: SilencedByDict
