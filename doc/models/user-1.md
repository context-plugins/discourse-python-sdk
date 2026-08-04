
# User 1

*This model accepts additional fields of type Any.*

## Structure

`User1`

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

from discourse.models.user_1 import User1

user_1 = User1(
    id=238,
    username='username2',
    name='name2',
    avatar_template='avatar_template8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

