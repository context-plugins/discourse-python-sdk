
# Admin Badges Json Request

## Structure

`AdminBadgesJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | The name for the new badge. |
| `badge_type_id` | `int` | Required | The ID for the badge type. 1 for Gold, 2 for Silver,<br>3 for Bronze. |

## Example

```python
from discourseapidocumentation.models.admin_badges_json_request import AdminBadgesJsonRequest

admin_badges_json_request = AdminBadgesJsonRequest(
    name='name8',
    badge_type_id=72
)
```

