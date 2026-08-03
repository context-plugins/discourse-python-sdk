
# Poster 6

*This model accepts additional fields of type Any.*

## Structure

`Poster6`

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

from discourseapidocumentation.models.poster_6 import Poster6

poster_6 = Poster6(
    extras='extras6',
    description='description2',
    user_id=110,
    primary_group_id=26,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

