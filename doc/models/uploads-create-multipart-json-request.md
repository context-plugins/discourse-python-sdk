
# Uploads Create Multipart Json Request

## Structure

`UploadsCreateMultipartJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `upload_type` | [`UploadType1`](../../doc/models/upload-type-1.md) | Required | - |
| `file_name` | `str` | Required | - |
| `file_size` | `int` | Required | File size should be represented in bytes. |
| `metadata` | [`Metadata`](../../doc/models/metadata.md) | Optional | - |

## Example

```python
from discourseapidocumentation.models.metadata import Metadata
from discourseapidocumentation.models.upload_type_1 import UploadType1
from discourseapidocumentation.models.uploads_create_multipart_json_request import UploadsCreateMultipartJsonRequest

uploads_create_multipart_json_request = UploadsCreateMultipartJsonRequest(
    upload_type=UploadType1.AVATAR,
    file_name='IMG_2021.jpeg',
    file_size=4096,
    metadata=Metadata(
        sha_1_checksum='sha1-checksum2'
    )
)
```

