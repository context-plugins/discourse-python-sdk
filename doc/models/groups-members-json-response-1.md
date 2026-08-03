
# Groups Members Json Response 1

## Structure

`GroupsMembersJsonResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `str` | Required | - |
| `usernames` | `List[Any]` | Required | - |
| `emails` | `List[Any]` | Required | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.groups_members_json_response_1 import GroupsMembersJsonResponse1

groups_members_json_response_1 = GroupsMembersJsonResponse1(
    success='success6',
    usernames=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    emails=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ]
)
```

