
# Posts Locked Json Response

*This model accepts additional fields of type Any.*

## Structure

`PostsLockedJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `locked` | `bool` | Required | Whether the post is locked |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.posts_locked_json_response import PostsLockedJsonResponse

posts_locked_json_response = PostsLockedJsonResponse(
    locked=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

