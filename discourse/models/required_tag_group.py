from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RequiredTagGroup(SdkBaseModel):
    name: str
    min_count: int


class RequiredTagGroupDict(TypedDict):
    name: str
    min_count: int
