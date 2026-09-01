from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.period import PeriodOrStr


class Reminder(SdkBaseModel):
    value: int
    unit: str
    period: PeriodOrStr
    type_: str = Field(alias="type")


class ReminderDict(TypedDict):
    value: int
    unit: str
    period: PeriodOrStr
    type_: str
