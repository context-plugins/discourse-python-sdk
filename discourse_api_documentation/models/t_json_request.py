from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .topic5 import Topic5, Topic5Dict


class TJsonRequest(SdkBaseModel):
    topic: Optional[Topic5] = UNSET


class TJsonRequestDict(TypedDict):
    topic: NotRequired[Topic5 | Topic5Dict]
