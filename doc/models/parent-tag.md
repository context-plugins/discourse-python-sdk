
# Parent Tag

## Structure

`ParentTag`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `name` | `str` | Required | - |
| `slug` | `str` | Required | - |

## Example

```python
from discourse.models.parent_tag import ParentTag

parent_tag = ParentTag(
    id=110,
    name='name2',
    slug='slug6'
)
```

