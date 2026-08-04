
# Group 7

## Structure

`Group7`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `automatic` | `bool` | Required | - |
| `name` | `str` | Required | - |
| `display_name` | `str` | Required | - |
| `user_count` | `int` | Required | - |
| `mentionable_level` | `int` | Required | - |
| `messageable_level` | `int` | Required | - |
| `visibility_level` | `int` | Required | - |
| `primary_group` | `bool` | Required | - |
| `title` | `str` | Required | - |
| `grant_trust_level` | `str` | Required | - |
| `incoming_email` | `str` | Required | - |
| `has_messages` | `bool` | Required | - |
| `flair_url` | `str` | Required | - |
| `flair_bg_color` | `str` | Required | - |
| `flair_color` | `str` | Required | - |
| `bio_raw` | `str` | Required | - |
| `bio_cooked` | `str` | Required | - |
| `bio_excerpt` | `str` | Required | - |
| `public_admission` | `bool` | Required | - |
| `public_exit` | `bool` | Required | - |
| `allow_membership_requests` | `bool` | Required | - |
| `full_name` | `str` | Required | - |
| `default_notification_level` | `int` | Required | - |
| `membership_request_template` | `str` | Required | - |
| `members_visibility_level` | `int` | Required | - |
| `can_see_members` | `bool` | Required | - |
| `can_admin_group` | `bool` | Required | - |
| `publish_read_state` | `bool` | Required | - |

## Example

```python
from discourse.models.group_7 import Group7

group_7 = Group7(
    id=212,
    automatic=False,
    name='name8',
    display_name='display_name8',
    user_count=204,
    mentionable_level=40,
    messageable_level=152,
    visibility_level=0,
    primary_group=False,
    title='title6',
    grant_trust_level='grant_trust_level0',
    incoming_email='incoming_email2',
    has_messages=False,
    flair_url='flair_url8',
    flair_bg_color='flair_bg_color2',
    flair_color='flair_color2',
    bio_raw='bio_raw0',
    bio_cooked='bio_cooked6',
    bio_excerpt='bio_excerpt2',
    public_admission=False,
    public_exit=False,
    allow_membership_requests=False,
    full_name='full_name4',
    default_notification_level=172,
    membership_request_template='membership_request_template6',
    members_visibility_level=60,
    can_see_members=False,
    can_admin_group=False,
    publish_read_state=False
)
```

