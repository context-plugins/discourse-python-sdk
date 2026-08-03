
# Suggested Topic

## Structure

`SuggestedTopic`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `title` | `str` | Required | - |
| `fancy_title` | `str` | Required | - |
| `slug` | `str` | Required | - |
| `posts_count` | `int` | Required | - |
| `reply_count` | `int` | Required | - |
| `highest_post_number` | `int` | Required | - |
| `image_url` | `str` | Required | - |
| `created_at` | `str` | Required | - |
| `last_posted_at` | `str` | Required | - |
| `bumped` | `bool` | Required | - |
| `bumped_at` | `str` | Required | - |
| `archetype` | `str` | Required | - |
| `unseen` | `bool` | Required | - |
| `pinned` | `bool` | Required | - |
| `unpinned` | `str` | Required | - |
| `excerpt` | `str` | Required | - |
| `visible` | `bool` | Required | - |
| `closed` | `bool` | Required | - |
| `archived` | `bool` | Required | - |
| `bookmarked` | `str` | Required | - |
| `liked` | `str` | Required | - |
| `tags` | [`List[Tag]`](../../doc/models/tag.md) | Required | - |
| `tags_descriptions` | `Any` | Required | - |
| `like_count` | `int` | Required | - |
| `views` | `int` | Required | - |
| `category_id` | `int` | Required | - |
| `featured_link` | `str` | Required | - |
| `posters` | [`List[Poster4]`](../../doc/models/poster-4.md) | Required | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.poster_4 import Poster4
from discourseapidocumentation.models.suggested_topic import SuggestedTopic
from discourseapidocumentation.models.tag import Tag
from discourseapidocumentation.models.user import User

suggested_topic = SuggestedTopic(
    id=98,
    title='title6',
    fancy_title='fancy_title0',
    slug='slug4',
    posts_count=236,
    reply_count=188,
    highest_post_number=76,
    image_url='image_url6',
    created_at='created_at8',
    last_posted_at='last_posted_at8',
    bumped=False,
    bumped_at='bumped_at6',
    archetype='archetype6',
    unseen=False,
    pinned=False,
    unpinned='unpinned2',
    excerpt='excerpt2',
    visible=False,
    closed=False,
    archived=False,
    bookmarked='bookmarked0',
    liked='liked8',
    tags=[
        Tag(
            id=26,
            name='name0',
            slug='slug4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    tags_descriptions=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    like_count=96,
    views=92,
    category_id=164,
    featured_link='featured_link6',
    posters=[
        Poster4(
            extras='extras2',
            description='description8',
            user=User(
                id=76,
                username='username0',
                name='name0',
                avatar_template='avatar_template0'
            )
        )
    ]
)
```

