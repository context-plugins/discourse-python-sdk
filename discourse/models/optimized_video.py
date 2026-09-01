from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OptimizedVideo(SdkBaseModel):
    id: Optional[int] = UNSET
    upload_id: Optional[int] = UNSET
    url: Optional[str] = UNSET
    extension: Optional[str] = UNSET
    filesize: Optional[int] = UNSET
    sha1: Optional[str] = UNSET
    original_filename: Optional[str] = UNSET


class OptimizedVideoDict(TypedDict):
    id: NotRequired[int]
    upload_id: NotRequired[int]
    url: NotRequired[str]
    extension: NotRequired[str]
    filesize: NotRequired[int]
    sha1: NotRequired[str]
    original_filename: NotRequired[str]
