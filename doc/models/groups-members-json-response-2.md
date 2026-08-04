
# Groups Members Json Response 2

## Structure

`GroupsMembersJsonResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `str` | Required | - |
| `usernames` | `List[Any]` | Required | - |
| `skipped_usernames` | `List[Any]` | Required | - |

## Example

```python
import jsonpickle

from discourse.models.groups_members_json_response_2 import GroupsMembersJsonResponse2

groups_members_json_response_2 = GroupsMembersJsonResponse2(
    success='success2',
    usernames=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    skipped_usernames=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ]
)
```

