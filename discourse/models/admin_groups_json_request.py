from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .group import Group, GroupDict


class AdminGroupsJsonRequest(SdkBaseModel):
    group: Group


class AdminGroupsJsonRequestDict(TypedDict):
    group: GroupDict
