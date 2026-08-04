
# Suspension

## Structure

`Suspension`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `suspend_reason` | `str` | Required | - |
| `full_suspend_reason` | `str` | Required | - |
| `suspended_till` | `str` | Required | - |
| `suspended_at` | `str` | Required | - |
| `suspended_by` | [`SuspendedBy`](../../doc/models/suspended-by.md) | Required | - |

## Example

```python
from discourse.models.suspended_by import SuspendedBy
from discourse.models.suspension import Suspension

suspension = Suspension(
    suspend_reason='suspend_reason4',
    full_suspend_reason='full_suspend_reason6',
    suspended_till='suspended_till4',
    suspended_at='suspended_at8',
    suspended_by=SuspendedBy(
        id=146,
        username='username4',
        name='name4',
        avatar_template='avatar_template6'
    )
)
```

