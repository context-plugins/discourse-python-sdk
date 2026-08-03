
# Uploads Create Multipart Json Response

## Structure

`UploadsCreateMultipartJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Required | The path of the temporary file on the external storage<br>service. |
| `external_upload_identifier` | `str` | Required | The identifier of the multipart upload in the external<br>storage provider. This is the multipart upload_id in AWS S3. |
| `unique_identifier` | `str` | Required | A unique string that identifies the external upload.<br>This must be stored and then sent in the /complete-multipart<br>and /batch-presign-multipart-parts endpoints. |

## Example

```python
from discourseapidocumentation.models.uploads_create_multipart_json_response import UploadsCreateMultipartJsonResponse

uploads_create_multipart_json_response = UploadsCreateMultipartJsonResponse(
    key='temp/site/uploads/default/12345/67890.jpg',
    external_upload_identifier='84x83tmxy398t3y._Q_z8CoJYVr69bE6D7f8J6Oo0434QquLFoYdGVerWFx9X5HDEI_TP_95c34n853495x35345394.d.ghQ',
    unique_identifier='66e86218-80d9-4bda-b4d5-2b6def968705'
)
```

