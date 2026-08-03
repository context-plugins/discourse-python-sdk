
# Users Password Reset Json Request

## Structure

`UsersPasswordResetJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `str` | Required | - |
| `password` | `str` | Required | - |

## Example

```python
from discourseapidocumentation.models.users_password_reset_json_request import UsersPasswordResetJsonRequest

users_password_reset_json_request = UsersPasswordResetJsonRequest(
    username='username4',
    password='password8'
)
```

