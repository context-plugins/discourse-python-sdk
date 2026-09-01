from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UJsonRequest(SdkBaseModel):
    name: Optional[str] = UNSET
    external_ids: Optional[Any] = UNSET


class UJsonRequestDict(TypedDict):
    name: NotRequired[str]
    external_ids: NotRequired[Any]
