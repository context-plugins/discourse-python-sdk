
# Reply to User

## Structure

`ReplyToUser`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `username` | `str` | Required | - |
| `name` | `str` | Optional | - |
| `avatar_template` | `str` | Required | - |

## Example

```python
from discourseapidocumentation.models.reply_to_user import ReplyToUser

reply_to_user = ReplyToUser(
    username='username6',
    avatar_template='avatar_template6',
    id=20,
    name='name4'
)
```

