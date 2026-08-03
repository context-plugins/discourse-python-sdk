
# Featured Topic

## Structure

`FeaturedTopic`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `title` | `str` | Required | - |
| `fancy_title` | `str` | Required | - |
| `slug` | `str` | Required | - |
| `posts_count` | `int` | Required | - |

## Example

```python
from discourseapidocumentation.models.featured_topic import FeaturedTopic

featured_topic = FeaturedTopic(
    id=50,
    title='title6',
    fancy_title='fancy_title0',
    slug='slug6',
    posts_count=188
)
```

