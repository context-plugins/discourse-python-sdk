
# Posts Replies Json Response

*This model accepts additional fields of type Any.*

## Structure

`PostsRepliesJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `name` | `str` | Required | - |
| `username` | `str` | Required | - |
| `avatar_template` | `str` | Required | - |
| `created_at` | `str` | Required | - |
| `cooked` | `str` | Required | - |
| `post_number` | `int` | Required | - |
| `post_type` | `int` | Required | - |
| `posts_count` | `int` | Required | - |
| `updated_at` | `str` | Required | - |
| `reply_count` | `int` | Required | - |
| `reply_to_post_number` | `int` | Required | - |
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
| `version` | `int` | Required | - |
| `can_edit` | `bool` | Required | - |
| `can_delete` | `bool` | Required | - |
| `can_recover` | `bool` | Required | - |
| `can_see_hidden_post` | `bool` | Required | - |
| `can_wiki` | `bool` | Required | - |
| `user_title` | `str` | Required | - |
| `reply_to_user` | [`ReplyToUser`](../../doc/models/reply-to-user.md) | Required | - |
| `bookmarked` | `bool` | Required | - |
| `actions_summary` | [`List[ActionsSummary]`](../../doc/models/actions-summary.md) | Required | - |
| `moderator` | `bool` | Required | - |
| `admin` | `bool` | Required | - |
| `staff` | `bool` | Required | - |
| `user_id` | `int` | Required | - |
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
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.actions_summary import ActionsSummary
from discourse.models.posts_replies_json_response import PostsRepliesJsonResponse
from discourse.models.reply_to_user import ReplyToUser

posts_replies_json_response = PostsRepliesJsonResponse(
    id=16,
    name='name6',
    username='username6',
    avatar_template='avatar_template4',
    created_at='created_at4',
    cooked='cooked2',
    post_number=168,
    post_type=94,
    posts_count=154,
    updated_at='updated_at2',
    reply_count=106,
    reply_to_post_number=140,
    quote_count=30,
    incoming_link_count=54,
    reads=66,
    readers_count=54,
    score=202.76,
    yours=False,
    topic_id=46,
    topic_slug='topic_slug6',
    display_username='display_username6',
    primary_group_name='primary_group_name4',
    flair_name='flair_name0',
    flair_url='flair_url6',
    flair_bg_color='flair_bg_color0',
    flair_color='flair_color0',
    version=244,
    can_edit=False,
    can_delete=False,
    can_recover=False,
    can_see_hidden_post=False,
    can_wiki=False,
    user_title='user_title0',
    reply_to_user=ReplyToUser(
        username='username6',
        avatar_template='avatar_template6',
        id=20,
        name='name4'
    ),
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
    user_id=112,
    hidden=False,
    trust_level=0,
    deleted_at='deleted_at4',
    user_deleted=False,
    edit_reason='edit_reason4',
    can_view_edit_history=False,
    wiki=False,
    reviewable_id=166,
    reviewable_score_count=248,
    reviewable_score_pending_count=238,
    post_url='post_url8',
    flair_group_id=66,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

