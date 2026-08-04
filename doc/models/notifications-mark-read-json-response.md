
# Notifications Mark Read Json Response

*This model accepts additional fields of type Any.*

## Structure

`NotificationsMarkReadJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.notifications_mark_read_json_response import NotificationsMarkReadJsonResponse

notifications_mark_read_json_response = NotificationsMarkReadJsonResponse(
    success='success8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

