from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type import TypeOrStr
from .metadata import Metadata, MetadataDict


class UploadsGeneratePresignedPutJsonRequest(SdkBaseModel):
    type_: TypeOrStr = Field(alias="type")
    file_name: str
    file_size: int
    """File size should be represented in bytes."""

    metadata: Optional[Metadata] = UNSET


class UploadsGeneratePresignedPutJsonRequestDict(TypedDict):
    type_: TypeOrStr
    file_name: str
    file_size: int
    metadata: NotRequired[Metadata | MetadataDict]
