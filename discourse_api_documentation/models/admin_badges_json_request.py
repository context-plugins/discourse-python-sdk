from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AdminBadgesJsonRequest(SdkBaseModel):
    name: str
    """The name for the new badge."""

    badge_type_id: int
    """The ID for the badge type. 1 for Gold, 2 for Silver, 3 for Bronze."""


class AdminBadgesJsonRequestDict(TypedDict):
    name: str
    badge_type_id: int
