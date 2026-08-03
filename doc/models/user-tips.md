
# User Tips

## Structure

`UserTips`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_notification` | `int` | Required | - |
| `topic_timeline` | `int` | Required | - |
| `post_menu` | `int` | Required | - |
| `topic_notification_levels` | `int` | Required | - |
| `suggested_topics` | `int` | Required | - |

## Example

```python
from discourseapidocumentation.models.user_tips import UserTips

user_tips = UserTips(
    first_notification=66,
    topic_timeline=210,
    post_menu=220,
    topic_notification_levels=254,
    suggested_topics=202
)
```

