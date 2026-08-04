
# Posts Json Response 1

## Structure

`PostsJsonResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `name` | `str` | Required | - |
| `username` | `str` | Required | - |
| `avatar_template` | `str` | Required | - |
| `created_at` | `str` | Required | - |
| `raw` | `str` | Optional | - |
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
| `display_username` | `str` | Required | - |
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

## Example

```python
import jsonpickle

from discourse.models.actions_summary import ActionsSummary
from discourse.models.posts_json_response_1 import PostsJsonResponse1

posts_json_response_1 = PostsJsonResponse1(
    id=200,
    name='name6',
    username='username4',
    avatar_template='avatar_template4',
    created_at='created_at4',
    cooked='cooked2',
    post_number=96,
    post_type=166,
    posts_count=82,
    updated_at='updated_at8',
    reply_count=34,
    reply_to_post_number='reply_to_post_number2',
    quote_count=214,
    incoming_link_count=126,
    reads=138,
    readers_count=18,
    score=91.96,
    yours=False,
    topic_id=118,
    topic_slug='topic_slug6',
    display_username='display_username6',
    primary_group_name='primary_group_name4',
    flair_name='flair_name0',
    flair_url='flair_url6',
    flair_bg_color='flair_bg_color0',
    flair_color='flair_color0',
    version=172,
    can_edit=False,
    can_delete=False,
    can_recover=False,
    can_wiki=False,
    user_title='user_title0',
    bookmarked=False,
    actions_summary=[
        ActionsSummary(
            id=218,
            can_act=False
        )
    ],
    moderator=False,
    admin=False,
    staff=False,
    user_id=40,
    draft_sequence=86,
    hidden=False,
    trust_level=72,
    deleted_at='deleted_at4',
    user_deleted=False,
    edit_reason='edit_reason4',
    can_view_edit_history=False,
    wiki=False,
    reviewable_id=238,
    reviewable_score_count=80,
    reviewable_score_pending_count=54,
    post_url='post_url2',
    raw='raw0',
    flair_group_id=250,
    badges_granted=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    can_see_hidden_post=False,
    post_localizations=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ]
)
```

