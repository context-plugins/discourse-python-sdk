
# Uploads Abort Multipart Json Request

## Structure

`UploadsAbortMultipartJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `external_upload_identifier` | `str` | Required | The identifier of the multipart upload in the external<br>storage provider. This is the multipart upload_id in AWS S3. |

## Example

```python
from discourse.models.uploads_abort_multipart_json_request import UploadsAbortMultipartJsonRequest

uploads_abort_multipart_json_request = UploadsAbortMultipartJsonRequest(
    external_upload_identifier='84x83tmxy398t3y._Q_z8CoJYVr69bE6D7f8J6Oo0434QquLFoYdGVerWFx9X5HDEI_TP_95c34n853495x35345394.d.ghQ'
)
```

