
# Actions Summary

## Structure

`ActionsSummary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `can_act` | `bool` | Required | - |

## Example

```python
from discourse.models.actions_summary import ActionsSummary

actions_summary = ActionsSummary(
    id=218,
    can_act=False
)
```

