from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InvitesCreateMultipleJsonRequest(SdkBaseModel):
    email: Optional[str] = UNSET
    """pass 1 email per invite to be generated. other properties will be shared by each invite."""

    skip_email: Optional[bool] = UNSET
    custom_message: Optional[str] = UNSET
    """optional, for email invites"""

    max_redemptions_allowed: Optional[int] = UNSET
    """optional, for link invites"""

    topic_id: Optional[int] = UNSET
    group_ids: Optional[str] = UNSET
    """Optional, either this or ``group_names``. Comma separated list for multiple ids."""

    group_names: Optional[str] = UNSET
    """Optional, either this or ``group_ids``. Comma separated list for multiple names."""

    expires_at: Optional[str] = UNSET
    """optional, if not supplied, the invite_expiry_days site setting is used"""


class InvitesCreateMultipleJsonRequestDict(TypedDict):
    email: NotRequired[str]
    skip_email: NotRequired[bool]
    custom_message: NotRequired[str]
    max_redemptions_allowed: NotRequired[int]
    topic_id: NotRequired[int]
    group_ids: NotRequired[str]
    group_names: NotRequired[str]
    expires_at: NotRequired[str]
