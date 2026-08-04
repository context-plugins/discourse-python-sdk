
# Uploads Json Response

## Structure

`UploadsJsonResponse`

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
from discourse.models.optimized_video import OptimizedVideo
from discourse.models.thumbnail import Thumbnail
from discourse.models.uploads_json_response import UploadsJsonResponse

uploads_json_response = UploadsJsonResponse(
    id=162,
    url='url4',
    original_filename='original_filename8',
    filesize=172,
    width=250,
    height=154,
    thumbnail_width=148,
    thumbnail_height=236,
    extension='extension6',
    short_url='short_url2',
    short_path='short_path4',
    retain_hours='retain_hours6',
    human_filesize='human_filesize4',
    dominant_color='dominant_color4',
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

