
# Triggers

## Structure

`Triggers`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_change` | `int` | Required | - |
| `none` | `int` | Required | - |
| `post_revision` | `int` | Required | - |
| `trust_level_change` | `int` | Required | - |
| `post_action` | `int` | Required | - |

## Example

```python
from discourseapidocumentation.models.triggers import Triggers

triggers = Triggers(
    user_change=26,
    none=198,
    post_revision=74,
    trust_level_change=164,
    post_action=132
)
```

