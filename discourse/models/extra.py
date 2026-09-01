from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Extra(SdkBaseModel):
    categories: OptionalNullable[str] = UNSET


class ExtraDict(TypedDict):
    categories: NotRequired[str | None]
