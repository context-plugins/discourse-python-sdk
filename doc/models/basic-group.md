
# Basic Group

## Structure

`BasicGroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `automatic` | `bool` | Required | - |
| `name` | `str` | Required | - |
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
| `can_edit_group` | `bool` | Optional | - |
| `publish_read_state` | `bool` | Required | - |

## Example

```python
from discourseapidocumentation.models.basic_group import BasicGroup

basic_group = BasicGroup(
    id=132,
    automatic=False,
    name='name8',
    user_count=28,
    mentionable_level=216,
    messageable_level=72,
    visibility_level=80,
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
    default_notification_level=92,
    membership_request_template='membership_request_template6',
    members_visibility_level=236,
    can_see_members=False,
    can_admin_group=False,
    publish_read_state=False,
    can_edit_group=False
)
```

