
# Notification

*This model accepts additional fields of type Any.*

## Structure

`Notification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `user_id` | `int` | Optional | - |
| `notification_type` | `int` | Optional | - |
| `read` | `bool` | Optional | - |
| `created_at` | `str` | Optional | - |
| `post_number` | `int` | Optional | - |
| `topic_id` | `int` | Optional | - |
| `slug` | `str` | Optional | - |
| `data` | [`Data`](../../doc/models/data.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.notification import Notification

notification = Notification(
    id=88,
    user_id=184,
    notification_type=108,
    read=False,
    created_at='created_at0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

