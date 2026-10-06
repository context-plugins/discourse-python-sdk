from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .user8 import User8, User8Dict


class UJsonResponse(SdkBaseModel):
    user_badges: list[Any]
    user: User8


class UJsonResponseDict(TypedDict):
    user_badges: list[Any]
    user: User8Dict
