
# Tag 4

*This model accepts additional fields of type Any.*

## Structure

`Tag4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `name` | `str` | Optional | - |
| `topic_count` | `int` | Optional | - |
| `staff` | `bool` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.tag_4 import Tag4

tag_4 = Tag4(
    id=46,
    name='name4',
    topic_count=202,
    staff=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

