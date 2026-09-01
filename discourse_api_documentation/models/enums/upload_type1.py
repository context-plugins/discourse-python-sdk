from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class UploadType1(str, Enum):
    AVATAR = "avatar"
    PROFILE_BACKGROUND = "profile_background"
    CARD_BACKGROUND = "card_background"
    CUSTOM_EMOJI = "custom_emoji"
    COMPOSER = "composer"

    __str__ = str.__str__


UploadType1OrStr: TypeAlias = Annotated[UploadType1 | str, open_enum_validator(UploadType1)]
