from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ActionsSummary8(SdkBaseModel):
    id: int
    count: int
    hidden: bool
    can_act: bool


class ActionsSummary8Dict(TypedDict):
    id: int
    count: int
    hidden: bool
    can_act: bool
