from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .parent_tag import ParentTag, ParentTagDict
from .tag_model import TagModel, TagModelDict


class TagGroup1(SdkBaseModel):
    id: int
    name: str
    tags: list[TagModel]
    parent_tag: list[ParentTag]
    one_per_topic: bool
    permissions: Any


class TagGroup1Dict(TypedDict):
    id: int
    name: str
    tags: list[TagModelDict]
    parent_tag: list[ParentTagDict]
    one_per_topic: bool
    permissions: Any
