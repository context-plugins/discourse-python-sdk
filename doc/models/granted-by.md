
# Granted By

## Structure

`GrantedBy`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `username` | `str` | Required | - |
| `name` | `str` | Required | - |
| `avatar_template` | `str` | Required | - |
| `flair_name` | `str` | Required | - |
| `admin` | `bool` | Required | - |
| `moderator` | `bool` | Required | - |
| `trust_level` | `int` | Required | - |

## Example

```python
from discourse.models.granted_by import GrantedBy

granted_by = GrantedBy(
    id=106,
    username='username0',
    name='name0',
    avatar_template='avatar_template0',
    flair_name='flair_name6',
    admin=False,
    moderator=False,
    trust_level=90
)
```

