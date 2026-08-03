
# User Theme

## Structure

`UserTheme`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `theme_id` | `int` | Required | - |
| `name` | `str` | Required | - |
| `default` | `bool` | Required | - |
| `color_scheme_id` | `int` | Required | - |
| `dark_color_scheme_id` | `int` | Optional | - |
| `only_theme_color_schemes` | `bool` | Optional | - |

## Example

```python
from discourseapidocumentation.models.user_theme import UserTheme

user_theme = UserTheme(
    theme_id=42,
    name='name2',
    default=False,
    color_scheme_id=190,
    dark_color_scheme_id=206,
    only_theme_color_schemes=False
)
```

