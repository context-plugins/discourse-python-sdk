
# Created By

## Structure

`CreatedBy`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `username` | `str` | Required | - |
| `name` | `str` | Required | - |
| `avatar_template` | `str` | Required | - |

## Example

```python
from discourseapidocumentation.models.created_by import CreatedBy

created_by = CreatedBy(
    id=188,
    username='username8',
    name='name2',
    avatar_template='avatar_template8'
)
```

