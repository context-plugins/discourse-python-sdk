from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UserNotificationSchedule(SdkBaseModel):
    enabled: bool
    day_0_start_time: int
    day_0_end_time: int
    day_1_start_time: int
    day_1_end_time: int
    day_2_start_time: int
    day_2_end_time: int
    day_3_start_time: int
    day_3_end_time: int
    day_4_start_time: int
    day_4_end_time: int
    day_5_start_time: int
    day_5_end_time: int
    day_6_start_time: int
    day_6_end_time: int


class UserNotificationScheduleDict(TypedDict):
    enabled: bool
    day_0_start_time: int
    day_0_end_time: int
    day_1_start_time: int
    day_1_end_time: int
    day_2_start_time: int
    day_2_end_time: int
    day_3_start_time: int
    day_3_end_time: int
    day_4_start_time: int
    day_4_end_time: int
    day_5_start_time: int
    day_5_end_time: int
    day_6_start_time: int
    day_6_end_time: int
