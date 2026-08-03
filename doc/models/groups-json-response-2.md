
# Groups Json Response 2

## Structure

`GroupsJsonResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `groups` | [`List[Group4]`](../../doc/models/group-4.md) | Required | - |
| `extras` | [`Extras2`](../../doc/models/extras-2.md) | Required | - |
| `total_rows_groups` | `int` | Required | - |
| `load_more_groups` | `str` | Required | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.extras_2 import Extras2
from discourseapidocumentation.models.group_4 import Group4
from discourseapidocumentation.models.groups_json_response_2 import GroupsJsonResponse2

groups_json_response_2 = GroupsJsonResponse2(
    groups=[
        Group4(
            id=152,
            automatic=False,
            name='name6',
            display_name='display_name6',
            mentionable_level=236,
            messageable_level=92,
            visibility_level=196,
            primary_group=False,
            title='title2',
            grant_trust_level='grant_trust_level8',
            incoming_email='incoming_email6',
            has_messages=False,
            flair_url='flair_url6',
            flair_bg_color='flair_bg_color0',
            flair_color='flair_color0',
            bio_raw='bio_raw8',
            bio_cooked='bio_cooked2',
            bio_excerpt='bio_excerpt0',
            public_admission=False,
            public_exit=False,
            allow_membership_requests=False,
            full_name='full_name2',
            default_notification_level=112,
            membership_request_template='membership_request_template2',
            members_visibility_level=0,
            can_see_members=False,
            can_admin_group=False,
            publish_read_state=False,
            user_count=248,
            is_group_user=False,
            is_group_owner=False,
            can_edit_group=False
        )
    ],
    extras=Extras2(
        type_filters=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ]
    ),
    total_rows_groups=76,
    load_more_groups='load_more_groups6'
)
```

