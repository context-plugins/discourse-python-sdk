from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ActionsSummary2(SdkBaseModel):
    id: int
    """``2``: like, ``3``, ``4``, ``6``, ``7``, ``8``: flag"""

    count: Optional[int] = UNSET
    acted: Optional[bool] = UNSET
    can_undo: Optional[bool] = UNSET
    can_act: Optional[bool] = UNSET


class ActionsSummary2Dict(TypedDict):
    id: int
    count: NotRequired[int]
    acted: NotRequired[bool]
    can_undo: NotRequired[bool]
    can_act: NotRequired[bool]
