
# User Notification Schedule

## Structure

`UserNotificationSchedule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Required | - |
| `day_0_start_time` | `int` | Required | - |
| `day_0_end_time` | `int` | Required | - |
| `day_1_start_time` | `int` | Required | - |
| `day_1_end_time` | `int` | Required | - |
| `day_2_start_time` | `int` | Required | - |
| `day_2_end_time` | `int` | Required | - |
| `day_3_start_time` | `int` | Required | - |
| `day_3_end_time` | `int` | Required | - |
| `day_4_start_time` | `int` | Required | - |
| `day_4_end_time` | `int` | Required | - |
| `day_5_start_time` | `int` | Required | - |
| `day_5_end_time` | `int` | Required | - |
| `day_6_start_time` | `int` | Required | - |
| `day_6_end_time` | `int` | Required | - |

## Example

```python
from discourse.models.user_notification_schedule import UserNotificationSchedule

user_notification_schedule = UserNotificationSchedule(
    enabled=False,
    day_0_start_time=242,
    day_0_end_time=54,
    day_1_start_time=130,
    day_1_end_time=246,
    day_2_start_time=112,
    day_2_end_time=212,
    day_3_start_time=160,
    day_3_end_time=110,
    day_4_start_time=186,
    day_4_end_time=212,
    day_5_start_time=48,
    day_5_end_time=64,
    day_6_start_time=102,
    day_6_end_time=208
)
```

