
# User 11

## Structure

`User11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `username` | `str` | Required | - |
| `name` | `str` | Required | - |
| `avatar_template` | `str` | Required | - |
| `title` | `str` | Required | - |

## Example

```python
from discourse.models.user_11 import User11

user_11 = User11(
    id=2,
    username='username2',
    name='name2',
    avatar_template='avatar_template2',
    title='title8'
)
```

