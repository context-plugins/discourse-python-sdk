from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .parent_tag import ParentTag, ParentTagDict
from .tag import Tag, TagDict


class TagGroup(SdkBaseModel):
    id: int
    name: str
    tags: list[Tag]
    parent_tag: list[ParentTag]
    one_per_topic: bool
    permissions: dict[str, int]


class TagGroupDict(TypedDict):
    id: int
    name: str
    tags: list[Tag | TagDict]
    parent_tag: list[ParentTag | ParentTagDict]
    one_per_topic: bool
    permissions: dict[str, int]
