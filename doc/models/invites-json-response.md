
# Invites Json Response

## Structure

`InvitesJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `invite_key` | `str` | Required | - |
| `link` | `str` | Required | - |
| `description` | `str` | Required | - |
| `email` | `str` | Required | - |
| `domain` | `str` | Required | - |
| `emailed` | `bool` | Required | - |
| `can_delete_invite` | `bool` | Required | - |
| `custom_message` | `str` | Required | - |
| `created_at` | `str` | Required | - |
| `updated_at` | `str` | Required | - |
| `expires_at` | `str` | Required | - |
| `expired` | `bool` | Required | - |
| `grants_admin` | `bool` | Required | - |
| `grants_moderator` | `bool` | Required | - |
| `topics` | `List[Any]` | Required | - |
| `groups` | `List[Any]` | Required | - |

## Example

```python
from discourseapidocumentation.models.invites_json_response import InvitesJsonResponse

invites_json_response = InvitesJsonResponse(
    id=42,
    invite_key='invite_key8',
    link='http://example.com/invites/9045fd767efe201ca60c6658bcf14158',
    description='description8',
    email='not-a-user-yet@example.com',
    domain='domain4',
    emailed=False,
    can_delete_invite=False,
    custom_message='Hello world!',
    created_at='2021-01-01T12:00:00.000Z',
    updated_at='2021-01-01T12:00:00.000Z',
    expires_at='2021-02-01T12:00:00.000Z',
    expired=False,
    grants_admin=False,
    grants_moderator=False,
    topics=[],
    groups=[]
)
```

