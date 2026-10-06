from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .user import User, UserDict


class Poster4(SdkBaseModel):
    extras: str
    description: str
    user: User


class Poster4Dict(TypedDict):
    extras: str
    description: str
    user: UserDict
