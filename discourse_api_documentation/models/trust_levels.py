from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TrustLevels(SdkBaseModel):
    newuser: int
    basic: int
    member: int
    regular: int
    leader: int


class TrustLevelsDict(TypedDict):
    newuser: int
    basic: int
    member: int
    regular: int
    leader: int
