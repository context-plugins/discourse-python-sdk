from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .extras2 import Extras2, Extras2Dict
from .group4 import Group4, Group4Dict


class GroupsJsonResponse2(SdkBaseModel):
    groups: list[Group4]
    extras: Extras2
    total_rows_groups: int
    load_more_groups: str


class GroupsJsonResponse2Dict(TypedDict):
    groups: list[Group4Dict]
    extras: Extras2Dict
    total_rows_groups: int
    load_more_groups: str
