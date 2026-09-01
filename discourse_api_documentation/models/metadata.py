from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Metadata(SdkBaseModel):
    sha1_checksum: Optional[str] = Field(default=UNSET, alias="sha1-checksum")
    """The SHA1 checksum of the upload binary blob. Optionally be provided and serves as an additional security check
    when later processing the file in complete-external-upload endpoint."""


class MetadataDict(TypedDict):
    sha1_checksum: NotRequired[str]
