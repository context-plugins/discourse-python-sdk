
# Suspended By

## Structure

`SuspendedBy`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `username` | `str` | Required | - |
| `name` | `str` | Required | - |
| `avatar_template` | `str` | Required | - |

## Example

```python
from discourse.models.suspended_by import SuspendedBy

suspended_by = SuspendedBy(
    id=146,
    username='username4',
    name='name4',
    avatar_template='avatar_template6'
)
```

