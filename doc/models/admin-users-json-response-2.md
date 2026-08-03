
# Admin Users Json Response 2

*This model accepts additional fields of type Any.*

## Structure

`AdminUsersJsonResponse2`

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

from discourseapidocumentation.models.admin_users_json_response_2 import AdminUsersJsonResponse2

admin_users_json_response_2 = AdminUsersJsonResponse2(
    id=104,
    username='username8',
    name='name8',
    avatar_template='avatar_template2',
    active=False,
    admin=False,
    moderator=False,
    last_seen_at='last_seen_at4',
    last_emailed_at='last_emailed_at4',
    created_at='created_at6',
    last_seen_age=123.58,
    last_emailed_age=36.6,
    created_at_age=189.86,
    trust_level=88,
    manual_locked_trust_level='manual_locked_trust_level4',
    title='title4',
    time_read=52,
    staged=False,
    days_visited=124,
    posts_read_count=216,
    topics_entered=118,
    post_count=76,
    email='email8',
    secondary_emails=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

