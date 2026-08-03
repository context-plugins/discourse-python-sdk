
# Admin Users Json Request

## Structure

`AdminUsersJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `delete_posts` | `bool` | Optional | - |
| `block_email` | `bool` | Optional | - |
| `block_urls` | `bool` | Optional | - |
| `block_ip` | `bool` | Optional | - |

## Example

```python
from discourseapidocumentation.models.admin_users_json_request import AdminUsersJsonRequest

admin_users_json_request = AdminUsersJsonRequest(
    delete_posts=False,
    block_email=False,
    block_urls=False,
    block_ip=False
)
```

