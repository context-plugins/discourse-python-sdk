
# U Json Request

## Structure

`UJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `external_ids` | `Any` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.u_json_request import UJsonRequest

u_json_request = UJsonRequest(
    name='name4',
    external_ids=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)
```

