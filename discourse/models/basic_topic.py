from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BasicTopic(SdkBaseModel):
    id: Optional[int] = UNSET
    title: Optional[str] = UNSET
    fancy_title: Optional[str] = UNSET
    slug: Optional[str] = UNSET
    posts_count: Optional[int] = UNSET


class BasicTopicDict(TypedDict):
    id: NotRequired[int]
    title: NotRequired[str]
    fancy_title: NotRequired[str]
    slug: NotRequired[str]
    posts_count: NotRequired[int]
