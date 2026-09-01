from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .silence import Silence, SilenceDict


class AdminUsersSilenceJsonResponse(SdkBaseModel):
    silence: Silence


class AdminUsersSilenceJsonResponseDict(TypedDict):
    silence: Silence | SilenceDict
