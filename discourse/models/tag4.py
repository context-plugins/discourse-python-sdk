from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Tag4(SdkBaseModel):
    id: Optional[int] = UNSET
    name: Optional[str] = UNSET
    topic_count: Optional[int] = UNSET
    staff: Optional[bool] = UNSET


class Tag4Dict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    topic_count: NotRequired[int]
    staff: NotRequired[bool]
