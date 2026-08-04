
# User Badge

## Structure

`UserBadge`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `granted_at` | `str` | Required | - |
| `grouping_position` | `int` | Required | - |
| `is_favorite` | `str` | Required | - |
| `can_favorite` | `bool` | Required | - |
| `badge_id` | `int` | Required | - |
| `granted_by_id` | `int` | Required | - |

## Example

```python
from discourse.models.user_badge import UserBadge

user_badge = UserBadge(
    id=38,
    granted_at='granted_at4',
    grouping_position=202,
    is_favorite='is_favorite6',
    can_favorite=False,
    badge_id=254,
    granted_by_id=100
)
```

