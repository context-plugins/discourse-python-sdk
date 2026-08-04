
# Groups Json Request

## Structure

`GroupsJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `group` | [`Group`](../../doc/models/group.md) | Required | - |

## Example

```python
from discourse.models.group import Group
from discourse.models.groups_json_request import GroupsJsonRequest

groups_json_request = GroupsJsonRequest(
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

