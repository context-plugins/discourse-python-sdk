
# T Invite Json Request

*This model accepts additional fields of type Any.*

## Structure

`TInviteJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user` | `str` | Optional | - |
| `email` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.t_invite_json_request import TInviteJsonRequest

t_invite_json_request = TInviteJsonRequest(
    user='user6',
    email='email0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

