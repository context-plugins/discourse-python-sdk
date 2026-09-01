from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TInviteGroupJsonRequest(SdkBaseModel):
    group: Optional[str] = UNSET
    """The name of the group to invite"""

    should_notify: Optional[bool] = UNSET
    """Whether to notify the group, it defaults to true"""


class TInviteGroupJsonRequestDict(TypedDict):
    group: NotRequired[str]
    should_notify: NotRequired[bool]
