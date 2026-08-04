
# U Preferences Avatar Pick Json Request

## Structure

`UPreferencesAvatarPickJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `upload_id` | `int` | Required | - |
| `mtype` | [`Type1`](../../doc/models/type-1.md) | Required | - |

## Example

```python
from discourse.models.type_1 import Type1
from discourse.models.u_preferences_avatar_pick_json_request import UPreferencesAvatarPickJsonRequest

u_preferences_avatar_pick_json_request = UPreferencesAvatarPickJsonRequest(
    upload_id=206,
    mtype=Type1.GRAVATAR
)
```

