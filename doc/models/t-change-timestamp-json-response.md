
# T Change Timestamp Json Response

*This model accepts additional fields of type Any.*

## Structure

`TChangeTimestampJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.t_change_timestamp_json_response import TChangeTimestampJsonResponse

t_change_timestamp_json_response = TChangeTimestampJsonResponse(
    success='OK',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

