
# Post 3

*This model accepts additional fields of type Any.*

## Structure

`Post3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `name` | `str` | Optional | - |
| `username` | `str` | Optional | - |
| `avatar_template` | `str` | Optional | - |
| `created_at` | `str` | Optional | - |
| `cooked` | `str` | Optional | - |
| `post_number` | `int` | Optional | - |
| `post_type` | `int` | Optional | - |
| `updated_at` | `str` | Optional | - |
| `reply_count` | `int` | Optional | - |
| `reply_to_post_number` | `str` | Optional | - |
| `quote_count` | `int` | Optional | - |
| `incoming_link_count` | `int` | Optional | - |
| `reads` | `int` | Optional | - |
| `readers_count` | `int` | Optional | - |
| `score` | `float` | Optional | - |
| `yours` | `bool` | Optional | - |
| `topic_id` | `int` | Optional | - |
| `topic_slug` | `str` | Optional | - |
| `display_username` | `str` | Optional | - |
| `primary_group_name` | `str` | Optional | - |
| `flair_name` | `str` | Optional | - |
| `flair_url` | `str` | Optional | - |
| `flair_bg_color` | `str` | Optional | - |
| `flair_color` | `str` | Optional | - |
| `version` | `int` | Optional | - |
| `can_edit` | `bool` | Optional | - |
| `can_delete` | `bool` | Optional | - |
| `can_recover` | `bool` | Optional | - |
| `can_wiki` | `bool` | Optional | - |
| `read` | `bool` | Optional | - |
| `user_title` | `str` | Optional | - |
| `actions_summary` | [`List[ActionsSummary6]`](../../doc/models/actions-summary-6.md) | Optional | - |
| `moderator` | `bool` | Optional | - |
| `admin` | `bool` | Optional | - |
| `staff` | `bool` | Optional | - |
| `user_id` | `int` | Optional | - |
| `hidden` | `bool` | Optional | - |
| `trust_level` | `int` | Optional | - |
| `deleted_at` | `str` | Optional | - |
| `user_deleted` | `bool` | Optional | - |
| `edit_reason` | `str` | Optional | - |
| `can_view_edit_history` | `bool` | Optional | - |
| `wiki` | `bool` | Optional | - |
| `reviewable_id` | `int` | Optional | - |
| `reviewable_score_count` | `int` | Optional | - |
| `reviewable_score_pending_count` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.post_3 import Post3

post_3 = Post3(
    id=118,
    name='name4',
    username='username4',
    avatar_template='avatar_template6',
    created_at='created_at2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

