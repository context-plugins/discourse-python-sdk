
# Extras

## Structure

`Extras`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `visible_group_names` | `List[Any]` | Required | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.extras import Extras

extras = Extras(
    visible_group_names=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ]
)
```

