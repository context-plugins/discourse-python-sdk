
# Badge Grouping

## Structure

`BadgeGrouping`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `name` | `str` | Required | - |
| `description` | `str` | Required | - |
| `position` | `int` | Required | - |
| `system` | `bool` | Required | - |

## Example

```python
from discourseapidocumentation.models.badge_grouping import BadgeGrouping

badge_grouping = BadgeGrouping(
    id=200,
    name='name4',
    description='description6',
    position=230,
    system=False
)
```

