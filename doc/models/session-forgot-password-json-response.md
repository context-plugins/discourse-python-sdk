
# Session Forgot Password Json Response

## Structure

`SessionForgotPasswordJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `str` | Required | - |
| `user_found` | `bool` | Required | - |

## Example

```python
from discourseapidocumentation.models.session_forgot_password_json_response import SessionForgotPasswordJsonResponse

session_forgot_password_json_response = SessionForgotPasswordJsonResponse(
    success='success4',
    user_found=False
)
```

