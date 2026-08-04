
# Badge Type

## Structure

`BadgeType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `name` | `str` | Required | - |
| `sort_order` | `int` | Required | - |

## Example

```python
from discourse.models.badge_type import BadgeType

badge_type = BadgeType(
    id=164,
    name='name0',
    sort_order=130
)
```

