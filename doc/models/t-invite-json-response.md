
# T Invite Json Response

*This model accepts additional fields of type Any.*

## Structure

`TInviteJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user` | [`User1`](../../doc/models/user-1.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.t_invite_json_response import TInviteJsonResponse
from discourse.models.user_1 import User1

t_invite_json_response = TInviteJsonResponse(
    user=User1(
        id=76,
        username='username0',
        name='name0',
        avatar_template='avatar_template0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

