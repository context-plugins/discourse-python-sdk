
# Latest Json Response

*This model accepts additional fields of type Any.*

## Structure

`LatestJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `users` | [`List[User2]`](../../doc/models/user-2.md) | Optional | - |
| `primary_groups` | `List[Any]` | Optional | - |
| `topic_list` | [`TopicList4`](../../doc/models/topic-list-4.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.latest_json_response import LatestJsonResponse
from discourseapidocumentation.models.topic_list_4 import TopicList4
from discourseapidocumentation.models.user_2 import User2

latest_json_response = LatestJsonResponse(
    users=[
        User2(
            id=58,
            username='username4',
            name='name6',
            avatar_template='avatar_template4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        User2(
            id=58,
            username='username4',
            name='name6',
            avatar_template='avatar_template4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    primary_groups=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    topic_list=TopicList4(
        can_create_topic=False,
        draft='draft6',
        draft_key='draft_key4',
        draft_sequence=80,
        per_page=116,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

