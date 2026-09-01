from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Permissions2(SdkBaseModel):
    everyone: Optional[int] = UNSET


class Permissions2Dict(TypedDict):
    everyone: NotRequired[int]
