
# T Timer Json Response

*This model accepts additional fields of type Any.*

## Structure

`TTimerJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `str` | Optional | - |
| `execute_at` | `str` | Optional | - |
| `duration` | `str` | Optional | - |
| `based_on_last_post` | `bool` | Optional | - |
| `closed` | `bool` | Optional | - |
| `category_id` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.t_timer_json_response import TTimerJsonResponse

t_timer_json_response = TTimerJsonResponse(
    success='OK',
    execute_at='execute_at8',
    duration='duration0',
    based_on_last_post=False,
    closed=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

