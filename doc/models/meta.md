
# Meta

## Structure

`Meta`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `offset` | `int` | Required | - |

## Example

```python
from discourse.models.meta import Meta

meta = Meta(
    total=36,
    limit=126,
    offset=222
)
```

