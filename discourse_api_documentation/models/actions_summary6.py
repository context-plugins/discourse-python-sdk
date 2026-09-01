from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ActionsSummary6(SdkBaseModel):
    id: Optional[int] = UNSET
    can_act: Optional[bool] = UNSET


class ActionsSummary6Dict(TypedDict):
    id: NotRequired[int]
    can_act: NotRequired[bool]
