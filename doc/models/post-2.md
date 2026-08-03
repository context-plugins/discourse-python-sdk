
# Post 2

## Structure

`Post2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `username` | `str` | Required | - |
| `avatar_template` | `str` | Required | - |
| `created_at` | `str` | Required | - |
| `cooked` | `str` | Required | - |
| `post_number` | `int` | Required | - |
| `post_type` | `int` | Required | - |
| `posts_count` | `int` | Required | - |
| `updated_at` | `str` | Required | - |
| `reply_count` | `int` | Required | - |
| `reply_to_post_number` | `str` | Required | - |
| `quote_count` | `int` | Required | - |
| `incoming_link_count` | `int` | Required | - |
| `reads` | `int` | Required | - |
| `readers_count` | `int` | Required | - |
| `score` | `float` | Required | - |
| `yours` | `bool` | Required | - |
| `topic_id` | `int` | Required | - |
| `topic_slug` | `str` | Required | - |
| `primary_group_name` | `str` | Required | - |
| `flair_name` | `str` | Required | - |
| `flair_url` | `str` | Required | - |
| `flair_bg_color` | `str` | Required | - |
| `flair_color` | `str` | Required | - |
| `flair_group_id` | `int` | Optional | - |
| `badges_granted` | `List[Any]` | Optional | - |
| `version` | `int` | Required | - |
| `can_edit` | `bool` | Required | - |
| `can_delete` | `bool` | Required | - |
| `can_recover` | `bool` | Required | - |
| `can_see_hidden_post` | `bool` | Optional | - |
| `can_wiki` | `bool` | Required | - |
| `user_title` | `str` | Required | - |
| `bookmarked` | `bool` | Required | - |
| `raw` | `str` | Required | - |
| `actions_summary` | [`List[ActionsSummary]`](../../doc/models/actions-summary.md) | Required | - |
| `moderator` | `bool` | Required | - |
| `admin` | `bool` | Required | - |
| `staff` | `bool` | Required | - |
| `user_id` | `int` | Required | - |
| `draft_sequence` | `int` | Required | - |
| `hidden` | `bool` | Required | - |
| `trust_level` | `int` | Required | - |
| `deleted_at` | `str` | Required | - |
| `user_deleted` | `bool` | Required | - |
| `edit_reason` | `str` | Required | - |
| `can_view_edit_history` | `bool` | Required | - |
| `wiki` | `bool` | Required | - |
| `reviewable_id` | `int` | Required | - |
| `reviewable_score_count` | `int` | Required | - |
| `reviewable_score_pending_count` | `int` | Required | - |
| `post_url` | `str` | Required | - |
| `post_localizations` | `List[Any]` | Optional | - |
| `mentioned_users` | `List[Any]` | Optional | - |
| `name` | `str` | Optional | - |
| `display_username` | `str` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.actions_summary import ActionsSummary
from discourseapidocumentation.models.post_2 import Post2

post_2 = Post2(
    id=124,
    username='username0',
    avatar_template='avatar_template0',
    created_at='created_at8',
    cooked='cooked8',
    post_number=20,
    post_type=242,
    posts_count=6,
    updated_at='updated_at6',
    reply_count=214,
    reply_to_post_number='reply_to_post_number6',
    quote_count=138,
    incoming_link_count=202,
    reads=42,
    readers_count=162,
    score=27.2,
    yours=False,
    topic_id=62,
    topic_slug='topic_slug0',
    primary_group_name='primary_group_name8',
    flair_name='flair_name4',
    flair_url='flair_url0',
    flair_bg_color='flair_bg_color4',
    flair_color='flair_color4',
    version=96,
    can_edit=False,
    can_delete=False,
    can_recover=False,
    can_wiki=False,
    user_title='user_title4',
    bookmarked=False,
    raw='raw4',
    actions_summary=[
        ActionsSummary(
            id=218,
            can_act=False
        )
    ],
    moderator=False,
    admin=False,
    staff=False,
    user_id=220,
    draft_sequence=10,
    hidden=False,
    trust_level=108,
    deleted_at='deleted_at8',
    user_deleted=False,
    edit_reason='edit_reason8',
    can_view_edit_history=False,
    wiki=False,
    reviewable_id=198,
    reviewable_score_count=100,
    reviewable_score_pending_count=130,
    post_url='post_url2',
    flair_group_id=174,
    badges_granted=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    can_see_hidden_post=False,
    post_localizations=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    mentioned_users=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ]
)
```

