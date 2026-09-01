from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UploadsAbortMultipartJsonRequest(SdkBaseModel):
    external_upload_identifier: str
    """The identifier of the multipart upload in the external storage provider. This is the multipart upload_id in AWS
    S3."""


class UploadsAbortMultipartJsonRequestDict(TypedDict):
    external_upload_identifier: str
