
# Post Types

## Structure

`PostTypes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `regular` | `int` | Required | - |
| `moderator_action` | `int` | Required | - |
| `small_action` | `int` | Required | - |
| `whisper` | `int` | Required | - |

## Example

```python
from discourseapidocumentation.models.post_types import PostTypes

post_types = PostTypes(
    regular=174,
    moderator_action=126,
    small_action=86,
    whisper=152
)
```

