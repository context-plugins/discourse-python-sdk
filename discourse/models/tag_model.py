from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TagModel(SdkBaseModel):
    id: int
    name: str
    slug: str


class TagModelDict(TypedDict):
    id: int
    name: str
    slug: str
