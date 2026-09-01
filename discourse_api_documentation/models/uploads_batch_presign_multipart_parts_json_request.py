from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UploadsBatchPresignMultipartPartsJsonRequest(SdkBaseModel):
    part_numbers: list[Any]
    """The part numbers to generate the presigned URLs for, must be between 1 and 10000."""

    unique_identifier: str
    """The unique identifier returned in the original /create-multipart request."""


class UploadsBatchPresignMultipartPartsJsonRequestDict(TypedDict):
    part_numbers: list[Any]
    unique_identifier: str
