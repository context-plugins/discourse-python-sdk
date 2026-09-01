from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Extras(SdkBaseModel):
    visible_group_names: list[Any]


class ExtrasDict(TypedDict):
    visible_group_names: list[Any]
