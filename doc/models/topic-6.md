
# Topic 6

*This model accepts additional fields of type Any.*

## Structure

`Topic6`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `title` | `str` | Optional | - |
| `fancy_title` | `str` | Optional | - |
| `slug` | `str` | Optional | - |
| `posts_count` | `int` | Optional | - |
| `reply_count` | `int` | Optional | - |
| `highest_post_number` | `int` | Optional | - |
| `image_url` | `str` | Optional | - |
| `created_at` | `str` | Optional | - |
| `last_posted_at` | `str` | Optional | - |
| `bumped` | `bool` | Optional | - |
| `bumped_at` | `str` | Optional | - |
| `archetype` | `str` | Optional | - |
| `unseen` | `bool` | Optional | - |
| `last_read_post_number` | `int` | Optional | - |
| `unread_posts` | `int` | Optional | - |
| `pinned` | `bool` | Optional | - |
| `unpinned` | `str` | Optional | - |
| `visible` | `bool` | Optional | - |
| `closed` | `bool` | Optional | - |
| `archived` | `bool` | Optional | - |
| `notification_level` | `int` | Optional | - |
| `bookmarked` | `bool` | Optional | - |
| `liked` | `bool` | Optional | - |
| `views` | `int` | Optional | - |
| `like_count` | `int` | Optional | - |
| `has_summary` | `bool` | Optional | - |
| `last_poster_username` | `str` | Optional | - |
| `category_id` | `int` | Optional | - |
| `op_like_count` | `int` | Optional | - |
| `pinned_globally` | `bool` | Optional | - |
| `featured_link` | `str` | Optional | - |
| `posters` | [`List[Poster1]`](../../doc/models/poster-1.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.topic_6 import Topic6

topic_6 = Topic6(
    id=134,
    title='title6',
    fancy_title='fancy_title8',
    slug='slug8',
    posts_count=16,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

