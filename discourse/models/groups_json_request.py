from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .group import Group, GroupDict


class GroupsJsonRequest(SdkBaseModel):
    group: Group


class GroupsJsonRequestDict(TypedDict):
    group: GroupDict
