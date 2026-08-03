
# Extras 2

## Structure

`Extras2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `type_filters` | `List[Any]` | Required | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.extras_2 import Extras2

extras_2 = Extras2(
    type_filters=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ]
)
```

