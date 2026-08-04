
# Post

## Structure

`Post`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `post_number` | `int` | Required | - |
| `url` | `str` | Required | - |
| `category_slug` | `str` | Required | - |
| `topic` | [`Topic`](../../doc/models/topic.md) | Required | - |

## Example

```python
import jsonpickle

from discourse.models.post import Post
from discourse.models.topic import Topic

post = Post(
    id=236,
    post_number=132,
    url='url4',
    category_slug='category_slug4',
    topic=Topic(
        id=54,
        title='title4',
        tags=[
            'tags3'
        ],
        tags_descriptions=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        slug='slug2'
    )
)
```

