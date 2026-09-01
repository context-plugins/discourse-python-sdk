from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UploadsCreateMultipartJsonResponse(SdkBaseModel):
    key: str
    """The path of the temporary file on the external storage service."""

    external_upload_identifier: str
    """The identifier of the multipart upload in the external storage provider. This is the multipart upload_id in AWS
    S3."""

    unique_identifier: str
    """A unique string that identifies the external upload. This must be stored and then sent in the /complete-multipart
    and /batch-presign-multipart-parts endpoints."""


class UploadsCreateMultipartJsonResponseDict(TypedDict):
    key: str
    external_upload_identifier: str
    unique_identifier: str
