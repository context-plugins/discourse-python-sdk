from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .optimized_video import OptimizedVideo, OptimizedVideoDict
from .thumbnail import Thumbnail, ThumbnailDict


class UploadsCompleteExternalUploadJsonResponse(SdkBaseModel):
    id: int
    url: str
    original_filename: str
    filesize: int
    width: int
    height: int
    thumbnail_width: int
    thumbnail_height: int
    extension: str
    short_url: str
    short_path: str
    retain_hours: str | None
    human_filesize: str
    dominant_color: OptionalNullable[str] = UNSET
    thumbnail: OptionalNullable[Thumbnail] = UNSET
    optimized_video: OptionalNullable[OptimizedVideo] = UNSET


class UploadsCompleteExternalUploadJsonResponseDict(TypedDict):
    id: int
    url: str
    original_filename: str
    filesize: int
    width: int
    height: int
    thumbnail_width: int
    thumbnail_height: int
    extension: str
    short_url: str
    short_path: str
    retain_hours: str | None
    human_filesize: str
    dominant_color: NotRequired[str | None]
    thumbnail: NotRequired[ThumbnailDict | None]
    optimized_video: NotRequired[OptimizedVideoDict | None]
