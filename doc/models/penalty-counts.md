
# Penalty Counts

## Structure

`PenaltyCounts`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `silenced` | `int` | Required | - |
| `suspended` | `int` | Required | - |

## Example

```python
from discourse.models.penalty_counts import PenaltyCounts

penalty_counts = PenaltyCounts(
    silenced=44,
    suspended=238
)
```

