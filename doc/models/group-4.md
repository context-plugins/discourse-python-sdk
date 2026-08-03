
# Group 4

## Structure

`Group4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `automatic` | `bool` | Required | - |
| `name` | `str` | Required | - |
| `display_name` | `str` | Required | - |
| `user_count` | `int` | Optional | - |
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
| `is_group_user` | `bool` | Optional | - |
| `is_group_owner` | `bool` | Optional | - |
| `members_visibility_level` | `int` | Required | - |
| `can_see_members` | `bool` | Required | - |
| `can_admin_group` | `bool` | Required | - |
| `can_edit_group` | `bool` | Optional | - |
| `publish_read_state` | `bool` | Required | - |

## Example

```python
from discourseapidocumentation.models.group_4 import Group4

group_4 = Group4(
    id=98,
    automatic=False,
    name='name0',
    display_name='display_name0',
    mentionable_level=182,
    messageable_level=38,
    visibility_level=142,
    primary_group=False,
    title='title6',
    grant_trust_level='grant_trust_level2',
    incoming_email='incoming_email0',
    has_messages=False,
    flair_url='flair_url0',
    flair_bg_color='flair_bg_color4',
    flair_color='flair_color4',
    bio_raw='bio_raw2',
    bio_cooked='bio_cooked6',
    bio_excerpt='bio_excerpt4',
    public_admission=False,
    public_exit=False,
    allow_membership_requests=False,
    full_name='full_name6',
    default_notification_level=58,
    membership_request_template='membership_request_template6',
    members_visibility_level=202,
    can_see_members=False,
    can_admin_group=False,
    publish_read_state=False,
    user_count=194,
    is_group_user=False,
    is_group_owner=False,
    can_edit_group=False
)
```

