
# Directory Item

## Structure

`DirectoryItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `likes_received` | `int` | Required | - |
| `likes_given` | `int` | Required | - |
| `topics_entered` | `int` | Required | - |
| `topic_count` | `int` | Required | - |
| `post_count` | `int` | Required | - |
| `posts_read` | `int` | Required | - |
| `days_visited` | `int` | Required | - |
| `user` | [`User11`](../../doc/models/user-11.md) | Required | - |

## Example

```python
from discourse.models.directory_item import DirectoryItem
from discourse.models.user_11 import User11

directory_item = DirectoryItem(
    id=230,
    likes_received=12,
    likes_given=152,
    topics_entered=244,
    topic_count=130,
    post_count=202,
    posts_read=24,
    days_visited=250,
    user=User11(
        id=76,
        username='username0',
        name='name0',
        avatar_template='avatar_template0',
        title='title4'
    )
)
```

