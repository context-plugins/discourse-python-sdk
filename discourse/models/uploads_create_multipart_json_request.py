from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.upload_type1 import UploadType1OrStr
from .metadata import Metadata, MetadataDict


class UploadsCreateMultipartJsonRequest(SdkBaseModel):
    upload_type: UploadType1OrStr
    file_name: str
    file_size: int
    """File size should be represented in bytes."""

    metadata: Optional[Metadata] = UNSET


class UploadsCreateMultipartJsonRequestDict(TypedDict):
    upload_type: UploadType1OrStr
    file_name: str
    file_size: int
    metadata: NotRequired[MetadataDict]
