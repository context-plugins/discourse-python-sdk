
# T Invite Group Json Request

*This model accepts additional fields of type Any.*

## Structure

`TInviteGroupJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `group` | `str` | Optional | The name of the group to invite |
| `should_notify` | `bool` | Optional | Whether to notify the group, it defaults to true |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.t_invite_group_json_request import TInviteGroupJsonRequest

t_invite_group_json_request = TInviteGroupJsonRequest(
    group='group8',
    should_notify=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

