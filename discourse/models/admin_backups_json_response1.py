from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AdminBackupsJsonResponse1(SdkBaseModel):
    success: str


class AdminBackupsJsonResponse1Dict(TypedDict):
    success: str
