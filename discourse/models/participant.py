from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Participant(SdkBaseModel):
    extras: Optional[str] = UNSET
    description: OptionalNullable[str] = UNSET
    user_id: Optional[int] = UNSET
    primary_group_id: OptionalNullable[int] = UNSET


class ParticipantDict(TypedDict):
    extras: NotRequired[str]
    description: NotRequired[str | None]
    user_id: NotRequired[int]
    primary_group_id: NotRequired[int | None]
