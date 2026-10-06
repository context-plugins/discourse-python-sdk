from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .tag_group import TagGroup, TagGroupDict


class TagGroupsJsonResponse(SdkBaseModel):
    tag_groups: list[TagGroup]


class TagGroupsJsonResponseDict(TypedDict):
    tag_groups: list[TagGroupDict]
