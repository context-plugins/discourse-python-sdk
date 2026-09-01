from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PenaltyCounts1(SdkBaseModel):
    silenced: int
    suspended: int
    total: int


class PenaltyCounts1Dict(TypedDict):
    silenced: int
    suspended: int
    total: int
