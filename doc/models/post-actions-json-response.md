
# Post Actions Json Response

*This model accepts additional fields of type Any.*

## Structure

`PostActionsJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | The ID of the post |
| `name` | `str` | Required | The name of the post author |
| `username` | `str` | Required | The username of the post author |
| `avatar_template` | `str` | Required | Template for the author's avatar URL |
| `created_at` | `str` | Required | When the post was created |
| `cooked` | `str` | Required | The HTML content of the post |
| `post_number` | `int` | Required | The post number within the topic |
| `post_type` | `int` | Required | The type of post |
| `posts_count` | `int` | Required | Total posts count for the user |
| `updated_at` | `str` | Required | When the post was last updated |
| `reply_count` | `int` | Required | Number of replies to this post |
| `reply_to_post_number` | `str` | Required | Post number this post is replying to |
| `quote_count` | `int` | Required | Number of times this post has been quoted |
| `incoming_link_count` | `int` | Required | Number of incoming links to this post |
| `reads` | `int` | Required | Number of reads |
| `readers_count` | `int` | Required | Number of readers |
| `score` | `float` | Required | Post score |
| `yours` | `bool` | Required | Whether this post belongs to the current user |
| `topic_id` | `int` | Required | ID of the topic this post belongs to |
| `topic_slug` | `str` | Required | Slug of the topic this post belongs to |
| `display_username` | `str` | Required | Display username of the post author |
| `primary_group_name` | `str` | Required | Primary group name of the author |
| `flair_name` | `str` | Required | Flair name of the author |
| `flair_url` | `str` | Required | Flair URL of the author |
| `flair_bg_color` | `str` | Required | Flair background color of the author |
| `flair_color` | `str` | Required | Flair color of the author |
| `flair_group_id` | `int` | Required | Flair group ID of the author |
| `badges_granted` | `List[Any]` | Required | Badges granted to the user |
| `version` | `int` | Required | Version number of the post |
| `can_edit` | `bool` | Required | Whether the current user can edit this post |
| `can_delete` | `bool` | Required | Whether the current user can delete this post |
| `can_recover` | `bool` | Required | Whether the current user can recover this post |
| `can_see_hidden_post` | `bool` | Required | Whether the current user can see hidden posts |
| `can_wiki` | `bool` | Required | Whether the current user can wiki this post |
| `user_title` | `str` | Required | Title of the post author |
| `bookmarked` | `bool` | Required | Whether the post is bookmarked by the current user |
| `actions_summary` | [`List[ActionsSummary5]`](../../doc/models/actions-summary-5.md) | Required | Summary of actions performed on this post |
| `moderator` | `bool` | Required | Whether the post author is a moderator |
| `admin` | `bool` | Required | Whether the post author is an admin |
| `staff` | `bool` | Required | Whether the post author is staff |
| `user_id` | `int` | Required | ID of the post author |
| `hidden` | `bool` | Required | Whether the post is hidden |
| `trust_level` | `int` | Required | Trust level of the post author |
| `deleted_at` | `str` | Required | When the post was deleted |
| `user_deleted` | `bool` | Required | Whether the post was deleted by the user |
| `edit_reason` | `str` | Required | Reason for the last edit |
| `can_view_edit_history` | `bool` | Required | Whether the current user can view edit history |
| `wiki` | `bool` | Required | Whether this is a wiki post |
| `reviewable_id` | `int` | Required | ID of the reviewable if this post is under review |
| `reviewable_score_count` | `int` | Required | Number of reviewable scores |
| `reviewable_score_pending_count` | `int` | Required | Number of pending reviewable scores |
| `post_url` | `str` | Required | URL of the post |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.actions_summary_5 import ActionsSummary5
from discourseapidocumentation.models.post_actions_json_response import PostActionsJsonResponse

post_actions_json_response = PostActionsJsonResponse(
    id=126,
    name='name8',
    username='username2',
    avatar_template='avatar_template2',
    created_at='created_at6',
    cooked='cooked0',
    post_number=22,
    post_type=240,
    posts_count=8,
    updated_at='updated_at4',
    reply_count=216,
    reply_to_post_number='reply_to_post_number4',
    quote_count=140,
    incoming_link_count=200,
    reads=212,
    readers_count=164,
    score=196.18,
    yours=False,
    topic_id=192,
    topic_slug='topic_slug8',
    display_username='display_username8',
    primary_group_name='primary_group_name6',
    flair_name='flair_name8',
    flair_url='flair_url8',
    flair_bg_color='flair_bg_color2',
    flair_color='flair_color2',
    flair_group_id=176,
    badges_granted=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    version=98,
    can_edit=False,
    can_delete=False,
    can_recover=False,
    can_see_hidden_post=False,
    can_wiki=False,
    user_title='user_title2',
    bookmarked=False,
    actions_summary=[
        ActionsSummary5(
            id=218,
            count=46,
            acted=False,
            can_undo=False,
            can_act=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    moderator=False,
    admin=False,
    staff=False,
    user_id=222,
    hidden=False,
    trust_level=110,
    deleted_at='deleted_at6',
    user_deleted=False,
    edit_reason='edit_reason6',
    can_view_edit_history=False,
    wiki=False,
    reviewable_id=56,
    reviewable_score_count=102,
    reviewable_score_pending_count=128,
    post_url='post_url0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

