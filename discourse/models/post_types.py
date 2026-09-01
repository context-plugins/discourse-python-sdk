from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PostTypes(SdkBaseModel):
    regular: int
    moderator_action: int
    small_action: int
    whisper: int


class PostTypesDict(TypedDict):
    regular: int
    moderator_action: int
    small_action: int
    whisper: int
