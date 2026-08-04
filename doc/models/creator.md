
# Creator

## Structure

`Creator`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `username` | `str` | Required | - |
| `name` | `str` | Optional | - |
| `avatar_template` | `str` | Required | - |

## Example

```python
from discourse.models.creator import Creator

creator = Creator(
    id=76,
    username='username2',
    avatar_template='avatar_template2',
    name='name8'
)
```

