
# User Action

## Structure

`UserAction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `excerpt` | `str` | Required | - |
| `action_type` | `int` | Required | - |
| `created_at` | `str` | Required | - |
| `avatar_template` | `str` | Required | - |
| `acting_avatar_template` | `str` | Required | - |
| `slug` | `str` | Required | - |
| `topic_id` | `int` | Required | - |
| `target_user_id` | `int` | Required | - |
| `target_name` | `str` | Required | - |
| `target_username` | `str` | Required | - |
| `post_number` | `int` | Required | - |
| `post_id` | `str` | Required | - |
| `username` | `str` | Required | - |
| `name` | `str` | Required | - |
| `user_id` | `int` | Required | - |
| `acting_username` | `str` | Required | - |
| `acting_name` | `str` | Required | - |
| `acting_user_id` | `int` | Required | - |
| `title` | `str` | Required | - |
| `deleted` | `bool` | Required | - |
| `hidden` | `str` | Required | - |
| `post_type` | `str` | Required | - |
| `action_code` | `str` | Required | - |
| `category_id` | `int` | Required | - |
| `closed` | `bool` | Required | - |
| `archived` | `bool` | Required | - |

## Example

```python
from discourseapidocumentation.models.user_action import UserAction

user_action = UserAction(
    excerpt='excerpt4',
    action_type=122,
    created_at='created_at0',
    avatar_template='avatar_template2',
    acting_avatar_template='acting_avatar_template4',
    slug='slug6',
    topic_id=24,
    target_user_id=80,
    target_name='target_name6',
    target_username='target_username2',
    post_number=238,
    post_id='post_id6',
    username='username2',
    name='name2',
    user_id=182,
    acting_username='acting_username6',
    acting_name='acting_name8',
    acting_user_id=216,
    title='title8',
    deleted=False,
    hidden='hidden0',
    post_type='post_type4',
    action_code='action_code2',
    category_id=176,
    closed=False,
    archived=False
)
```

