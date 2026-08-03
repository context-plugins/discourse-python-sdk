
# Admin Groups Json Request

## Structure

`AdminGroupsJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `group` | [`Group`](../../doc/models/group.md) | Required | - |

## Example

```python
from discourseapidocumentation.models.admin_groups_json_request import AdminGroupsJsonRequest
from discourseapidocumentation.models.group import Group

admin_groups_json_request = AdminGroupsJsonRequest(
    group=Group(
        name='name8',
        full_name='full_name4',
        bio_raw='bio_raw0',
        usernames='usernames0',
        owner_usernames='owner_usernames8',
        automatic_membership_email_domains='automatic_membership_email_domains2'
    )
)
```

