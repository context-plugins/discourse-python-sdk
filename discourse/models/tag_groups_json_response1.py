from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .tag_group1 import TagGroup1, TagGroup1Dict


class TagGroupsJsonResponse1(SdkBaseModel):
    tag_group: TagGroup1


class TagGroupsJsonResponse1Dict(TypedDict):
    tag_group: TagGroup1 | TagGroup1Dict
