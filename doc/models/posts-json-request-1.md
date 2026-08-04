
# Posts Json Request 1

## Structure

`PostsJsonRequest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `post` | [`Post1`](../../doc/models/post-1.md) | Optional | - |
| `bypass_bump` | `bool` | Optional | Skip bumping the topic when updating the post. Requires<br>staff or TL4 permissions. |

## Example

```python
from discourse.models.post_1 import Post1
from discourse.models.posts_json_request_1 import PostsJsonRequest1

posts_json_request_1 = PostsJsonRequest1(
    post=Post1(
        raw='raw4',
        edit_reason='edit_reason8'
    ),
    bypass_bump=False
)
```

