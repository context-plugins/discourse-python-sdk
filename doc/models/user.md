
# User

## Structure

`User`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `username` | `str` | Required | - |
| `name` | `str` | Required | - |
| `avatar_template` | `str` | Required | - |

## Example

```python
from discourseapidocumentation.models.user import User

user = User(
    id=76,
    username='username0',
    name='name0',
    avatar_template='avatar_template0'
)
```

