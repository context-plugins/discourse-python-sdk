
# Metadata

## Structure

`Metadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sha_1_checksum` | `str` | Optional | The SHA1 checksum of the upload binary blob. Optionally<br>be provided and serves as an additional security check when<br>later processing the file in complete-external-upload endpoint. |

## Example

```python
from discourseapidocumentation.models.metadata import Metadata

metadata = Metadata(
    sha_1_checksum='sha1-checksum2'
)
```

