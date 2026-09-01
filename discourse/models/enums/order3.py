from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Order3(str, Enum):
    CREATED = "created"
    LAST_EMAILED = "last_emailed"
    SEEN = "seen"
    USERNAME = "username"
    EMAIL = "email"
    TRUST_LEVEL = "trust_level"
    DAYS_VISITED = "days_visited"
    POSTS_READ = "posts_read"
    TOPICS_VIEWED = "topics_viewed"
    POSTS = "posts"
    READ_TIME = "read_time"

    __str__ = str.__str__


Order3OrStr: TypeAlias = Annotated[Order3 | str, open_enum_validator(Order3)]
