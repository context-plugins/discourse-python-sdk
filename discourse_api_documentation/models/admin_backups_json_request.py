from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AdminBackupsJsonRequest(SdkBaseModel):
    with_uploads: bool


class AdminBackupsJsonRequestDict(TypedDict):
    with_uploads: bool
