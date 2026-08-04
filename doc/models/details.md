
# Details

## Structure

`Details`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `can_edit` | `bool` | Required | - |
| `notification_level` | `int` | Required | - |
| `can_move_posts` | `bool` | Required | - |
| `can_delete` | `bool` | Required | - |
| `can_remove_allowed_users` | `bool` | Required | - |
| `can_create_post` | `bool` | Required | - |
| `can_reply_as_new_topic` | `bool` | Required | - |
| `can_invite_to` | `bool` | Optional | - |
| `can_invite_via_email` | `bool` | Optional | - |
| `can_flag_topic` | `bool` | Optional | - |
| `can_convert_topic` | `bool` | Required | - |
| `can_review_topic` | `bool` | Required | - |
| `can_close_topic` | `bool` | Required | - |
| `can_archive_topic` | `bool` | Required | - |
| `can_split_merge_topic` | `bool` | Required | - |
| `can_edit_staff_notes` | `bool` | Required | - |
| `can_toggle_topic_visibility` | `bool` | Required | - |
| `can_pin_unpin_topic` | `bool` | Required | - |
| `can_banner_topic` | `bool` | Optional | - |
| `can_moderate_category` | `bool` | Required | - |
| `can_remove_self_id` | `int` | Required | - |
| `participants` | [`List[Participant1]`](../../doc/models/participant-1.md) | Optional | - |
| `created_by` | [`CreatedBy`](../../doc/models/created-by.md) | Required | - |
| `last_poster` | [`LastPoster`](../../doc/models/last-poster.md) | Required | - |

## Example

```python
from discourse.models.created_by import CreatedBy
from discourse.models.details import Details
from discourse.models.last_poster import LastPoster
from discourse.models.participant_1 import Participant1

details = Details(
    can_edit=False,
    notification_level=30,
    can_move_posts=False,
    can_delete=False,
    can_remove_allowed_users=False,
    can_create_post=False,
    can_reply_as_new_topic=False,
    can_convert_topic=False,
    can_review_topic=False,
    can_close_topic=False,
    can_archive_topic=False,
    can_split_merge_topic=False,
    can_edit_staff_notes=False,
    can_toggle_topic_visibility=False,
    can_pin_unpin_topic=False,
    can_moderate_category=False,
    can_remove_self_id=168,
    created_by=CreatedBy(
        id=188,
        username='username8',
        name='name2',
        avatar_template='avatar_template8'
    ),
    last_poster=LastPoster(
        id=254,
        username='username2',
        name='name8',
        avatar_template='avatar_template2'
    ),
    can_invite_to=False,
    can_invite_via_email=False,
    can_flag_topic=False,
    can_banner_topic=False,
    participants=[
        Participant1(
            id=34,
            username='username4',
            name='name4',
            avatar_template='avatar_template6',
            post_count=6,
            primary_group_name='primary_group_name2',
            flair_name='flair_name8',
            flair_url='flair_url4',
            flair_color='flair_color8',
            flair_bg_color='flair_bg_color8',
            admin=False,
            moderator=False,
            trust_level=18,
            flair_group_id=84
        ),
        Participant1(
            id=34,
            username='username4',
            name='name4',
            avatar_template='avatar_template6',
            post_count=6,
            primary_group_name='primary_group_name2',
            flair_name='flair_name8',
            flair_url='flair_url4',
            flair_color='flair_color8',
            flair_bg_color='flair_bg_color8',
            admin=False,
            moderator=False,
            trust_level=18,
            flair_group_id=84
        ),
        Participant1(
            id=34,
            username='username4',
            name='name4',
            avatar_template='avatar_template6',
            post_count=6,
            primary_group_name='primary_group_name2',
            flair_name='flair_name8',
            flair_url='flair_url4',
            flair_color='flair_color8',
            flair_bg_color='flair_bg_color8',
            admin=False,
            moderator=False,
            trust_level=18,
            flair_group_id=84
        )
    ]
)
```

