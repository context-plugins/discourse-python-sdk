
# Admin Backups Json Request

## Structure

`AdminBackupsJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `with_uploads` | `bool` | Required | - |

## Example

```python
from discourse.models.admin_backups_json_request import AdminBackupsJsonRequest

admin_backups_json_request = AdminBackupsJsonRequest(
    with_uploads=False
)
```

