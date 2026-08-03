
# Post Actions Json Request

## Structure

`PostActionsJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | The ID of the post to perform the action on |
| `post_action_type_id` | `int` | Required | The ID of the post action type (e.g., 2 for like) |
| `flag_topic` | `bool` | Optional | Whether to flag the entire topic |

## Example

```python
from discourseapidocumentation.models.post_actions_json_request import PostActionsJsonRequest

post_actions_json_request = PostActionsJsonRequest(
    id=16,
    post_action_type_id=14,
    flag_topic=False
)
```

