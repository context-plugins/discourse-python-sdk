from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdminUsersJsonRequest(SdkBaseModel):
    delete_posts: Optional[bool] = UNSET
    block_email: Optional[bool] = UNSET
    block_urls: Optional[bool] = UNSET
    block_ip: Optional[bool] = UNSET


class AdminUsersJsonRequestDict(TypedDict):
    delete_posts: NotRequired[bool]
    block_email: NotRequired[bool]
    block_urls: NotRequired[bool]
    block_ip: NotRequired[bool]
