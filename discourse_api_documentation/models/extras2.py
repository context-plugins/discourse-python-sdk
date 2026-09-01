from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Extras2(SdkBaseModel):
    type_filters: list[Any]


class Extras2Dict(TypedDict):
    type_filters: list[Any]
