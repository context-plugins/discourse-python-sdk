from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Topic5(SdkBaseModel):
    title: Optional[str] = UNSET
    category_id: Optional[int] = UNSET


class Topic5Dict(TypedDict):
    title: NotRequired[str]
    category_id: NotRequired[int]
