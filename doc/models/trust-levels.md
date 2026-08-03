
# Trust Levels

## Structure

`TrustLevels`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `newuser` | `int` | Required | - |
| `basic` | `int` | Required | - |
| `member` | `int` | Required | - |
| `regular` | `int` | Required | - |
| `leader` | `int` | Required | - |

## Example

```python
from discourseapidocumentation.models.trust_levels import TrustLevels

trust_levels = TrustLevels(
    newuser=196,
    basic=160,
    member=18,
    regular=28,
    leader=70
)
```

