from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GroupUser(SdkBaseModel):
    group_id: int
    user_id: int
    notification_level: int
    owner: Optional[bool] = UNSET


class GroupUserDict(TypedDict):
    group_id: int
    user_id: int
    notification_level: int
    owner: NotRequired[bool]
