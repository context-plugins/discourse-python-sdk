
# Admin Badges Json Request 1

## Structure

`AdminBadgesJsonRequest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | The name for the new badge. |
| `badge_type_id` | `int` | Required | The ID for the badge type. 1 for Gold, 2 for Silver,<br>3 for Bronze. |

## Example

```python
from discourse.models.admin_badges_json_request_1 import AdminBadgesJsonRequest1

admin_badges_json_request_1 = AdminBadgesJsonRequest1(
    name='name6',
    badge_type_id=192
)
```

