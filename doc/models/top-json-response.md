
# Top Json Response

*This model accepts additional fields of type Any.*

## Structure

`TopJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `users` | [`List[User1]`](../../doc/models/user-1.md) | Optional | - |
| `primary_groups` | `List[Any]` | Optional | - |
| `topic_list` | [`TopicList5`](../../doc/models/topic-list-5.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.top_json_response import TopJsonResponse
from discourse.models.topic_list_5 import TopicList5
from discourse.models.user_1 import User1

top_json_response = TopJsonResponse(
    users=[
        User1(
            id=58,
            username='username4',
            name='name6',
            avatar_template='avatar_template4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        User1(
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
    topic_list=TopicList5(
        can_create_topic=False,
        draft='draft6',
        draft_key='draft_key4',
        draft_sequence=80,
        for_period='for_period6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

