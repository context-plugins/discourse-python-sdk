from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type(str, Enum):
    AVATAR = "avatar"
    PROFILE_BACKGROUND = "profile_background"
    CARD_BACKGROUND = "card_background"
    CUSTOM_EMOJI = "custom_emoji"
    COMPOSER = "composer"

    __str__ = str.__str__


TypeOrStr: TypeAlias = Annotated[Type | str, open_enum_validator(Type)]
