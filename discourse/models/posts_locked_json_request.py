from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PostsLockedJsonRequest(SdkBaseModel):
    locked: str
    """Whether to lock the post (true/false)"""


class PostsLockedJsonRequestDict(TypedDict):
    locked: str
