from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Thumbnail(SdkBaseModel):
    id: Optional[int] = UNSET
    upload_id: Optional[int] = UNSET
    url: Optional[str] = UNSET
    extension: Optional[str] = UNSET
    width: Optional[int] = UNSET
    height: Optional[int] = UNSET
    filesize: Optional[int] = UNSET


class ThumbnailDict(TypedDict):
    id: NotRequired[int]
    upload_id: NotRequired[int]
    url: NotRequired[str]
    extension: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    filesize: NotRequired[int]
