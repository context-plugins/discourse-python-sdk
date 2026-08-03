
# Owner

## Structure

`Owner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `username` | `str` | Required | - |
| `name` | `str` | Required | - |
| `avatar_template` | `str` | Required | - |
| `title` | `str` | Required | - |
| `last_posted_at` | `str` | Required | - |
| `last_seen_at` | `str` | Required | - |
| `added_at` | `str` | Required | - |
| `timezone` | `str` | Required | - |

## Example

```python
from discourseapidocumentation.models.owner import Owner

owner = Owner(
    id=84,
    username='username6',
    name='name4',
    avatar_template='avatar_template6',
    title='title0',
    last_posted_at='last_posted_at4',
    last_seen_at='last_seen_at0',
    added_at='added_at0',
    timezone='timezone6'
)
```

