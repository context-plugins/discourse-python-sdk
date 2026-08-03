
# Silence

## Structure

`Silence`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `silenced` | `bool` | Required | - |
| `silence_reason` | `str` | Required | - |
| `full_silence_reason` | `str` | Required | - |
| `silenced_till` | `str` | Required | - |
| `silenced_at` | `str` | Required | - |
| `silenced_by` | [`SilencedBy`](../../doc/models/silenced-by.md) | Required | - |

## Example

```python
from discourseapidocumentation.models.silence import Silence
from discourseapidocumentation.models.silenced_by import SilencedBy

silence = Silence(
    silenced=False,
    silence_reason='silence_reason2',
    full_silence_reason='full_silence_reason0',
    silenced_till='silenced_till2',
    silenced_at='silenced_at0',
    silenced_by=SilencedBy(
        id=46,
        username='username6',
        name='name4',
        avatar_template='avatar_template6'
    )
)
```

