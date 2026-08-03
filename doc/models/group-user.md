
# Group User

## Structure

`GroupUser`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `group_id` | `int` | Required | - |
| `user_id` | `int` | Required | - |
| `notification_level` | `int` | Required | - |
| `owner` | `bool` | Optional | - |

## Example

```python
from discourseapidocumentation.models.group_user import GroupUser

group_user = GroupUser(
    group_id=116,
    user_id=40,
    notification_level=40,
    owner=False
)
```

