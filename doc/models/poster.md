
# Poster

## Structure

`Poster`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `extras` | `str` | Required | - |
| `description` | `str` | Required | - |
| `user_id` | `int` | Required | - |
| `primary_group_id` | `int` | Required | - |

## Example

```python
from discourseapidocumentation.models.poster import Poster

poster = Poster(
    extras='extras8',
    description='description6',
    user_id=62,
    primary_group_id=234
)
```

