
# Extra

*This model accepts additional fields of type Any.*

## Structure

`Extra`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `categories` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.extra import Extra

extra = Extra(
    categories='categories8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

