from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PostsLockedJsonResponse(SdkBaseModel):
    locked: bool
    """Whether the post is locked"""


class PostsLockedJsonResponseDict(TypedDict):
    locked: bool
