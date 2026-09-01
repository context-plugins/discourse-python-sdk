from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Order2(str, Enum):
    LIKES_RECEIVED = "likes_received"
    LIKES_GIVEN = "likes_given"
    TOPIC_COUNT = "topic_count"
    POST_COUNT = "post_count"
    TOPICS_ENTERED = "topics_entered"
    POSTS_READ = "posts_read"
    DAYS_VISITED = "days_visited"

    __str__ = str.__str__


Order2OrStr: TypeAlias = Annotated[Order2 | str, open_enum_validator(Order2)]
