
# Admin Users Suspend Json Request

## Structure

`AdminUsersSuspendJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `suspend_until` | `str` | Required | - |
| `reason` | `str` | Required | - |
| `message` | `str` | Optional | Will send an email with this message when present |
| `post_action` | `str` | Optional | - |

## Example

```python
from discourseapidocumentation.models.admin_users_suspend_json_request import AdminUsersSuspendJsonRequest

admin_users_suspend_json_request = AdminUsersSuspendJsonRequest(
    suspend_until='2121-02-22',
    reason='reason8',
    message='message6',
    post_action='delete'
)
```

