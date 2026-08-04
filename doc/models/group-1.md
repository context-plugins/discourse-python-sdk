
# Group 1

## Structure

`Group1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `automatic` | `bool` | Required | - |
| `name` | `str` | Required | - |
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
| `is_group_user` | `bool` | Required | - |
| `members_visibility_level` | `int` | Required | - |
| `can_see_members` | `bool` | Required | - |
| `can_admin_group` | `bool` | Required | - |
| `can_edit_group` | `bool` | Optional | - |
| `publish_read_state` | `bool` | Required | - |
| `is_group_owner_display` | `bool` | Required | - |
| `mentionable` | `bool` | Required | - |
| `messageable` | `bool` | Required | - |
| `automatic_membership_email_domains` | `str` | Required | - |
| `smtp_updated_at` | `str` | Optional | - |
| `smtp_updated_by` | `Any` | Optional | - |
| `smtp_enabled` | `bool` | Optional | - |
| `smtp_server` | `str` | Required | - |
| `smtp_port` | `str` | Required | - |
| `smtp_ssl_mode` | `int` | Required | - |
| `email_username` | `str` | Required | - |
| `email_from_alias` | `str` | Optional | - |
| `email_password` | `str` | Required | - |
| `message_count` | `int` | Required | - |
| `allow_unknown_sender_topic_replies` | `bool` | Required | - |
| `associated_group_ids` | `List[Any]` | Optional | - |
| `watching_category_ids` | `List[Any]` | Required | - |
| `tracking_category_ids` | `List[Any]` | Required | - |
| `watching_first_post_category_ids` | `List[Any]` | Required | - |
| `regular_category_ids` | `List[Any]` | Required | - |
| `muted_category_ids` | `List[Any]` | Required | - |
| `watching_tags` | `List[Any]` | Optional | - |
| `watching_first_post_tags` | `List[Any]` | Optional | - |
| `tracking_tags` | `List[Any]` | Optional | - |
| `regular_tags` | `List[Any]` | Optional | - |
| `muted_tags` | `List[Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.group_1 import Group1

group_1 = Group1(
    id=20,
    automatic=False,
    name='name4',
    mentionable_level=104,
    messageable_level=216,
    visibility_level=192,
    primary_group=False,
    title='title0',
    grant_trust_level='grant_trust_level6',
    incoming_email='incoming_email6',
    has_messages=False,
    flair_url='flair_url4',
    flair_bg_color='flair_bg_color8',
    flair_color='flair_color2',
    bio_raw='bio_raw4',
    bio_cooked='bio_cooked0',
    bio_excerpt='bio_excerpt8',
    public_admission=False,
    public_exit=False,
    allow_membership_requests=False,
    full_name='full_name0',
    default_notification_level=236,
    membership_request_template='membership_request_template0',
    is_group_user=False,
    members_visibility_level=124,
    can_see_members=False,
    can_admin_group=False,
    publish_read_state=False,
    is_group_owner_display=False,
    mentionable=False,
    messageable=False,
    automatic_membership_email_domains='automatic_membership_email_domains8',
    smtp_server='smtp_server4',
    smtp_port='smtp_port6',
    smtp_ssl_mode=32,
    email_username='email_username2',
    email_password='email_password6',
    message_count=222,
    allow_unknown_sender_topic_replies=False,
    watching_category_ids=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    tracking_category_ids=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    watching_first_post_category_ids=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    regular_category_ids=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    muted_category_ids=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    user_count=140,
    can_edit_group=False,
    smtp_updated_at='smtp_updated_at2',
    smtp_updated_by=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    smtp_enabled=False
)
```

