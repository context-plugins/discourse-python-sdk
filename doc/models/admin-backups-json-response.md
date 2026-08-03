
# Admin Backups Json Response

*This model accepts additional fields of type Any.*

## Structure

`AdminBackupsJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filename` | `str` | Required | - |
| `size` | `int` | Required | - |
| `last_modified` | `str` | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.admin_backups_json_response import AdminBackupsJsonResponse

admin_backups_json_response = AdminBackupsJsonResponse(
    filename='filename0',
    size=166,
    last_modified='last_modified6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

