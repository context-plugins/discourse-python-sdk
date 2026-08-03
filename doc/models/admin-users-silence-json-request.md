
# Admin Users Silence Json Request

## Structure

`AdminUsersSilenceJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `silenced_till` | `str` | Required | - |
| `reason` | `str` | Required | - |
| `message` | `str` | Optional | Will send an email with this message when present |
| `post_action` | `str` | Optional | - |

## Example

```python
from discourseapidocumentation.models.admin_users_silence_json_request import AdminUsersSilenceJsonRequest

admin_users_silence_json_request = AdminUsersSilenceJsonRequest(
    silenced_till='2022-06-01T08:00:00.000Z',
    reason='reason2',
    message='message8',
    post_action='delete'
)
```

