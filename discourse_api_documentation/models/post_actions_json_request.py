from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PostActionsJsonRequest(SdkBaseModel):
    id: int
    """The ID of the post to perform the action on"""

    post_action_type_id: int
    """The ID of the post action type (e.g., 2 for like)"""

    flag_topic: Optional[bool] = UNSET
    """Whether to flag the entire topic"""


class PostActionsJsonRequestDict(TypedDict):
    id: int
    post_action_type_id: int
    flag_topic: NotRequired[bool]
