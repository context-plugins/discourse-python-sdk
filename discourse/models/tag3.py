from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Tag3(SdkBaseModel):
    id: Optional[int] = UNSET
    text: Optional[str] = UNSET
    name: Optional[str] = UNSET
    count: Optional[int] = UNSET
    pm_count: Optional[int] = UNSET
    target_tag: OptionalNullable[str] = UNSET


class Tag3Dict(TypedDict):
    id: NotRequired[int]
    text: NotRequired[str]
    name: NotRequired[str]
    count: NotRequired[int]
    pm_count: NotRequired[int]
    target_tag: NotRequired[str | None]
