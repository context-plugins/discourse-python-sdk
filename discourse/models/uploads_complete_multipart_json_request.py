from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UploadsCompleteMultipartJsonRequest(SdkBaseModel):
    unique_identifier: str
    """The unique identifier returned in the original /create-multipart request."""

    parts: list[Any]
    """All of the part numbers and their corresponding ETags that have been uploaded must be provided."""


class UploadsCompleteMultipartJsonRequestDict(TypedDict):
    unique_identifier: str
    parts: list[Any]
