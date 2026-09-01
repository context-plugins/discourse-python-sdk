from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GroupPermission(SdkBaseModel):
    permission_type: int
    group_name: str
    group_id: int


class GroupPermissionDict(TypedDict):
    permission_type: int
    group_name: str
    group_id: int
