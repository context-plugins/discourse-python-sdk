
# Poster 1

*This model accepts additional fields of type Any.*

## Structure

`Poster1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `extras` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `user_id` | `int` | Optional | - |
| `primary_group_id` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.poster_1 import Poster1

poster_1 = Poster1(
    extras='extras6',
    description='description8',
    user_id=46,
    primary_group_id=218,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

