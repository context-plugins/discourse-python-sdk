
# User Badges Json Response

## Structure

`UserBadgesJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `badges` | [`List[Badge3]`](../../doc/models/badge-3.md) | Optional | - |
| `badge_types` | [`List[BadgeType]`](../../doc/models/badge-type.md) | Optional | - |
| `granted_bies` | [`List[GrantedBy]`](../../doc/models/granted-by.md) | Optional | - |
| `user_badges` | [`List[UserBadge]`](../../doc/models/user-badge.md) | Required | - |

## Example

```python
from discourse.models.badge_3 import Badge3
from discourse.models.badge_type import BadgeType
from discourse.models.granted_by import GrantedBy
from discourse.models.user_badge import UserBadge
from discourse.models.user_badges_json_response import UserBadgesJsonResponse

user_badges_json_response = UserBadgesJsonResponse(
    user_badges=[
        UserBadge(
            id=222,
            granted_at='granted_at8',
            grouping_position=130,
            is_favorite='is_favorite8',
            can_favorite=False,
            badge_id=182,
            granted_by_id=28
        )
    ],
    badges=[
        Badge3(
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
            slug='slug6',
            manually_grantable=False,
            badge_type_id=92
        ),
        Badge3(
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
            slug='slug6',
            manually_grantable=False,
            badge_type_id=92
        ),
        Badge3(
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
            slug='slug6',
            manually_grantable=False,
            badge_type_id=92
        )
    ],
    badge_types=[
        BadgeType(
            id=206,
            name='name0',
            sort_order=172
        )
    ],
    granted_bies=[
        GrantedBy(
            id=198,
            username='username6',
            name='name6',
            avatar_template='avatar_template6',
            flair_name='flair_name0',
            admin=False,
            moderator=False,
            trust_level=182
        ),
        GrantedBy(
            id=198,
            username='username6',
            name='name6',
            avatar_template='avatar_template6',
            flair_name='flair_name0',
            admin=False,
            moderator=False,
            trust_level=182
        ),
        GrantedBy(
            id=198,
            username='username6',
            name='name6',
            avatar_template='avatar_template6',
            flair_name='flair_name0',
            admin=False,
            moderator=False,
            trust_level=182
        )
    ]
)
```

