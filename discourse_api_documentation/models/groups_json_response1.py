from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GroupsJsonResponse1(SdkBaseModel):
    success: str


class GroupsJsonResponse1Dict(TypedDict):
    success: str
