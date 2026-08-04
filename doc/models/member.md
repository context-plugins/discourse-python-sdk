
# Member

## Structure

`Member`

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
from discourse.models.member import Member

member = Member(
    id=196,
    username='username4',
    name='name6',
    avatar_template='avatar_template4',
    title='title8',
    last_posted_at='last_posted_at2',
    last_seen_at='last_seen_at2',
    added_at='added_at8',
    timezone='timezone4'
)
```

