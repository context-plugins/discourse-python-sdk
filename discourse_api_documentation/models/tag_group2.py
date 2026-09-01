from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .permissions2 import Permissions2, Permissions2Dict


class TagGroup2(SdkBaseModel):
    id: Optional[int] = UNSET
    name: Optional[str] = UNSET
    tag_names: Optional[list[Any]] = UNSET
    parent_tag_name: Optional[list[Any]] = UNSET
    one_per_topic: Optional[bool] = UNSET
    permissions: Optional[Permissions2] = UNSET


class TagGroup2Dict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    tag_names: NotRequired[list[Any]]
    parent_tag_name: NotRequired[list[Any]]
    one_per_topic: NotRequired[bool]
    permissions: NotRequired[Permissions2 | Permissions2Dict]
