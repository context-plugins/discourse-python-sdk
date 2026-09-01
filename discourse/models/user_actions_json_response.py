from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .user_action import UserAction, UserActionDict


class UserActionsJsonResponse(SdkBaseModel):
    user_actions: list[UserAction]


class UserActionsJsonResponseDict(TypedDict):
    user_actions: list[UserAction | UserActionDict]
