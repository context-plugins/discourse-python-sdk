from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Meta(SdkBaseModel):
    total: int
    limit: int
    offset: int


class MetaDict(TypedDict):
    total: int
    limit: int
    offset: int
