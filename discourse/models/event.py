from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .creator import Creator, CreatorDict
from .enums.status import StatusOrStr
from .occurrence import Occurrence, OccurrenceDict
from .post import Post, PostDict
from .reminder import Reminder, ReminderDict


class Event(SdkBaseModel):
    id: int
    category_id: int | None
    name: OptionalNullable[str] = UNSET
    recurrence: OptionalNullable[str] = UNSET
    recurrence_until: OptionalNullable[RFC3339DateTime] = UNSET
    starts_at: RFC3339DateTime | None
    ends_at: RFC3339DateTime | None
    rrule: Optional[str] = UNSET
    show_local_time: bool
    timezone: str | None
    duration: Optional[str] = UNSET
    all_day: Optional[bool] = UNSET
    custom_fields: OptionalNullable[Any] = UNSET
    post: Post
    occurrences: list[Occurrence]
    can_act_on_discourse_post_event: bool | None
    can_update_attendance: bool | None
    creator: Optional[Creator] = UNSET
    is_closed: bool
    is_expired: bool
    is_ongoing: bool
    is_private: bool
    is_public: bool
    is_standalone: bool
    minimal: OptionalNullable[bool] = UNSET
    raw_invitees: OptionalNullable[list[str]] = UNSET
    reminders: Optional[list[Reminder]] = UNSET
    sample_invitees: Optional[list[Any]] = UNSET
    should_display_invitees: bool
    stats: Optional[Any] = UNSET
    status: StatusOrStr
    url: Optional[str] = UNSET
    description: OptionalNullable[str] = UNSET
    description_html: OptionalNullable[str] = UNSET
    location: OptionalNullable[str] = UNSET
    watching_invitee: OptionalNullable[Any] = UNSET
    chat_enabled: OptionalNullable[bool] = UNSET
    channel: Optional[Any] = UNSET
    livestream: Optional[bool] = UNSET
    livestream_onebox: OptionalNullable[str] = UNSET
    is_zoom_livestream: Optional[bool] = UNSET
    max_attendees: OptionalNullable[int] = UNSET
    at_capacity: bool
    image_upload: OptionalNullable[Any] = UNSET


class EventDict(TypedDict):
    id: int
    category_id: int | None
    name: NotRequired[str | None]
    recurrence: NotRequired[str | None]
    recurrence_until: NotRequired[RFC3339DateTime | None]
    starts_at: RFC3339DateTime | None
    ends_at: RFC3339DateTime | None
    rrule: NotRequired[str]
    show_local_time: bool
    timezone: str | None
    duration: NotRequired[str]
    all_day: NotRequired[bool]
    custom_fields: NotRequired[Any | None]
    post: PostDict
    occurrences: list[OccurrenceDict]
    can_act_on_discourse_post_event: bool | None
    can_update_attendance: bool | None
    creator: NotRequired[CreatorDict]
    is_closed: bool
    is_expired: bool
    is_ongoing: bool
    is_private: bool
    is_public: bool
    is_standalone: bool
    minimal: NotRequired[bool | None]
    raw_invitees: NotRequired[list[str] | None]
    reminders: NotRequired[list[ReminderDict]]
    sample_invitees: NotRequired[list[Any]]
    should_display_invitees: bool
    stats: NotRequired[Any]
    status: StatusOrStr
    url: NotRequired[str]
    description: NotRequired[str | None]
    description_html: NotRequired[str | None]
    location: NotRequired[str | None]
    watching_invitee: NotRequired[Any | None]
    chat_enabled: NotRequired[bool | None]
    channel: NotRequired[Any]
    livestream: NotRequired[bool]
    livestream_onebox: NotRequired[str | None]
    is_zoom_livestream: NotRequired[bool]
    max_attendees: NotRequired[int | None]
    at_capacity: bool
    image_upload: NotRequired[Any | None]
