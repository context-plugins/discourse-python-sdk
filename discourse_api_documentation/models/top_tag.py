from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TopTag(SdkBaseModel):
    id: int
    name: str
    slug: str


class TopTagDict(TypedDict):
    id: int
    name: str
    slug: str
