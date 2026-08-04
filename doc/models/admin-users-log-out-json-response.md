
# Admin Users Log Out Json Response

## Structure

`AdminUsersLogOutJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `str` | Required | - |

## Example

```python
from discourse.models.admin_users_log_out_json_response import AdminUsersLogOutJsonResponse

admin_users_log_out_json_response = AdminUsersLogOutJsonResponse(
    success='OK'
)
```

