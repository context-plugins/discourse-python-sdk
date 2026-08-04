
# Admin Users List Json Response

*This model accepts additional fields of type Any.*

## Structure

`AdminUsersListJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `username` | `str` | Required | - |
| `name` | `str` | Required | - |
| `avatar_template` | `str` | Required | - |
| `email` | `str` | Optional | - |
| `secondary_emails` | `List[Any]` | Optional | - |
| `active` | `bool` | Required | - |
| `admin` | `bool` | Required | - |
| `moderator` | `bool` | Required | - |
| `last_seen_at` | `str` | Required | - |
| `last_emailed_at` | `str` | Required | - |
| `created_at` | `str` | Required | - |
| `last_seen_age` | `float` | Required | - |
| `last_emailed_age` | `float` | Required | - |
| `created_at_age` | `float` | Required | - |
| `trust_level` | `int` | Required | - |
| `manual_locked_trust_level` | `str` | Required | - |
| `title` | `str` | Required | - |
| `time_read` | `int` | Required | - |
| `staged` | `bool` | Required | - |
| `days_visited` | `int` | Required | - |
| `posts_read_count` | `int` | Required | - |
| `topics_entered` | `int` | Required | - |
| `post_count` | `int` | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.admin_users_list_json_response import AdminUsersListJsonResponse

admin_users_list_json_response = AdminUsersListJsonResponse(
    id=244,
    username='username8',
    name='name2',
    avatar_template='avatar_template8',
    active=False,
    admin=False,
    moderator=False,
    last_seen_at='last_seen_at8',
    last_emailed_at='last_emailed_at0',
    created_at='created_at0',
    last_seen_age=122.42,
    last_emailed_age=35.44,
    created_at_age=188.7,
    trust_level=28,
    manual_locked_trust_level='manual_locked_trust_level0',
    title='title2',
    time_read=192,
    staged=False,
    days_visited=8,
    posts_read_count=156,
    topics_entered=254,
    post_count=216,
    email='email4',
    secondary_emails=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

