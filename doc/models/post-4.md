
# Post 4

## Structure

`Post4`

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
| `version` | `int` | Required | - |
| `can_edit` | `bool` | Required | - |
| `can_delete` | `bool` | Required | - |
| `can_recover` | `bool` | Required | - |
| `can_see_hidden_post` | `bool` | Optional | - |
| `can_wiki` | `bool` | Required | - |
| `link_counts` | [`List[LinkCount]`](../../doc/models/link-count.md) | Required | - |
| `read` | `bool` | Required | - |
| `user_title` | `str` | Required | - |
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

## Example

```python
from discourseapidocumentation.models.actions_summary import ActionsSummary
from discourseapidocumentation.models.link_count import LinkCount
from discourseapidocumentation.models.post_4 import Post4

post_4 = Post4(
    id=128,
    name='name6',
    username='username4',
    avatar_template='avatar_template4',
    created_at='created_at6',
    cooked='cooked2',
    post_number=24,
    post_type=238,
    updated_at='updated_at8',
    reply_count=218,
    reply_to_post_number='reply_to_post_number2',
    quote_count=114,
    incoming_link_count=198,
    reads=210,
    readers_count=90,
    score=6.76,
    yours=False,
    topic_id=190,
    topic_slug='topic_slug4',
    display_username='display_username6',
    primary_group_name='primary_group_name4',
    flair_name='flair_name0',
    flair_url='flair_url6',
    flair_bg_color='flair_bg_color0',
    flair_color='flair_color0',
    version=100,
    can_edit=False,
    can_delete=False,
    can_recover=False,
    can_wiki=False,
    link_counts=[
        LinkCount(
            url='url4',
            internal=False,
            reflection=False,
            title='title6',
            clicks=220
        )
    ],
    read=False,
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
    user_id=224,
    hidden=False,
    trust_level=144,
    deleted_at='deleted_at4',
    user_deleted=False,
    edit_reason='edit_reason4',
    can_view_edit_history=False,
    wiki=False,
    reviewable_id=54,
    reviewable_score_count=152,
    reviewable_score_pending_count=126,
    can_see_hidden_post=False
)
```

