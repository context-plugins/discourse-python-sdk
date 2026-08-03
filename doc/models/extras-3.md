
# Extras 3

*This model accepts additional fields of type Any.*

## Structure

`Extras3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `categories` | `List[Any]` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.extras_3 import Extras3

extras_3 = Extras3(
    categories=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

