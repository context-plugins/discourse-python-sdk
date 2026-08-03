
# Link Count

## Structure

`LinkCount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Required | - |
| `internal` | `bool` | Required | - |
| `reflection` | `bool` | Required | - |
| `title` | `str` | Required | - |
| `clicks` | `int` | Required | - |

## Example

```python
from discourseapidocumentation.models.link_count import LinkCount

link_count = LinkCount(
    url='url8',
    internal=False,
    reflection=False,
    title='title0',
    clicks=146
)
```

