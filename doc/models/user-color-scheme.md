
# User Color Scheme

## Structure

`UserColorScheme`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `name` | `str` | Required | - |
| `is_dark` | `bool` | Required | - |
| `theme_id` | `int` | Optional | - |
| `colors` | `List[Any]` | Required | - |

## Example

```python
import jsonpickle

from discourse.models.user_color_scheme import UserColorScheme

user_color_scheme = UserColorScheme(
    id=108,
    name='name2',
    is_dark=False,
    colors=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    theme_id=78
)
```

