
# Access Control

## Structure

`AccessControl`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mandatory_acl` | `Any` | Required | - |
| `banned_acl` | `Any` | Required | - |

## Example

```python
import jsonpickle

from discourse.models.access_control import AccessControl

access_control = AccessControl(
    mandatory_acl=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    banned_acl=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)
```

