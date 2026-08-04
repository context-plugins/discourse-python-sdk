
# Permissions 2

*This model accepts additional fields of type Any.*

## Structure

`Permissions2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `everyone` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.permissions_2 import Permissions2

permissions_2 = Permissions2(
    everyone=40,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

