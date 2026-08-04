
# Posts Json Request 2

## Structure

`PostsJsonRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `force_destroy` | `bool` | Optional | The `SiteSetting.can_permanently_delete` needs to be<br>enabled first before this param can be used. Also this endpoint<br>needs to be called first without `force_destroy` and then followed<br>up with a second call 5 minutes later with `force_destroy` to<br>permanently delete. |

## Example

```python
from discourse.models.posts_json_request_2 import PostsJsonRequest2

posts_json_request_2 = PostsJsonRequest2(
    force_destroy=True
)
```

