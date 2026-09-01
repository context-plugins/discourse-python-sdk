from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Tag(SdkBaseModel):
    id: int
    name: str
    slug: str


class TagDict(TypedDict):
    id: int
    name: str
    slug: str
