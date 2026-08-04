
# Permissions

*This model accepts additional fields of type Any.*

## Structure

`Permissions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `everyone` | `int` | Optional | - |
| `staff` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.permissions import Permissions

permissions = Permissions(
    everyone=1,
    staff=166,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

