
# Groups Members Json Request

## Structure

`GroupsMembersJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `usernames` | `str` | Optional | comma separated list |

## Example

```python
from discourse.models.groups_members_json_request import GroupsMembersJsonRequest

groups_members_json_request = GroupsMembersJsonRequest(
    usernames='username1,username2'
)
```

