
# Penalty Counts 1

## Structure

`PenaltyCounts1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `silenced` | `int` | Required | - |
| `suspended` | `int` | Required | - |
| `total` | `int` | Required | - |

## Example

```python
from discourse.models.penalty_counts_1 import PenaltyCounts1

penalty_counts_1 = PenaltyCounts1(
    silenced=76,
    suspended=206,
    total=34
)
```

