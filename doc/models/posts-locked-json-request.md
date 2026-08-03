
# Posts Locked Json Request

*This model accepts additional fields of type Any.*

## Structure

`PostsLockedJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `locked` | `str` | Required | Whether to lock the post (true/false) |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.posts_locked_json_request import PostsLockedJsonRequest

posts_locked_json_request = PostsLockedJsonRequest(
    locked='locked0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

