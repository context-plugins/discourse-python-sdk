from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LinkCount(SdkBaseModel):
    url: str
    internal: bool
    reflection: bool
    title: str
    clicks: int


class LinkCountDict(TypedDict):
    url: str
    internal: bool
    reflection: bool
    title: str
    clicks: int
