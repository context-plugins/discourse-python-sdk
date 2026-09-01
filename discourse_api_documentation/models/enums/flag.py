from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Flag(str, Enum):
    ACTIVE = "active"
    NEW = "new"
    STAFF = "staff"
    SUSPENDED = "suspended"
    BLOCKED = "blocked"
    SUSPECT = "suspect"

    __str__ = str.__str__


FlagOrStr: TypeAlias = Annotated[Flag | str, open_enum_validator(Flag)]
