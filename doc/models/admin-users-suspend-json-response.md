
# Admin Users Suspend Json Response

## Structure

`AdminUsersSuspendJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `suspension` | [`Suspension`](../../doc/models/suspension.md) | Required | - |

## Example

```python
from discourseapidocumentation.models.admin_users_suspend_json_response import AdminUsersSuspendJsonResponse
from discourseapidocumentation.models.suspended_by import SuspendedBy
from discourseapidocumentation.models.suspension import Suspension

admin_users_suspend_json_response = AdminUsersSuspendJsonResponse(
    suspension=Suspension(
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
)
```

