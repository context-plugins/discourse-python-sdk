from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NotificationLevel(str, Enum):
    _0 = "0"
    _1 = "1"
    _2 = "2"
    _3 = "3"

    __str__ = str.__str__


NotificationLevelOrStr: TypeAlias = Annotated[NotificationLevel | str, open_enum_validator(NotificationLevel)]
