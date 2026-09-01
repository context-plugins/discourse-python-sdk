from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AdminGroupsJsonResponse1(SdkBaseModel):
    success: str


class AdminGroupsJsonResponse1Dict(TypedDict):
    success: str
