
# Optimized Video

## Structure

`OptimizedVideo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `upload_id` | `int` | Optional | - |
| `url` | `str` | Optional | - |
| `extension` | `str` | Optional | - |
| `filesize` | `int` | Optional | - |
| `sha_1` | `str` | Optional | - |
| `original_filename` | `str` | Optional | - |

## Example

```python
from discourse.models.optimized_video import OptimizedVideo

optimized_video = OptimizedVideo(
    id=182,
    upload_id=116,
    url='url4',
    extension='extension6',
    filesize=152
)
```

