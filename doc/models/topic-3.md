
# Topic 3

*This model accepts additional fields of type Any.*

## Structure

`Topic3`

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
| `category_id` | `str` | Optional | - |
| `pinned_globally` | `bool` | Optional | - |
| `featured_link` | `str` | Optional | - |
| `allowed_user_count` | `int` | Optional | - |
| `posters` | [`List[Poster1]`](../../doc/models/poster-1.md) | Optional | - |
| `participants` | `List[Any]` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.topic_3 import Topic3

topic_3 = Topic3(
    id=208,
    title='title2',
    fancy_title='fancy_title2',
    slug='slug4',
    posts_count=90,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

