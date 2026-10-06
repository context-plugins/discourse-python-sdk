from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .extra import Extra, ExtraDict


class GroupedSearchResult(SdkBaseModel):
    more_posts: str | None
    more_users: str | None
    more_categories: str | None
    term: str
    search_log_id: int
    more_full_page_results: str | None
    can_create_topic: bool
    error: str | None
    extra: Optional[Extra] = UNSET
    post_ids: list[Any]
    user_ids: list[Any]
    category_ids: list[Any]
    tag_ids: list[Any]
    group_ids: list[Any]


class GroupedSearchResultDict(TypedDict):
    more_posts: str | None
    more_users: str | None
    more_categories: str | None
    term: str
    search_log_id: int
    more_full_page_results: str | None
    can_create_topic: bool
    error: str | None
    extra: NotRequired[ExtraDict]
    post_ids: list[Any]
    user_ids: list[Any]
    category_ids: list[Any]
    tag_ids: list[Any]
    group_ids: list[Any]
