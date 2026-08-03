
# Invites Json Request

## Structure

`InvitesJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Optional | required for email invites only |
| `skip_email` | `bool` | Optional | **Default**: `False` |
| `custom_message` | `str` | Optional | optional, for email invites |
| `max_redemptions_allowed` | `int` | Optional | optional, for link invites<br><br>**Default**: `1` |
| `topic_id` | `int` | Optional | - |
| `group_ids` | `str` | Optional | Optional, either this or `group_names`. Comma separated<br>list for multiple ids. |
| `group_names` | `str` | Optional | Optional, either this or `group_ids`. Comma separated<br>list for multiple names. |
| `expires_at` | `str` | Optional | optional, if not supplied, the invite_expiry_days site<br>setting is used |

## Example

```python
from discourseapidocumentation.models.invites_json_request import InvitesJsonRequest

invites_json_request = InvitesJsonRequest(
    email='not-a-user-yet@example.com',
    skip_email=False,
    custom_message='custom_message2',
    max_redemptions_allowed=5,
    topic_id=198,
    group_ids='42,43',
    group_names='foo,bar'
)
```

