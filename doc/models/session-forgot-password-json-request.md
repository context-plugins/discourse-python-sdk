
# Session Forgot Password Json Request

## Structure

`SessionForgotPasswordJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `login` | `str` | Required | - |

## Example

```python
from discourse.models.session_forgot_password_json_request import SessionForgotPasswordJsonRequest

session_forgot_password_json_request = SessionForgotPasswordJsonRequest(
    login='login2'
)
```

