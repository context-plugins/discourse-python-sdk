
# Posts Json Response 3

## Structure

`PostsJsonResponse3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `post` | [`Post2`](../../doc/models/post-2.md) | Required | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.actions_summary import ActionsSummary
from discourseapidocumentation.models.post_2 import Post2
from discourseapidocumentation.models.posts_json_response_3 import PostsJsonResponse3

posts_json_response_3 = PostsJsonResponse3(
    post=Post2(
        id=236,
        username='username0',
        avatar_template='avatar_template0',
        created_at='created_at8',
        cooked='cooked8',
        post_number=132,
        post_type=130,
        posts_count=118,
        updated_at='updated_at6',
        reply_count=70,
        reply_to_post_number='reply_to_post_number6',
        quote_count=250,
        incoming_link_count=90,
        reads=102,
        readers_count=18,
        score=253.6,
        yours=False,
        topic_id=82,
        topic_slug='topic_slug0',
        primary_group_name='primary_group_name8',
        flair_name='flair_name4',
        flair_url='flair_url0',
        flair_bg_color='flair_bg_color4',
        flair_color='flair_color4',
        version=208,
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
        user_id=76,
        draft_sequence=122,
        hidden=False,
        trust_level=220,
        deleted_at='deleted_at8',
        user_deleted=False,
        edit_reason='edit_reason8',
        can_view_edit_history=False,
        wiki=False,
        reviewable_id=54,
        reviewable_score_count=212,
        reviewable_score_pending_count=18,
        post_url='post_url2',
        flair_group_id=30,
        badges_granted=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        can_see_hidden_post=False,
        post_localizations=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        mentioned_users=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ]
    )
)
```

