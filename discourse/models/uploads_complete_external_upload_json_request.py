from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UploadsCompleteExternalUploadJsonRequest(SdkBaseModel):
    unique_identifier: str
    """The unique identifier returned in the original /generate-presigned-put request."""

    for_private_message: Optional[str] = UNSET
    """Optionally set this to true if the upload is for a private message."""

    for_site_setting: Optional[str] = UNSET
    """Optionally set this to true if the upload is for a site setting."""

    pasted: Optional[str] = UNSET
    """Optionally set this to true if the upload was pasted into the upload area. This will convert PNG files to
    JPEG."""


class UploadsCompleteExternalUploadJsonRequestDict(TypedDict):
    unique_identifier: str
    for_private_message: NotRequired[str]
    for_site_setting: NotRequired[str]
    pasted: NotRequired[str]
