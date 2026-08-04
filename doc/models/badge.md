
# Badge

## Structure

`Badge`

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
| `long_description` | `str` | Required | - |
| `slug` | `str` | Required | - |
| `manually_grantable` | `bool` | Required | - |
| `query` | `str` | Required | - |
| `trigger` | `int` | Required | - |
| `target_posts` | `bool` | Required | - |
| `auto_revoke` | `bool` | Required | - |
| `show_posts` | `bool` | Required | - |
| `i_18_n_name` | `str` | Optional | - |
| `image_upload_id` | `int` | Required | - |
| `badge_type_id` | `int` | Required | - |
| `show_in_post_header` | `bool` | Required | - |

## Example

```python
from discourse.models.badge import Badge

badge = Badge(
    id=184,
    name='name0',
    description='description0',
    grant_count=198,
    allow_title=False,
    multiple_grant=False,
    icon='icon2',
    image_url='image_url6',
    listable=False,
    enabled=False,
    badge_grouping_id=192,
    system=False,
    long_description='long_description2',
    slug='slug6',
    manually_grantable=False,
    query='query0',
    trigger=42,
    target_posts=False,
    auto_revoke=False,
    show_posts=False,
    image_upload_id=56,
    badge_type_id=208,
    show_in_post_header=False,
    i_18_n_name='i18n_name4'
)
```

