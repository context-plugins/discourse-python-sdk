
# Tag 3

*This model accepts additional fields of type Any.*

## Structure

`Tag3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `text` | `str` | Optional | - |
| `name` | `str` | Optional | - |
| `count` | `int` | Optional | - |
| `pm_count` | `int` | Optional | - |
| `target_tag` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.tag_3 import Tag3

tag_3 = Tag3(
    id=46,
    text='text0',
    name='name0',
    count=126,
    pm_count=96,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

