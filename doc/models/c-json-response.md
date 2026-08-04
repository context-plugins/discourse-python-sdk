
# C Json Response

## Structure

`CJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `users` | [`List[User]`](../../doc/models/user.md) | Optional | - |
| `primary_groups` | `List[Any]` | Optional | - |
| `topic_list` | [`TopicList`](../../doc/models/topic-list.md) | Required | - |

## Example

```python
import jsonpickle

from discourse.models.c_json_response import CJsonResponse
from discourse.models.poster import Poster
from discourse.models.top_tag import TopTag
from discourse.models.topic_1 import Topic1
from discourse.models.topic_list import TopicList
from discourse.models.user import User

c_json_response = CJsonResponse(
    topic_list=TopicList(
        can_create_topic=False,
        per_page=116,
        topics=[
            Topic1(
                id=54,
                title='title8',
                fancy_title='fancy_title6',
                slug='slug0',
                posts_count=192,
                reply_count=144,
                highest_post_number=224,
                image_url='image_url2',
                created_at='created_at4',
                last_posted_at='last_posted_at2',
                bumped=False,
                bumped_at='bumped_at2',
                archetype='archetype8',
                unseen=False,
                pinned=False,
                unpinned='unpinned8',
                excerpt='excerpt8',
                visible=False,
                closed=False,
                archived=False,
                bookmarked='bookmarked6',
                liked='liked2',
                views=136,
                like_count=52,
                has_summary=False,
                last_poster_username='last_poster_username2',
                category_id=208,
                pinned_globally=False,
                featured_link='featured_link2',
                posters=[
                    Poster(
                        extras='extras2',
                        description='description8',
                        user_id=60,
                        primary_group_id=232
                    )
                ]
            )
        ],
        top_tags=[
            TopTag(
                id=22,
                name='name8',
                slug='slug2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            TopTag(
                id=22,
                name='name8',
                slug='slug2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            TopTag(
                id=22,
                name='name8',
                slug='slug2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ]
    ),
    users=[
        User(
            id=58,
            username='username4',
            name='name6',
            avatar_template='avatar_template4'
        )
    ],
    primary_groups=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ]
)
```

