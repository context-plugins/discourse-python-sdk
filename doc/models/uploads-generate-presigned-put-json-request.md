
# Uploads Generate Presigned Put Json Request

## Structure

`UploadsGeneratePresignedPutJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type`](../../doc/models/type.md) | Required | - |
| `file_name` | `str` | Required | - |
| `file_size` | `int` | Required | File size should be represented in bytes. |
| `metadata` | [`Metadata`](../../doc/models/metadata.md) | Optional | - |

## Example

```python
from discourseapidocumentation.models.metadata import Metadata
from discourseapidocumentation.models.mtype import Type
from discourseapidocumentation.models.uploads_generate_presigned_put_json_request import UploadsGeneratePresignedPutJsonRequest

uploads_generate_presigned_put_json_request = UploadsGeneratePresignedPutJsonRequest(
    mtype=Type.CUSTOM_EMOJI,
    file_name='IMG_2021.jpeg',
    file_size=4096,
    metadata=Metadata(
        sha_1_checksum='sha1-checksum2'
    )
)
```

