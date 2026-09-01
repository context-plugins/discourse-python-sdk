from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .post3 import Post3, Post3Dict


class PostStream(SdkBaseModel):
    posts: Optional[list[Post3]] = UNSET


class PostStreamDict(TypedDict):
    posts: NotRequired[list[Post3 | Post3Dict]]
