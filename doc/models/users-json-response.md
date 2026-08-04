
# Users Json Response

## Structure

`UsersJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `bool` | Required | - |
| `active` | `bool` | Required | - |
| `message` | `str` | Required | - |
| `user_id` | `int` | Optional | - |

## Example

```python
from discourse.models.users_json_response import UsersJsonResponse

users_json_response = UsersJsonResponse(
    success=False,
    active=False,
    message='message2',
    user_id=100
)
```

