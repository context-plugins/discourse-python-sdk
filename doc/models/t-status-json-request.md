
# T Status Json Request

*This model accepts additional fields of type Any.*

## Structure

`TStatusJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`Status1`](../../doc/models/status-1.md) | Required | - |
| `enabled` | [`Enabled`](../../doc/models/enabled.md) | Required | - |
| `until` | `str` | Optional | Only required for `pinned` and `pinned_globally` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.enabled import Enabled
from discourse.models.status_1 import Status1
from discourse.models.t_status_json_request import TStatusJsonRequest

t_status_json_request = TStatusJsonRequest(
    status=Status1.VISIBLE,
    enabled=Enabled.TRUE,
    until='2030-12-31',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

