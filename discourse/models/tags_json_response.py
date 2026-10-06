from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .extras3 import Extras3, Extras3Dict
from .tag3 import Tag3, Tag3Dict


class TagsJsonResponse(SdkBaseModel):
    tags: Optional[list[Tag3]] = UNSET
    extras: Optional[Extras3] = UNSET


class TagsJsonResponseDict(TypedDict):
    tags: NotRequired[list[Tag3Dict]]
    extras: NotRequired[Extras3Dict]
