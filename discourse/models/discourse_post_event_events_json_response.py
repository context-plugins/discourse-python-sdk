from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .event import Event, EventDict


class DiscoursePostEventEventsJsonResponse(SdkBaseModel):
    events: list[Event]


class DiscoursePostEventEventsJsonResponseDict(TypedDict):
    events: list[EventDict]
