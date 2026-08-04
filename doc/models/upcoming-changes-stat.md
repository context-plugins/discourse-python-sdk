
# Upcoming Changes Stat

## Structure

`UpcomingChangesStat`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `humanized_name` | `str` | Required | - |
| `description` | `str` | Required | - |
| `enabled` | `bool` | Required | - |
| `specific_groups` | `List[str]` | Required | - |
| `reason` | [`Reason`](../../doc/models/reason.md) | Required | - |

## Example

```python
from discourse.models.reason import Reason
from discourse.models.upcoming_changes_stat import UpcomingChangesStat

upcoming_changes_stat = UpcomingChangesStat(
    name='name2',
    humanized_name='humanized_name0',
    description='description2',
    enabled=False,
    specific_groups=[
        'specific_groups7',
        'specific_groups6'
    ],
    reason=Reason.ENABLED_FOR_EVERYONE
)
```

