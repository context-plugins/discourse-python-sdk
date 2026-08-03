
# Badge 3

## Structure

`Badge3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `name` | `str` | Required | - |
| `description` | `str` | Required | - |
| `grant_count` | `int` | Required | - |
| `allow_title` | `bool` | Required | - |
| `multiple_grant` | `bool` | Required | - |
| `icon` | `str` | Required | - |
| `image_url` | `str` | Required | - |
| `listable` | `bool` | Required | - |
| `enabled` | `bool` | Required | - |
| `badge_grouping_id` | `int` | Required | - |
| `system` | `bool` | Required | - |
| `slug` | `str` | Required | - |
| `manually_grantable` | `bool` | Required | - |
| `badge_type_id` | `int` | Required | - |

## Example

```python
from discourseapidocumentation.models.badge_3 import Badge3

badge_3 = Badge3(
    id=230,
    name='name2',
    description='description2',
    grant_count=244,
    allow_title=False,
    multiple_grant=False,
    icon='icon4',
    image_url='image_url8',
    listable=False,
    enabled=False,
    badge_grouping_id=110,
    system=False,
    slug='slug6',
    manually_grantable=False,
    badge_type_id=254
)
```

