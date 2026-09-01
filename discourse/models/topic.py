from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Topic(SdkBaseModel):
    id: int
    title: str
    tags: list[str]
    tags_descriptions: Any
    slug: str


class TopicDict(TypedDict):
    id: int
    title: str
    tags: list[str]
    tags_descriptions: Any
    slug: str
