
# Last Poster

## Structure

`LastPoster`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `username` | `str` | Required | - |
| `name` | `str` | Required | - |
| `avatar_template` | `str` | Required | - |

## Example

```python
from discourse.models.last_poster import LastPoster

last_poster = LastPoster(
    id=254,
    username='username2',
    name='name8',
    avatar_template='avatar_template2'
)
```

