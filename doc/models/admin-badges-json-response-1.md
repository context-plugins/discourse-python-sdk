
# Admin Badges Json Response 1

## Structure

`AdminBadgesJsonResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `badge_types` | [`List[BadgeType]`](../../doc/models/badge-type.md) | Required | - |
| `badge` | [`Badge1`](../../doc/models/badge-1.md) | Required | - |

## Example

```python
from discourse.models.admin_badges_json_response_1 import AdminBadgesJsonResponse1
from discourse.models.badge_1 import Badge1
from discourse.models.badge_type import BadgeType

admin_badges_json_response_1 = AdminBadgesJsonResponse1(
    badge_types=[
        BadgeType(
            id=206,
            name='name0',
            sort_order=172
        )
    ],
    badge=Badge1(
        id=184,
        name='name0',
        description='description0',
        grant_count=198,
        allow_title=False,
        multiple_grant=False,
        icon='icon2',
        image_url='image_url6',
        image_upload_id=56,
        listable=False,
        enabled=False,
        badge_grouping_id=192,
        system=False,
        long_description='long_description2',
        slug='slug6',
        manually_grantable=False,
        query='query0',
        trigger='trigger8',
        target_posts=False,
        auto_revoke=False,
        show_posts=False,
        badge_type_id=208,
        show_in_post_header=False
    )
)
```

