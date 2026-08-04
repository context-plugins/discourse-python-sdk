
# U Json Response 1

## Structure

`UJsonResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `str` | Required | - |
| `user` | `Any` | Required | - |

## Example

```python
import jsonpickle

from discourse.models.u_json_response_1 import UJsonResponse1

u_json_response_1 = UJsonResponse1(
    success='success2',
    user=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)
```

