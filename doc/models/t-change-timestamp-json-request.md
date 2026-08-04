
# T Change Timestamp Json Request

*This model accepts additional fields of type Any.*

## Structure

`TChangeTimestampJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timestamp` | `str` | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.t_change_timestamp_json_request import TChangeTimestampJsonRequest

t_change_timestamp_json_request = TChangeTimestampJsonRequest(
    timestamp='1594291380',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

