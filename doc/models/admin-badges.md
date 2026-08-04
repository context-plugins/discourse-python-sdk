
# Admin Badges

## Structure

`AdminBadges`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `protected_system_fields` | `List[Any]` | Required | - |
| `triggers` | [`Triggers`](../../doc/models/triggers.md) | Required | - |
| `badge_ids` | `List[Any]` | Required | - |
| `badge_grouping_ids` | `List[Any]` | Required | - |
| `badge_type_ids` | `List[Any]` | Required | - |

## Example

```python
import jsonpickle

from discourse.models.admin_badges import AdminBadges
from discourse.models.triggers import Triggers

admin_badges = AdminBadges(
    protected_system_fields=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    triggers=Triggers(
        user_change=26,
        none=198,
        post_revision=74,
        trust_level_change=164,
        post_action=132
    ),
    badge_ids=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    badge_grouping_ids=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    badge_type_ids=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ]
)
```

