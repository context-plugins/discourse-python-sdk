
# Thumbnail

## Structure

`Thumbnail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `upload_id` | `int` | Optional | - |
| `url` | `str` | Optional | - |
| `extension` | `str` | Optional | - |
| `width` | `int` | Optional | - |
| `height` | `int` | Optional | - |
| `filesize` | `int` | Optional | - |

## Example

```python
from discourseapidocumentation.models.thumbnail import Thumbnail

thumbnail = Thumbnail(
    id=154,
    upload_id=144,
    url='url0',
    extension='extension2',
    width=2
)
```

