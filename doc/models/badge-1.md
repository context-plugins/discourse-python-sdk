
# Badge 1

## Structure

`Badge1`

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
| `image_upload_id` | `int` | Required | - |
| `listable` | `bool` | Required | - |
| `enabled` | `bool` | Required | - |
| `badge_grouping_id` | `int` | Required | - |
| `system` | `bool` | Required | - |
| `long_description` | `str` | Required | - |
| `slug` | `str` | Required | - |
| `manually_grantable` | `bool` | Required | - |
| `query` | `str` | Required | - |
| `trigger` | `str` | Required | - |
| `target_posts` | `bool` | Required | - |
| `auto_revoke` | `bool` | Required | - |
| `show_posts` | `bool` | Required | - |
| `badge_type_id` | `int` | Required | - |
| `show_in_post_header` | `bool` | Required | - |

## Example

```python
from discourseapidocumentation.models.badge_1 import Badge1

badge_1 = Badge1(
    id=220,
    name='name8',
    description='description8',
    grant_count=234,
    allow_title=False,
    multiple_grant=False,
    icon='icon0',
    image_url='image_url4',
    image_upload_id=236,
    listable=False,
    enabled=False,
    badge_grouping_id=100,
    system=False,
    long_description='long_description0',
    slug='slug2',
    manually_grantable=False,
    query='query8',
    trigger='trigger0',
    target_posts=False,
    auto_revoke=False,
    show_posts=False,
    badge_type_id=244,
    show_in_post_header=False
)
```

