
# Groups Members Json Response

## Structure

`GroupsMembersJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `members` | [`List[Member]`](../../doc/models/member.md) | Required | - |
| `owners` | [`List[Owner]`](../../doc/models/owner.md) | Required | - |
| `meta` | [`Meta`](../../doc/models/meta.md) | Required | - |

## Example

```python
from discourse.models.groups_members_json_response import GroupsMembersJsonResponse
from discourse.models.member import Member
from discourse.models.meta import Meta
from discourse.models.owner import Owner

groups_members_json_response = GroupsMembersJsonResponse(
    members=[
        Member(
            id=204,
            username='username2',
            name='name8',
            avatar_template='avatar_template2',
            title='title6',
            last_posted_at='last_posted_at0',
            last_seen_at='last_seen_at4',
            added_at='added_at6',
            timezone='timezone2'
        )
    ],
    owners=[
        Owner(
            id=210,
            username='username6',
            name='name4',
            avatar_template='avatar_template6',
            title='title0',
            last_posted_at='last_posted_at4',
            last_seen_at='last_seen_at0',
            added_at='added_at0',
            timezone='timezone6'
        )
    ],
    meta=Meta(
        total=36,
        limit=126,
        offset=222
    )
)
```

