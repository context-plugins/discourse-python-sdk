from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .tag_group2 import TagGroup2, TagGroup2Dict


class TagGroupsJsonResponse2(SdkBaseModel):
    tag_group: Optional[TagGroup2] = UNSET


class TagGroupsJsonResponse2Dict(TypedDict):
    tag_group: NotRequired[TagGroup2 | TagGroup2Dict]
