
# Tag Group 2

*This model accepts additional fields of type Any.*

## Structure

`TagGroup2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `name` | `str` | Optional | - |
| `tag_names` | `List[Any]` | Optional | - |
| `parent_tag_name` | `List[Any]` | Optional | - |
| `one_per_topic` | `bool` | Optional | - |
| `permissions` | [`Permissions2`](../../doc/models/permissions-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.tag_group_2 import TagGroup2

tag_group_2 = TagGroup2(
    id=108,
    name='name4',
    tag_names=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    parent_tag_name=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    one_per_topic=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

