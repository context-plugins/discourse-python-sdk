
# Notifications Mark Read Json Request

*This model accepts additional fields of type Any.*

## Structure

`NotificationsMarkReadJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | (optional) Leave off to mark all notifications as<br>read |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.notifications_mark_read_json_request import NotificationsMarkReadJsonRequest

notifications_mark_read_json_request = NotificationsMarkReadJsonRequest(
    id=82,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

