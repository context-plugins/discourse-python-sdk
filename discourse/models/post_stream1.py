from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .post4 import Post4, Post4Dict


class PostStream1(SdkBaseModel):
    posts: list[Post4]
    stream: list[Any]


class PostStream1Dict(TypedDict):
    posts: list[Post4 | Post4Dict]
    stream: list[Any]
