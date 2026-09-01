from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ParentTag(SdkBaseModel):
    id: int
    name: str
    slug: str


class ParentTagDict(TypedDict):
    id: int
    name: str
    slug: str
