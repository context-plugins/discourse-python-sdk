
# Uploads Complete Multipart Json Response

## Structure

`UploadsCompleteMultipartJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `url` | `str` | Required | - |
| `original_filename` | `str` | Required | - |
| `filesize` | `int` | Required | - |
| `width` | `int` | Required | - |
| `height` | `int` | Required | - |
| `thumbnail_width` | `int` | Required | - |
| `thumbnail_height` | `int` | Required | - |
| `extension` | `str` | Required | - |
| `short_url` | `str` | Required | - |
| `short_path` | `str` | Required | - |
| `retain_hours` | `str` | Required | - |
| `human_filesize` | `str` | Required | - |
| `dominant_color` | `str` | Optional | - |
| `thumbnail` | [`Thumbnail`](../../doc/models/thumbnail.md) | Optional | - |
| `optimized_video` | [`OptimizedVideo`](../../doc/models/optimized-video.md) | Optional | - |

## Example

```python
from discourseapidocumentation.models.optimized_video import OptimizedVideo
from discourseapidocumentation.models.thumbnail import Thumbnail
from discourseapidocumentation.models.uploads_complete_multipart_json_response import UploadsCompleteMultipartJsonResponse

uploads_complete_multipart_json_response = UploadsCompleteMultipartJsonResponse(
    id=132,
    url='url0',
    original_filename='original_filename4',
    filesize=202,
    width=24,
    height=124,
    thumbnail_width=118,
    thumbnail_height=206,
    extension='extension2',
    short_url='short_url6',
    short_path='short_path8',
    retain_hours='retain_hours2',
    human_filesize='human_filesize0',
    dominant_color='dominant_color0',
    thumbnail=Thumbnail(
        id=154,
        upload_id=144,
        url='url0',
        extension='extension2',
        width=2
    ),
    optimized_video=OptimizedVideo(
        id=182,
        upload_id=116,
        url='url4',
        extension='extension6',
        filesize=152
    )
)
```

