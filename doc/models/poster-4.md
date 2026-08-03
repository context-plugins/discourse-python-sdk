
# Poster 4

## Structure

`Poster4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `extras` | `str` | Required | - |
| `description` | `str` | Required | - |
| `user` | [`User`](../../doc/models/user.md) | Required | - |

## Example

```python
from discourseapidocumentation.models.poster_4 import Poster4
from discourseapidocumentation.models.user import User

poster_4 = Poster4(
    extras='extras0',
    description='description6',
    user=User(
        id=76,
        username='username0',
        name='name0',
        avatar_template='avatar_template0'
    )
)
```

