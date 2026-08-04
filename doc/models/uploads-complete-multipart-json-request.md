
# Uploads Complete Multipart Json Request

## Structure

`UploadsCompleteMultipartJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `unique_identifier` | `str` | Required | The unique identifier returned in the original /create-multipart<br>request. |
| `parts` | `List[Any]` | Required | All of the part numbers and their corresponding ETags<br>that have been uploaded must be provided. |

## Example

```python
import jsonpickle

from discourse.models.uploads_complete_multipart_json_request import UploadsCompleteMultipartJsonRequest

uploads_complete_multipart_json_request = UploadsCompleteMultipartJsonRequest(
    unique_identifier='66e86218-80d9-4bda-b4d5-2b6def968705',
    parts=[
        jsonpickle.decode('{"part_number":1,"etag":"0c376dcfcc2606f4335bbc732de93344"}'),
        jsonpickle.decode('{"part_number":2,"etag":"09ert8cfcc2606f4335bbc732de91122"}')
    ]
)
```

