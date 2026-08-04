
# T Notifications Json Request

*This model accepts additional fields of type Any.*

## Structure

`TNotificationsJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notification_level` | [`NotificationLevel`](../../doc/models/notification-level.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.notification_level import NotificationLevel
from discourse.models.t_notifications_json_request import TNotificationsJsonRequest

t_notifications_json_request = TNotificationsJsonRequest(
    notification_level=NotificationLevel.ENUM_2,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

