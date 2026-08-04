
# Topics Private Messages Json Response

*This model accepts additional fields of type Any.*

## Structure

`TopicsPrivateMessagesJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `users` | [`List[User1]`](../../doc/models/user-1.md) | Optional | - |
| `primary_groups` | `List[Any]` | Optional | - |
| `topic_list` | [`TopicList1`](../../doc/models/topic-list-1.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.topic_list_1 import TopicList1
from discourse.models.topics_private_messages_json_response import TopicsPrivateMessagesJsonResponse
from discourse.models.user_1 import User1

topics_private_messages_json_response = TopicsPrivateMessagesJsonResponse(
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
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    topic_list=TopicList1(
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

