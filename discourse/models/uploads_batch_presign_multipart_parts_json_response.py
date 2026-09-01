from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UploadsBatchPresignMultipartPartsJsonResponse(SdkBaseModel):
    presigned_urls: Any
    """The presigned URLs for each part number, which has the part numbers as keys."""


class UploadsBatchPresignMultipartPartsJsonResponseDict(TypedDict):
    presigned_urls: Any
