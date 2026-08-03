
# Reminder

*This model accepts additional fields of type Any.*

## Structure

`Reminder`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `int` | Required | - |
| `unit` | `str` | Required | - |
| `period` | [`Period`](../../doc/models/period.md) | Required | - |
| `mtype` | `str` | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.period import Period
from discourseapidocumentation.models.reminder import Reminder

reminder = Reminder(
    value=88,
    unit='unit8',
    period=Period.BEFORE,
    mtype='type0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

