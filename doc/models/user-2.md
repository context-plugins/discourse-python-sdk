
# User 2

*This model accepts additional fields of type Any.*

## Structure

`User2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `username` | `str` | Optional | - |
| `name` | `str` | Optional | - |
| `avatar_template` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.user_2 import User2

user_2 = User2(
    id=70,
    username='username0',
    name='name0',
    avatar_template='avatar_template0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

