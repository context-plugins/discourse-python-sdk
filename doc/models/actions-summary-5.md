
# Actions Summary 5

*This model accepts additional fields of type Any.*

## Structure

`ActionsSummary5`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | ID of the action type (e.g., 2 for like) |
| `count` | `int` | Optional | Number of times this action has been performed |
| `acted` | `bool` | Optional | Whether the current user has performed this<br>action |
| `can_undo` | `bool` | Optional | Whether the current user can undo this action |
| `can_act` | `bool` | Optional | Whether the current user can perform this action |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.actions_summary_5 import ActionsSummary5

actions_summary_5 = ActionsSummary5(
    id=146,
    count=26,
    acted=False,
    can_undo=False,
    can_act=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

