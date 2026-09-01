from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Enabled(str, Enum):
    TRUE = "true"
    FALSE = "false"

    __str__ = str.__str__


EnabledOrStr: TypeAlias = Annotated[Enabled | str, open_enum_validator(Enabled)]
