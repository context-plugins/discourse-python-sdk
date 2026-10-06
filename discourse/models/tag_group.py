from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .parent_tag import ParentTag, ParentTagDict
from .tag_model import TagModel, TagModelDict


class TagGroup(SdkBaseModel):
    id: int
    name: str
    tags: list[TagModel]
    parent_tag: list[ParentTag]
    one_per_topic: bool
    permissions: dict[str, int]


class TagGroupDict(TypedDict):
    id: int
    name: str
    tags: list[TagModelDict]
    parent_tag: list[ParentTagDict]
    one_per_topic: bool
    permissions: dict[str, int]
