from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Archetype(SdkBaseModel):
    id: str
    name: str
    options: list[Any]


class ArchetypeDict(TypedDict):
    id: str
    name: str
    options: list[Any]
