from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ActionsSummary5(SdkBaseModel):
    id: Optional[int] = UNSET
    """ID of the action type (e.g., 2 for like)"""

    count: Optional[int] = UNSET
    """Number of times this action has been performed"""

    acted: Optional[bool] = UNSET
    """Whether the current user has performed this action"""

    can_undo: Optional[bool] = UNSET
    """Whether the current user can undo this action"""

    can_act: Optional[bool] = UNSET
    """Whether the current user can perform this action"""


class ActionsSummary5Dict(TypedDict):
    id: NotRequired[int]
    count: NotRequired[int]
    acted: NotRequired[bool]
    can_undo: NotRequired[bool]
    can_act: NotRequired[bool]
