
# Category Setting

## Structure

`CategorySetting`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auto_bump_cooldown_days` | `int` | Optional | - |
| `num_auto_bump_daily` | `int` | Optional | - |
| `require_reply_approval` | `bool` | Optional | - |
| `require_topic_approval` | `bool` | Optional | - |
| `nested_replies_default` | `bool` | Optional | - |
| `topic_posting_review_mode` | `str` | Optional | - |
| `reply_posting_review_mode` | `str` | Optional | - |

## Example

```python
from discourseapidocumentation.models.category_setting import CategorySetting

category_setting = CategorySetting(
    auto_bump_cooldown_days=170,
    num_auto_bump_daily=182,
    require_reply_approval=False,
    require_topic_approval=False,
    nested_replies_default=False
)
```

