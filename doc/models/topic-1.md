
# Topic 1

## Structure

`Topic1`

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
| `views` | `int` | Required | - |
| `like_count` | `int` | Required | - |
| `has_summary` | `bool` | Required | - |
| `last_poster_username` | `str` | Required | - |
| `category_id` | `int` | Required | - |
| `pinned_globally` | `bool` | Required | - |
| `featured_link` | `str` | Required | - |
| `posters` | [`List[Poster]`](../../doc/models/poster.md) | Required | - |

## Example

```python
from discourse.models.poster import Poster
from discourse.models.topic_1 import Topic1

topic_1 = Topic1(
    id=56,
    title='title4',
    fancy_title='fancy_title0',
    slug='slug6',
    posts_count=194,
    reply_count=146,
    highest_post_number=222,
    image_url='image_url6',
    created_at='created_at8',
    last_posted_at='last_posted_at8',
    bumped=False,
    bumped_at='bumped_at6',
    archetype='archetype4',
    unseen=False,
    pinned=False,
    unpinned='unpinned2',
    excerpt='excerpt2',
    visible=False,
    closed=False,
    archived=False,
    bookmarked='bookmarked0',
    liked='liked8',
    views=134,
    like_count=54,
    has_summary=False,
    last_poster_username='last_poster_username8',
    category_id=206,
    pinned_globally=False,
    featured_link='featured_link6',
    posters=[
        Poster(
            extras='extras2',
            description='description8',
            user_id=60,
            primary_group_id=232
        )
    ]
)
```

