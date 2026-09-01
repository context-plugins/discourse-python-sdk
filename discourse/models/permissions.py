from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Permissions(SdkBaseModel):
    everyone: Optional[int] = UNSET
    staff: Optional[int] = UNSET


class PermissionsDict(TypedDict):
    everyone: NotRequired[int]
    staff: NotRequired[int]
