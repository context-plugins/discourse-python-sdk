
# Directory Items Json Response

## Structure

`DirectoryItemsJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `directory_items` | [`List[DirectoryItem]`](../../doc/models/directory-item.md) | Required | - |
| `meta` | [`Meta1`](../../doc/models/meta-1.md) | Required | - |

## Example

```python
from discourseapidocumentation.models.directory_item import DirectoryItem
from discourseapidocumentation.models.directory_items_json_response import DirectoryItemsJsonResponse
from discourseapidocumentation.models.meta_1 import Meta1
from discourseapidocumentation.models.user_11 import User11

directory_items_json_response = DirectoryItemsJsonResponse(
    directory_items=[
        DirectoryItem(
            id=130,
            likes_received=168,
            likes_given=52,
            topics_entered=144,
            topic_count=30,
            post_count=102,
            posts_read=132,
            days_visited=150,
            user=User11(
                id=76,
                username='username0',
                name='name0',
                avatar_template='avatar_template0',
                title='title4'
            )
        )
    ],
    meta=Meta1(
        last_updated_at='last_updated_at6',
        total_rows_directory_items=140,
        load_more_directory_items='load_more_directory_items0'
    )
)
```

