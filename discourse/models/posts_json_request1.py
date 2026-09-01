from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .post1 import Post1, Post1Dict


class PostsJsonRequest1(SdkBaseModel):
    post: Optional[Post1] = UNSET
    bypass_bump: Optional[bool] = UNSET
    """Skip bumping the topic when updating the post. Requires staff or TL4 permissions."""


class PostsJsonRequest1Dict(TypedDict):
    post: NotRequired[Post1 | Post1Dict]
    bypass_bump: NotRequired[bool]
