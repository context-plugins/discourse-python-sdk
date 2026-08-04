
# U Emails Json Response

## Structure

`UEmailsJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Required | - |
| `secondary_emails` | `List[Any]` | Required | - |
| `unconfirmed_emails` | `List[Any]` | Required | - |
| `associated_accounts` | `List[Any]` | Required | - |

## Example

```python
import jsonpickle

from discourse.models.u_emails_json_response import UEmailsJsonResponse

u_emails_json_response = UEmailsJsonResponse(
    email='email2',
    secondary_emails=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    unconfirmed_emails=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    associated_accounts=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ]
)
```

