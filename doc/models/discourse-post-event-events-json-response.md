
# Discourse Post Event Events Json Response

## Structure

`DiscoursePostEventEventsJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | [`List[Event]`](../../doc/models/event.md) | Required | - |

## Example

```python
import dateutil.parser
import jsonpickle

from discourseapidocumentation.models.discourse_post_event_events_json_response import DiscoursePostEventEventsJsonResponse
from discourseapidocumentation.models.event import Event
from discourseapidocumentation.models.occurrence import Occurrence
from discourseapidocumentation.models.post import Post
from discourseapidocumentation.models.status import Status
from discourseapidocumentation.models.topic import Topic

discourse_post_event_events_json_response = DiscoursePostEventEventsJsonResponse(
    events=[
        Event(
            id=68,
            category_id=194,
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
            status=Status.PRIVATE,
            at_capacity=False,
            name='name0',
            recurrence='recurrence6',
            recurrence_until=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            rrule='rrule0',
            duration='duration6'
        )
    ]
)
```

