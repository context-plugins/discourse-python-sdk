from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .post2 import Post2, Post2Dict


class PostsJsonResponse3(SdkBaseModel):
    post: Post2


class PostsJsonResponse3Dict(TypedDict):
    post: Post2 | Post2Dict
