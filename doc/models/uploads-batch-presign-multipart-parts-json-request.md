
# Uploads Batch Presign Multipart Parts Json Request

## Structure

`UploadsBatchPresignMultipartPartsJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `part_numbers` | `List[Any]` | Required | The part numbers to generate the presigned URLs for,<br>must be between 1 and 10000. |
| `unique_identifier` | `str` | Required | The unique identifier returned in the original /create-multipart<br>request. |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.uploads_batch_presign_multipart_parts_json_request import UploadsBatchPresignMultipartPartsJsonRequest

uploads_batch_presign_multipart_parts_json_request = UploadsBatchPresignMultipartPartsJsonRequest(
    part_numbers=[
        jsonpickle.decode('1'),
        jsonpickle.decode('2'),
        jsonpickle.decode('3')
    ],
    unique_identifier='66e86218-80d9-4bda-b4d5-2b6def968705'
)
```

