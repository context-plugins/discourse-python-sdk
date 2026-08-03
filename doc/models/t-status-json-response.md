
# T Status Json Response

*This model accepts additional fields of type Any.*

## Structure

`TStatusJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `str` | Optional | - |
| `topic_status_update` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.t_status_json_response import TStatusJsonResponse

t_status_json_response = TStatusJsonResponse(
    success='OK',
    topic_status_update='topic_status_update2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

