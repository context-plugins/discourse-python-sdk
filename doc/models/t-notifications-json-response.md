
# T Notifications Json Response

*This model accepts additional fields of type Any.*

## Structure

`TNotificationsJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.t_notifications_json_response import TNotificationsJsonResponse

t_notifications_json_response = TNotificationsJsonResponse(
    success='OK',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

