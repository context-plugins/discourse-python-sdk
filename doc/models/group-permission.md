
# Group Permission

## Structure

`GroupPermission`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `permission_type` | `int` | Required | - |
| `group_name` | `str` | Required | - |
| `group_id` | `int` | Required | - |

## Example

```python
from discourse.models.group_permission import GroupPermission

group_permission = GroupPermission(
    permission_type=196,
    group_name='group_name2',
    group_id=180
)
```

