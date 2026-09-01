from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type1 import Type1OrStr


class UPreferencesAvatarPickJsonRequest(SdkBaseModel):
    upload_id: int
    type_: Type1OrStr = Field(alias="type")


class UPreferencesAvatarPickJsonRequestDict(TypedDict):
    upload_id: int
    type_: Type1OrStr
