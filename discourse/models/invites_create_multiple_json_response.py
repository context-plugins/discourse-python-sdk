from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InvitesCreateMultipleJsonResponse(SdkBaseModel):
    num_successfully_created_invitations: Optional[int] = UNSET
    num_failed_invitations: Optional[int] = UNSET
    failed_invitations: Optional[list[Any]] = UNSET
    successful_invitations: Optional[list[Any]] = UNSET


class InvitesCreateMultipleJsonResponseDict(TypedDict):
    num_successfully_created_invitations: NotRequired[int]
    num_failed_invitations: NotRequired[int]
    failed_invitations: NotRequired[list[Any]]
    successful_invitations: NotRequired[list[Any]]
