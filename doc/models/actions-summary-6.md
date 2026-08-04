
# Actions Summary 6

*This model accepts additional fields of type Any.*

## Structure

`ActionsSummary6`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `can_act` | `bool` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.actions_summary_6 import ActionsSummary6

actions_summary_6 = ActionsSummary6(
    id=108,
    can_act=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

