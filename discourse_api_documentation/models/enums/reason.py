from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Reason(str, Enum):
    ENABLED_FOR_EVERYONE = "enabled_for_everyone"
    ENABLED_FOR_NO_ONE = "enabled_for_no_one"
    IN_SPECIFIC_GROUPS = "in_specific_groups"
    NOT_IN_SPECIFIC_GROUPS = "not_in_specific_groups"

    __str__ = str.__str__


ReasonOrStr: TypeAlias = Annotated[Reason | str, open_enum_validator(Reason)]
