
# Post Action Type

## Structure

`PostActionType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `name_key` | `str` | Required | - |
| `name` | `str` | Required | - |
| `description` | `str` | Required | - |
| `short_description` | `str` | Required | - |
| `is_flag` | `bool` | Required | - |
| `require_message` | `bool` | Required | - |
| `enabled` | `bool` | Required | - |
| `applies_to` | `List[Any]` | Required | - |
| `is_used` | `bool` | Required | - |
| `position` | `int` | Optional | - |
| `auto_action_type` | `bool` | Required | - |
| `system` | `bool` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.post_action_type import PostActionType

post_action_type = PostActionType(
    id=14,
    name_key='name_key4',
    name='name0',
    description='description0',
    short_description='short_description6',
    is_flag=False,
    require_message=False,
    enabled=False,
    applies_to=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    is_used=False,
    auto_action_type=False,
    position=44,
    system=False
)
```

