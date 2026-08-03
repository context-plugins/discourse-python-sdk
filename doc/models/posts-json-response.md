
# Posts Json Response

## Structure

`PostsJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `latest_posts` | [`List[LatestPost]`](../../doc/models/latest-post.md) | Required | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.actions_summary import ActionsSummary
from discourseapidocumentation.models.latest_post import LatestPost
from discourseapidocumentation.models.posts_json_response import PostsJsonResponse

posts_json_response = PostsJsonResponse(
    latest_posts=[
        LatestPost(
            id=36,
            name='name6',
            username='username4',
            avatar_template='avatar_template4',
            created_at='created_at4',
            cooked='cooked2',
            post_number=188,
            post_type=74,
            posts_count=174,
            updated_at='updated_at8',
            reply_count=126,
            reply_to_post_number='reply_to_post_number2',
            quote_count=50,
            incoming_link_count=34,
            reads=46,
            readers_count=182,
            score=113.36,
            yours=False,
            topic_id=26,
            topic_slug='topic_slug6',
            topic_title='topic_title2',
            topic_html_title='topic_html_title4',
            category_id=226,
            display_username='display_username6',
            primary_group_name='primary_group_name4',
            flair_name='flair_name0',
            flair_url='flair_url6',
            flair_bg_color='flair_bg_color0',
            flair_color='flair_color0',
            flair_group_id='flair_group_id4',
            badges_granted=[
                jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            ],
            version=8,
            can_edit=False,
            can_delete=False,
            can_recover=False,
            can_see_hidden_post=False,
            can_wiki=False,
            user_title='user_title0',
            bookmarked=False,
            raw='raw0',
            actions_summary=[
                ActionsSummary(
                    id=218,
                    can_act=False
                )
            ],
            moderator=False,
            admin=False,
            staff=False,
            user_id=132,
            hidden=False,
            trust_level=20,
            deleted_at='deleted_at4',
            user_deleted=False,
            edit_reason='edit_reason4',
            can_view_edit_history=False,
            wiki=False,
            excerpt='excerpt8',
            truncated=False,
            reviewable_id='reviewable_id4',
            reviewable_score_count=244,
            reviewable_score_pending_count=218,
            post_url='post_url2'
        )
    ]
)
```

