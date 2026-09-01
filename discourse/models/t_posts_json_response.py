from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .post_stream import PostStream, PostStreamDict


class TPostsJsonResponse(SdkBaseModel):
    post_stream: Optional[PostStream] = UNSET
    id: Optional[int] = UNSET


class TPostsJsonResponseDict(TypedDict):
    post_stream: NotRequired[PostStream | PostStreamDict]
    id: NotRequired[int]
