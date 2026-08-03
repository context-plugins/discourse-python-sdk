
# Posts Json Response 2

*This model accepts additional fields of type Any.*

## Structure

`PostsJsonResponse2`

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
| `version` | `int` | Required | - |
| `can_edit` | `bool` | Required | - |
| `can_delete` | `bool` | Required | - |
| `can_recover` | `bool` | Required | - |
| `can_see_hidden_post` | `bool` | Optional | - |
| `can_wiki` | `bool` | Required | - |
| `user_title` | `str` | Required | - |
| `bookmarked` | `bool` | Required | - |
| `raw` | `str` | Required | - |
| `actions_summary` | [`List[ActionsSummary2]`](../../doc/models/actions-summary-2.md) | Required | - |
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
| `mentioned_users` | `List[Any]` | Optional | - |
| `name` | `str` | Optional | - |
| `display_username` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.actions_summary_2 import ActionsSummary2
from discourseapidocumentation.models.posts_json_response_2 import PostsJsonResponse2

posts_json_response_2 = PostsJsonResponse2(
    id=164,
    username='username2',
    avatar_template='avatar_template2',
    created_at='created_at0',
    cooked='cooked4',
    post_number=60,
    post_type=54,
    posts_count=46,
    updated_at='updated_at8',
    reply_count=254,
    reply_to_post_number='reply_to_post_number8',
    quote_count=178,
    incoming_link_count=162,
    reads=82,
    readers_count=202,
    score=160.72,
    yours=False,
    topic_id=102,
    topic_slug='topic_slug2',
    primary_group_name='primary_group_name0',
    flair_name='flair_name6',
    flair_url='flair_url2',
    flair_bg_color='flair_bg_color6',
    flair_color='flair_color6',
    version=136,
    can_edit=False,
    can_delete=False,
    can_recover=False,
    can_wiki=False,
    user_title='user_title6',
    bookmarked=False,
    raw='raw6',
    actions_summary=[
        ActionsSummary2(
            id=218,
            count=46,
            acted=False,
            can_undo=False,
            can_act=False
        )
    ],
    moderator=False,
    admin=False,
    staff=False,
    user_id=4,
    hidden=False,
    trust_level=148,
    deleted_at='deleted_at0',
    user_deleted=False,
    edit_reason='edit_reason0',
    can_view_edit_history=False,
    wiki=False,
    reviewable_id=238,
    reviewable_score_count=140,
    reviewable_score_pending_count=90,
    post_url='post_url4',
    flair_group_id=214,
    can_see_hidden_post=False,
    mentioned_users=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    name='name2',
    display_username='display_username2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

