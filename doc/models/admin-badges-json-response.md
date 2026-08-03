
# Admin Badges Json Response

## Structure

`AdminBadgesJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `badges` | [`List[Badge]`](../../doc/models/badge.md) | Required | - |
| `badge_types` | [`List[BadgeType]`](../../doc/models/badge-type.md) | Required | - |
| `badge_groupings` | [`List[BadgeGrouping]`](../../doc/models/badge-grouping.md) | Required | - |
| `admin_badges` | [`AdminBadges`](../../doc/models/admin-badges.md) | Required | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.admin_badges import AdminBadges
from discourseapidocumentation.models.admin_badges_json_response import AdminBadgesJsonResponse
from discourseapidocumentation.models.badge import Badge
from discourseapidocumentation.models.badge_grouping import BadgeGrouping
from discourseapidocumentation.models.badge_type import BadgeType
from discourseapidocumentation.models.triggers import Triggers

admin_badges_json_response = AdminBadgesJsonResponse(
    badges=[
        Badge(
            id=68,
            name='name0',
            description='description0',
            grant_count=82,
            allow_title=False,
            multiple_grant=False,
            icon='icon8',
            image_url='image_url6',
            listable=False,
            enabled=False,
            badge_grouping_id=52,
            system=False,
            long_description='long_description2',
            slug='slug6',
            manually_grantable=False,
            query='query0',
            trigger=158,
            target_posts=False,
            auto_revoke=False,
            show_posts=False,
            image_upload_id=172,
            badge_type_id=92,
            show_in_post_header=False,
            i_18_n_name='i18n_name4'
        )
    ],
    badge_types=[
        BadgeType(
            id=206,
            name='name0',
            sort_order=172
        )
    ],
    badge_groupings=[
        BadgeGrouping(
            id=40,
            name='name8',
            description='description8',
            position=70,
            system=False
        )
    ],
    admin_badges=AdminBadges(
        protected_system_fields=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        triggers=Triggers(
            user_change=26,
            none=198,
            post_revision=74,
            trust_level_change=164,
            post_action=132
        ),
        badge_ids=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        badge_grouping_ids=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        badge_type_ids=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ]
    )
)
```

