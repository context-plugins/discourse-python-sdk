
# Admin Groups Json Response

## Structure

`AdminGroupsJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `basic_group` | [`BasicGroup`](../../doc/models/basic-group.md) | Required | - |

## Example

```python
from discourse.models.admin_groups_json_response import AdminGroupsJsonResponse
from discourse.models.basic_group import BasicGroup

admin_groups_json_response = AdminGroupsJsonResponse(
    basic_group=BasicGroup(
        id=132,
        automatic=False,
        name='name8',
        user_count=28,
        mentionable_level=216,
        messageable_level=72,
        visibility_level=80,
        primary_group=False,
        title='title6',
        grant_trust_level='grant_trust_level0',
        incoming_email='incoming_email2',
        has_messages=False,
        flair_url='flair_url8',
        flair_bg_color='flair_bg_color2',
        flair_color='flair_color2',
        bio_raw='bio_raw0',
        bio_cooked='bio_cooked6',
        bio_excerpt='bio_excerpt2',
        public_admission=False,
        public_exit=False,
        allow_membership_requests=False,
        full_name='full_name4',
        default_notification_level=92,
        membership_request_template='membership_request_template6',
        members_visibility_level=236,
        can_see_members=False,
        can_admin_group=False,
        publish_read_state=False,
        can_edit_group=False
    )
)
```

