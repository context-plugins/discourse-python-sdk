
# Approved By

## Structure

`ApprovedBy`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `username` | `str` | Required | - |
| `name` | `str` | Required | - |
| `avatar_template` | `str` | Required | - |

## Example

```python
from discourseapidocumentation.models.approved_by import ApprovedBy

approved_by = ApprovedBy(
    id=188,
    username='username6',
    name='name4',
    avatar_template='avatar_template6'
)
```

