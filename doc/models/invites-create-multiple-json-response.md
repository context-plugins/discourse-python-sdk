
# Invites Create Multiple Json Response

*This model accepts additional fields of type Any.*

## Structure

`InvitesCreateMultipleJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `num_successfully_created_invitations` | `int` | Optional | - |
| `num_failed_invitations` | `int` | Optional | - |
| `failed_invitations` | `List[Any]` | Optional | - |
| `successful_invitations` | `List[Any]` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.invites_create_multiple_json_response import InvitesCreateMultipleJsonResponse

invites_create_multiple_json_response = InvitesCreateMultipleJsonResponse(
    num_successfully_created_invitations=42,
    num_failed_invitations=42,
    failed_invitations=[],
    successful_invitations=[
        jsonpickle.decode('{"id":42,"link":"http://example.com/invites/9045fd767efe201ca60c6658bcf14158","email":"not-a-user-yet-1@example.com","emailed":true,"custom_message":"Hello world!","topics":[],"groups":[],"created_at":"2021-01-01T12:00:00.000Z","updated_at":"2021-01-01T12:00:00.000Z","expires_at":"2021-02-01T12:00:00.000Z","expired":false}'),
        jsonpickle.decode('{"id":42,"link":"http://example.com/invites/c6658bcf141589045fd767efe201ca60","email":"not-a-user-yet-2@example.com","emailed":true,"custom_message":"Hello world!","topics":[],"groups":[],"created_at":"2021-01-01T12:00:00.000Z","updated_at":"2021-01-01T12:00:00.000Z","expires_at":"2021-02-01T12:00:00.000Z","expired":false}')
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

