
# Notifications Json Response

*This model accepts additional fields of type Any.*

## Structure

`NotificationsJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notifications` | [`List[Notification]`](../../doc/models/notification.md) | Optional | - |
| `total_rows_notifications` | `int` | Optional | - |
| `seen_notification_id` | `int` | Optional | - |
| `load_more_notifications` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.notification import Notification
from discourseapidocumentation.models.notifications_json_response import NotificationsJsonResponse

notifications_json_response = NotificationsJsonResponse(
    notifications=[
        Notification(
            id=86,
            user_id=182,
            notification_type=106,
            read=False,
            created_at='created_at0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    total_rows_notifications=96,
    seen_notification_id=124,
    load_more_notifications='load_more_notifications2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

