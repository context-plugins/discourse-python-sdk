
# Admin Users Silence Json Response

## Structure

`AdminUsersSilenceJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `silence` | [`Silence`](../../doc/models/silence.md) | Required | - |

## Example

```python
from discourse.models.admin_users_silence_json_response import AdminUsersSilenceJsonResponse
from discourse.models.silence import Silence
from discourse.models.silenced_by import SilencedBy

admin_users_silence_json_response = AdminUsersSilenceJsonResponse(
    silence=Silence(
        silenced=False,
        silence_reason='silence_reason2',
        full_silence_reason='full_silence_reason0',
        silenced_till='silenced_till2',
        silenced_at='silenced_at0',
        silenced_by=SilencedBy(
            id=46,
            username='username6',
            name='name4',
            avatar_template='avatar_template6'
        )
    )
)
```

