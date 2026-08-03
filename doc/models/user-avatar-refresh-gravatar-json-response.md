
# User Avatar Refresh Gravatar Json Response

## Structure

`UserAvatarRefreshGravatarJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gravatar_upload_id` | `int` | Required | - |
| `gravatar_avatar_template` | `str` | Required | - |

## Example

```python
from discourseapidocumentation.models.user_avatar_refresh_gravatar_json_response import UserAvatarRefreshGravatarJsonResponse

user_avatar_refresh_gravatar_json_response = UserAvatarRefreshGravatarJsonResponse(
    gravatar_upload_id=8,
    gravatar_avatar_template='gravatar_avatar_template2'
)
```

