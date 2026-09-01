from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TagGroupsJsonRequest1(SdkBaseModel):
    name: Optional[str] = UNSET


class TagGroupsJsonRequest1Dict(TypedDict):
    name: NotRequired[str]
