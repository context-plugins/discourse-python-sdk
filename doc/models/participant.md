
# Participant

*This model accepts additional fields of type Any.*

## Structure

`Participant`

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

from discourseapidocumentation.models.participant import Participant

participant = Participant(
    extras='extras0',
    description='description6',
    user_id=152,
    primary_group_id=68,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

