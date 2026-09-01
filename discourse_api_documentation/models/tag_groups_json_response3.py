from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .tag_group2 import TagGroup2, TagGroup2Dict


class TagGroupsJsonResponse3(SdkBaseModel):
    success: Optional[str] = UNSET
    tag_group: Optional[TagGroup2] = UNSET


class TagGroupsJsonResponse3Dict(TypedDict):
    success: NotRequired[str]
    tag_group: NotRequired[TagGroup2 | TagGroup2Dict]
