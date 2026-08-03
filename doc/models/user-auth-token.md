
# User Auth Token

## Structure

`UserAuthToken`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `client_ip` | `str` | Required | - |
| `location` | `str` | Required | - |
| `browser` | `str` | Required | - |
| `device` | `str` | Required | - |
| `os` | `str` | Required | - |
| `icon` | `str` | Required | - |
| `created_at` | `str` | Required | - |
| `seen_at` | `str` | Required | - |
| `is_active` | `bool` | Required | - |

## Example

```python
from discourseapidocumentation.models.user_auth_token import UserAuthToken

user_auth_token = UserAuthToken(
    id=4,
    client_ip='client_ip0',
    location='location4',
    browser='browser0',
    device='device6',
    os='os8',
    icon='icon2',
    created_at='created_at8',
    seen_at='seen_at0',
    is_active=False
)
```

