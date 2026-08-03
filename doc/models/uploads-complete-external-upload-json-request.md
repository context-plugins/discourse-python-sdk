
# Uploads Complete External Upload Json Request

## Structure

`UploadsCompleteExternalUploadJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `unique_identifier` | `str` | Required | The unique identifier returned in the original /generate-presigned-put<br>request. |
| `for_private_message` | `str` | Optional | Optionally set this to true if the upload is for a<br>private message. |
| `for_site_setting` | `str` | Optional | Optionally set this to true if the upload is for a<br>site setting. |
| `pasted` | `str` | Optional | Optionally set this to true if the upload was pasted<br>into the upload area. This will convert PNG files to JPEG. |

## Example

```python
from discourseapidocumentation.models.uploads_complete_external_upload_json_request import UploadsCompleteExternalUploadJsonRequest

uploads_complete_external_upload_json_request = UploadsCompleteExternalUploadJsonRequest(
    unique_identifier='66e86218-80d9-4bda-b4d5-2b6def968705',
    for_private_message='true',
    for_site_setting='true',
    pasted='true'
)
```

