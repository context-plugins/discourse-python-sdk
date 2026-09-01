from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AdminBackupsJsonResponse(SdkBaseModel):
    filename: str
    size: int
    last_modified: str


class AdminBackupsJsonResponseDict(TypedDict):
    filename: str
    size: int
    last_modified: str
