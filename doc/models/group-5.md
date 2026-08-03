
# Group 5

## Structure

`Group5`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `name` | `str` | Required | - |
| `full_name` | `str` | Optional | - |
| `display_name` | `str` | Optional | - |
| `flair_url` | `str` | Required | - |
| `flair_bg_color` | `str` | Required | - |
| `flair_color` | `str` | Required | - |
| `automatic` | `bool` | Required | - |

## Example

```python
from discourseapidocumentation.models.group_5 import Group5

group_5 = Group5(
    id=94,
    name='name4',
    flair_url='flair_url4',
    flair_bg_color='flair_bg_color8',
    flair_color='flair_color8',
    automatic=False,
    full_name='full_name0',
    display_name='display_name4'
)
```

