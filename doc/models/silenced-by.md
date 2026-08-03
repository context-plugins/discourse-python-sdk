
# Silenced By

## Structure

`SilencedBy`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `username` | `str` | Required | - |
| `name` | `str` | Required | - |
| `avatar_template` | `str` | Required | - |

## Example

```python
from discourseapidocumentation.models.silenced_by import SilencedBy

silenced_by = SilencedBy(
    id=46,
    username='username6',
    name='name4',
    avatar_template='avatar_template6'
)
```

