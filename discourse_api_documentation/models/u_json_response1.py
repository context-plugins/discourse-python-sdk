from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UJsonResponse1(SdkBaseModel):
    success: str
    user: Any


class UJsonResponse1Dict(TypedDict):
    success: str
    user: Any
