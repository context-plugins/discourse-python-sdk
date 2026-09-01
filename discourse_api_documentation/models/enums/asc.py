from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Asc(str, Enum):
    TRUE = "true"

    __str__ = str.__str__


AscOrStr: TypeAlias = Annotated[Asc | str, open_enum_validator(Asc)]
