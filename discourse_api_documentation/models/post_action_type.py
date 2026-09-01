from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PostActionType(SdkBaseModel):
    id: int | None
    name_key: str | None
    name: str
    description: str
    short_description: str
    is_flag: bool
    require_message: bool
    enabled: bool
    applies_to: list[Any]
    is_used: bool
    position: Optional[int] = UNSET
    auto_action_type: bool
    system: Optional[bool] = UNSET


class PostActionTypeDict(TypedDict):
    id: int | None
    name_key: str | None
    name: str
    description: str
    short_description: str
    is_flag: bool
    require_message: bool
    enabled: bool
    applies_to: list[Any]
    is_used: bool
    position: NotRequired[int]
    auto_action_type: bool
    system: NotRequired[bool]
