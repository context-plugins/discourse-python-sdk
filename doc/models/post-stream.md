
# Post Stream

*This model accepts additional fields of type Any.*

## Structure

`PostStream`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `posts` | [`List[Post3]`](../../doc/models/post-3.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.post_3 import Post3
from discourse.models.post_stream import PostStream

post_stream = PostStream(
    posts=[
        Post3(
            id=64,
            name='name6',
            username='username6',
            avatar_template='avatar_template6',
            created_at='created_at4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Post3(
            id=64,
            name='name6',
            username='username6',
            avatar_template='avatar_template6',
            created_at='created_at4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Post3(
            id=64,
            name='name6',
            username='username6',
            avatar_template='avatar_template6',
            created_at='created_at4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

