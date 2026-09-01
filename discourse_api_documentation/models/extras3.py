from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Extras3(SdkBaseModel):
    categories: Optional[list[Any]] = UNSET


class Extras3Dict(TypedDict):
    categories: NotRequired[list[Any]]
