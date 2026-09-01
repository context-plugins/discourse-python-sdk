from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.enabled import EnabledOrStr
from .enums.status1 import Status1OrStr


class TStatusJsonRequest(SdkBaseModel):
    status: Status1OrStr
    enabled: EnabledOrStr
    until: Optional[str] = UNSET
    """Only required for ``pinned`` and ``pinned_globally``"""


class TStatusJsonRequestDict(TypedDict):
    status: Status1OrStr
    enabled: EnabledOrStr
    until: NotRequired[str]
