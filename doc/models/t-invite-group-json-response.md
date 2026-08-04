
# T Invite Group Json Response

*This model accepts additional fields of type Any.*

## Structure

`TInviteGroupJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `group` | [`Group6`](../../doc/models/group-6.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.group_6 import Group6
from discourse.models.t_invite_group_json_response import TInviteGroupJsonResponse

t_invite_group_json_response = TInviteGroupJsonResponse(
    group=Group6(
        id=38,
        name='name8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

