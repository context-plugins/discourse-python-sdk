
# Post Stream 1

## Structure

`PostStream1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `posts` | [`List[Post4]`](../../doc/models/post-4.md) | Required | - |
| `stream` | `List[Any]` | Required | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.actions_summary import ActionsSummary
from discourseapidocumentation.models.link_count import LinkCount
from discourseapidocumentation.models.post_4 import Post4
from discourseapidocumentation.models.post_stream_1 import PostStream1

post_stream_1 = PostStream1(
    posts=[
        Post4(
            id=64,
            name='name6',
            username='username6',
            avatar_template='avatar_template6',
            created_at='created_at4',
            cooked='cooked8',
            post_number=216,
            post_type=210,
            updated_at='updated_at2',
            reply_count=154,
            reply_to_post_number='reply_to_post_number2',
            quote_count=78,
            incoming_link_count=6,
            reads=238,
            readers_count=102,
            score=182.76,
            yours=False,
            topic_id=2,
            topic_slug='topic_slug6',
            display_username='display_username6',
            primary_group_name='primary_group_name4',
            flair_name='flair_name0',
            flair_url='flair_url6',
            flair_bg_color='flair_bg_color0',
            flair_color='flair_color0',
            version=36,
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
            user_id=160,
            hidden=False,
            trust_level=48,
            deleted_at='deleted_at4',
            user_deleted=False,
            edit_reason='edit_reason4',
            can_view_edit_history=False,
            wiki=False,
            reviewable_id=138,
            reviewable_score_count=40,
            reviewable_score_pending_count=190,
            can_see_hidden_post=False
        )
    ],
    stream=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ]
)
```

