
# Archetype

## Structure

`Archetype`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | - |
| `name` | `str` | Required | - |
| `options` | `List[Any]` | Required | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.archetype import Archetype

archetype = Archetype(
    id='id4',
    name='name4',
    options=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ]
)
```

