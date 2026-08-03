
# Actions Summary 2

## Structure

`ActionsSummary2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | `2`: like, `3`, `4`, `6`, `7`, `8`: flag |
| `count` | `int` | Optional | - |
| `acted` | `bool` | Optional | - |
| `can_undo` | `bool` | Optional | - |
| `can_act` | `bool` | Optional | - |

## Example

```python
from discourseapidocumentation.models.actions_summary_2 import ActionsSummary2

actions_summary_2 = ActionsSummary2(
    id=34,
    count=138,
    acted=False,
    can_undo=False,
    can_act=False
)
```

