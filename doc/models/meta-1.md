
# Meta 1

## Structure

`Meta1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `last_updated_at` | `str` | Required | - |
| `total_rows_directory_items` | `int` | Required | - |
| `load_more_directory_items` | `str` | Required | - |

## Example

```python
from discourseapidocumentation.models.meta_1 import Meta1

meta_1 = Meta1(
    last_updated_at='last_updated_at4',
    total_rows_directory_items=6,
    load_more_directory_items='load_more_directory_items0'
)
```

