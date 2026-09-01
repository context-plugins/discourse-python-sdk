from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .latest_post import LatestPost, LatestPostDict


class PostsJsonResponse(SdkBaseModel):
    latest_posts: list[LatestPost]


class PostsJsonResponseDict(TypedDict):
    latest_posts: list[LatestPost | LatestPostDict]
