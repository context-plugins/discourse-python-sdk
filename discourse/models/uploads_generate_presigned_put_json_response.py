from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UploadsGeneratePresignedPutJsonResponse(SdkBaseModel):
    key: Optional[str] = UNSET
    """The path of the temporary file on the external storage service."""

    url: Optional[str] = UNSET
    """A presigned PUT URL which must be used to upload the file binary blob to."""

    signed_headers: Optional[Any] = UNSET
    """A map of headers that must be sent with the PUT request."""

    unique_identifier: Optional[str] = UNSET
    """A unique string that identifies the external upload. This must be stored and then sent in the
    /complete-external-upload endpoint to complete the direct upload."""


class UploadsGeneratePresignedPutJsonResponseDict(TypedDict):
    key: NotRequired[str]
    url: NotRequired[str]
    signed_headers: NotRequired[Any]
    unique_identifier: NotRequired[str]
