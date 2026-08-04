
# Event

## Structure

`Event`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `category_id` | `int` | Required | - |
| `name` | `str` | Optional | - |
| `recurrence` | `str` | Optional | - |
| `recurrence_until` | `datetime` | Optional | - |
| `starts_at` | `datetime` | Required | - |
| `ends_at` | `datetime` | Required | - |
| `rrule` | `str` | Optional | - |
| `show_local_time` | `bool` | Required | - |
| `timezone` | `str` | Required | - |
| `duration` | `str` | Optional | **Constraints**: *Pattern*: `^\d{2}:\d{2}:\d{2}$` |
| `all_day` | `bool` | Optional | - |
| `custom_fields` | `Any` | Optional | - |
| `post` | [`Post`](../../doc/models/post.md) | Required | - |
| `occurrences` | [`List[Occurrence]`](../../doc/models/occurrence.md) | Required | - |
| `can_act_on_discourse_post_event` | `bool` | Required | - |
| `can_update_attendance` | `bool` | Required | - |
| `creator` | [`Creator`](../../doc/models/creator.md) | Optional | - |
| `is_closed` | `bool` | Required | - |
| `is_expired` | `bool` | Required | - |
| `is_ongoing` | `bool` | Required | - |
| `is_private` | `bool` | Required | - |
| `is_public` | `bool` | Required | - |
| `is_standalone` | `bool` | Required | - |
| `minimal` | `bool` | Optional | - |
| `raw_invitees` | `List[str]` | Optional | - |
| `reminders` | [`List[Reminder]`](../../doc/models/reminder.md) | Optional | - |
| `sample_invitees` | `List[Any]` | Optional | - |
| `should_display_invitees` | `bool` | Required | - |
| `stats` | `Any` | Optional | - |
| `status` | [`Status`](../../doc/models/status.md) | Required | - |
| `url` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `description_html` | `str` | Optional | - |
| `location` | `str` | Optional | - |
| `watching_invitee` | `Any` | Optional | - |
| `chat_enabled` | `bool` | Optional | - |
| `channel` | `Any` | Optional | - |
| `livestream` | `bool` | Optional | - |
| `livestream_onebox` | `str` | Optional | - |
| `is_zoom_livestream` | `bool` | Optional | - |
| `max_attendees` | `int` | Optional | - |
| `at_capacity` | `bool` | Required | - |
| `image_upload` | `Any` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from discourse.models.event import Event
from discourse.models.occurrence import Occurrence
from discourse.models.post import Post
from discourse.models.status import Status
from discourse.models.topic import Topic

event = Event(
    id=242,
    category_id=20,
    starts_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    ends_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    show_local_time=False,
    timezone='timezone0',
    post=Post(
        id=236,
        post_number=132,
        url='url4',
        category_slug='category_slug4',
        topic=Topic(
            id=54,
            title='title4',
            tags=[
                'tags3'
            ],
            tags_descriptions=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            slug='slug2'
        )
    ),
    occurrences=[
        Occurrence(
            starts_at='starts_at4',
            ends_at='ends_at0'
        )
    ],
    can_act_on_discourse_post_event=False,
    can_update_attendance=False,
    is_closed=False,
    is_expired=False,
    is_ongoing=False,
    is_private=False,
    is_public=False,
    is_standalone=False,
    should_display_invitees=False,
    status=Status.STANDALONE,
    at_capacity=False,
    name='name0',
    recurrence='recurrence6',
    recurrence_until=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    rrule='rrule0',
    duration='duration6'
)
```

