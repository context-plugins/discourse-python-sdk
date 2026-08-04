
# Users Json Request

## Structure

`UsersJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `email` | `str` | Required | - |
| `password` | `str` | Required | - |
| `username` | `str` | Required | - |
| `active` | `bool` | Optional | This param requires an admin api key in the request<br>header or it will be ignored |
| `approved` | `bool` | Optional | - |
| `user_fields` | `Dict[str, bool]` | Optional | - |
| `external_ids` | `Any` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.users_json_request import UsersJsonRequest

users_json_request = UsersJsonRequest(
    name='name2',
    email='email4',
    password='password6',
    username='username2',
    active=False,
    approved=False,
    user_fields={
        'key0': True,
        'key1': False,
        'key2': True
    },
    external_ids=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)
```

