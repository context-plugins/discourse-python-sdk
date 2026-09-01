from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GroupsMembersJsonRequest(SdkBaseModel):
    usernames: Optional[str] = UNSET
    """comma separated list"""


class GroupsMembersJsonRequestDict(TypedDict):
    usernames: NotRequired[str]
