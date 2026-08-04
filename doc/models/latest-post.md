
# Latest Post

## Structure

`LatestPost`

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
| `reply_to_post_number` | `str` | Required | - |
| `quote_count` | `int` | Required | - |
| `incoming_link_count` | `int` | Required | - |
| `reads` | `int` | Required | - |
| `readers_count` | `int` | Required | - |
| `score` | `float` | Required | - |
| `yours` | `bool` | Required | - |
| `topic_id` | `int` | Required | - |
| `topic_slug` | `str` | Required | - |
| `topic_title` | `str` | Required | - |
| `topic_html_title` | `str` | Required | - |
| `category_id` | `int` | Required | - |
| `display_username` | `str` | Required | - |
| `primary_group_name` | `str` | Required | - |
| `flair_name` | `str` | Required | - |
| `flair_url` | `str` | Required | - |
| `flair_bg_color` | `str` | Required | - |
| `flair_color` | `str` | Required | - |
| `flair_group_id` | `str` | Required | - |
| `badges_granted` | `List[Any]` | Required | - |
| `version` | `int` | Required | - |
| `can_edit` | `bool` | Required | - |
| `can_delete` | `bool` | Required | - |
| `can_recover` | `bool` | Required | - |
| `can_see_hidden_post` | `bool` | Required | - |
| `can_wiki` | `bool` | Required | - |
| `user_title` | `str` | Required | - |
| `bookmarked` | `bool` | Required | - |
| `raw` | `str` | Required | - |
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
| `excerpt` | `str` | Required | - |
| `truncated` | `bool` | Required | - |
| `reviewable_id` | `str` | Required | - |
| `reviewable_score_count` | `int` | Required | - |
| `reviewable_score_pending_count` | `int` | Required | - |
| `post_url` | `str` | Required | - |

## Example

```python
import jsonpickle

from discourse.models.actions_summary import ActionsSummary
from discourse.models.latest_post import LatestPost

latest_post = LatestPost(
    id=140,
    name='name0',
    username='username0',
    avatar_template='avatar_template0',
    created_at='created_at8',
    cooked='cooked8',
    post_number=36,
    post_type=226,
    posts_count=22,
    updated_at='updated_at6',
    reply_count=230,
    reply_to_post_number='reply_to_post_number6',
    quote_count=154,
    incoming_link_count=186,
    reads=58,
    readers_count=178,
    score=255.2,
    yours=False,
    topic_id=178,
    topic_slug='topic_slug0',
    topic_title='topic_title6',
    topic_html_title='topic_html_title0',
    category_id=122,
    display_username='display_username0',
    primary_group_name='primary_group_name8',
    flair_name='flair_name4',
    flair_url='flair_url0',
    flair_bg_color='flair_bg_color4',
    flair_color='flair_color4',
    flair_group_id='flair_group_id8',
    badges_granted=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    version=112,
    can_edit=False,
    can_delete=False,
    can_recover=False,
    can_see_hidden_post=False,
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
    user_id=236,
    hidden=False,
    trust_level=124,
    deleted_at='deleted_at8',
    user_deleted=False,
    edit_reason='edit_reason8',
    can_view_edit_history=False,
    wiki=False,
    excerpt='excerpt2',
    truncated=False,
    reviewable_id='reviewable_id0',
    reviewable_score_count=116,
    reviewable_score_pending_count=114,
    post_url='post_url2'
)
```

