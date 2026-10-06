from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .basic_topic import BasicTopic, BasicTopicDict


class TJsonResponse1(SdkBaseModel):
    basic_topic: Optional[BasicTopic] = UNSET


class TJsonResponse1Dict(TypedDict):
    basic_topic: NotRequired[BasicTopicDict]
