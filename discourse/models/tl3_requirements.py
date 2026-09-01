from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .penalty_counts1 import PenaltyCounts1, PenaltyCounts1Dict


class Tl3Requirements(SdkBaseModel):
    time_period: int
    requirements_met: bool
    requirements_lost: bool
    trust_level_locked: bool
    on_grace_period: bool
    days_visited: int
    min_days_visited: int
    num_topics_replied_to: int
    min_topics_replied_to: int
    topics_viewed: int
    min_topics_viewed: int
    posts_read: int
    min_posts_read: int
    topics_viewed_all_time: int
    min_topics_viewed_all_time: int
    posts_read_all_time: int
    min_posts_read_all_time: int
    num_flagged_posts: int
    max_flagged_posts: int
    num_flagged_by_users: int
    max_flagged_by_users: int
    num_likes_given: int
    min_likes_given: int
    num_likes_received: int
    min_likes_received: int
    num_likes_received_days: int
    min_likes_received_days: int
    num_likes_received_users: int
    min_likes_received_users: int
    penalty_counts: PenaltyCounts1


class Tl3RequirementsDict(TypedDict):
    time_period: int
    requirements_met: bool
    requirements_lost: bool
    trust_level_locked: bool
    on_grace_period: bool
    days_visited: int
    min_days_visited: int
    num_topics_replied_to: int
    min_topics_replied_to: int
    topics_viewed: int
    min_topics_viewed: int
    posts_read: int
    min_posts_read: int
    topics_viewed_all_time: int
    min_topics_viewed_all_time: int
    posts_read_all_time: int
    min_posts_read_all_time: int
    num_flagged_posts: int
    max_flagged_posts: int
    num_flagged_by_users: int
    max_flagged_by_users: int
    num_likes_given: int
    min_likes_given: int
    num_likes_received: int
    min_likes_received: int
    num_likes_received_days: int
    min_likes_received_days: int
    num_likes_received_users: int
    min_likes_received_users: int
    penalty_counts: PenaltyCounts1 | PenaltyCounts1Dict
