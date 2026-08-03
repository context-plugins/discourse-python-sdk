
# Invites Create Multiple Json Request

*This model accepts additional fields of type Any.*

## Structure

`InvitesCreateMultipleJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Optional | pass 1 email per invite to be generated. other properties<br>will be shared by each invite. |
| `skip_email` | `bool` | Optional | **Default**: `False` |
| `custom_message` | `str` | Optional | optional, for email invites |
| `max_redemptions_allowed` | `int` | Optional | optional, for link invites<br><br>**Default**: `1` |
| `topic_id` | `int` | Optional | - |
| `group_ids` | `str` | Optional | Optional, either this or `group_names`. Comma separated<br>list for multiple ids. |
| `group_names` | `str` | Optional | Optional, either this or `group_ids`. Comma separated<br>list for multiple names. |
| `expires_at` | `str` | Optional | optional, if not supplied, the invite_expiry_days site<br>setting is used |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.invites_create_multiple_json_request import InvitesCreateMultipleJsonRequest

invites_create_multiple_json_request = InvitesCreateMultipleJsonRequest(
    email='[\n  "not-a-user-yet-1@example.com",\n  "not-a-user-yet-2@example.com"\n]',
    skip_email=False,
    custom_message='custom_message4',
    max_redemptions_allowed=5,
    topic_id=80,
    group_ids='42,43',
    group_names='foo,bar',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

