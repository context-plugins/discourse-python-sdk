
# T Timer Json Request

*This model accepts additional fields of type Any.*

## Structure

`TTimerJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `time` | `str` | Optional | - |
| `status_type` | `str` | Optional | - |
| `based_on_last_post` | `bool` | Optional | - |
| `category_id` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.t_timer_json_request import TTimerJsonRequest

t_timer_json_request = TTimerJsonRequest(
    time='time6',
    status_type='status_type8',
    based_on_last_post=False,
    category_id=106,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

