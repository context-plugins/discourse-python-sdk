
# T Posts Json Response

*This model accepts additional fields of type Any.*

## Structure

`TPostsJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `post_stream` | [`PostStream`](../../doc/models/post-stream.md) | Optional | - |
| `id` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.post_3 import Post3
from discourseapidocumentation.models.post_stream import PostStream
from discourseapidocumentation.models.t_posts_json_response import TPostsJsonResponse

t_posts_json_response = TPostsJsonResponse(
    post_stream=PostStream(
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
    ),
    id=186,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

