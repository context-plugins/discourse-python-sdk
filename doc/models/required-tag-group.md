
# Required Tag Group

## Structure

`RequiredTagGroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `min_count` | `int` | Required | - |

## Example

```python
from discourse.models.required_tag_group import RequiredTagGroup

required_tag_group = RequiredTagGroup(
    name='name6',
    min_count=12
)
```

