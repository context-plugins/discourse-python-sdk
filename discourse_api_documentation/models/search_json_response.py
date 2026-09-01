from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .grouped_search_result import GroupedSearchResult, GroupedSearchResultDict
from .tag import Tag, TagDict


class SearchJsonResponse(SdkBaseModel):
    posts: list[Any]
    users: list[Any]
    categories: list[Any]
    tags: list[Tag]
    groups: list[Any]
    grouped_search_result: GroupedSearchResult


class SearchJsonResponseDict(TypedDict):
    posts: list[Any]
    users: list[Any]
    categories: list[Any]
    tags: list[Tag | TagDict]
    groups: list[Any]
    grouped_search_result: GroupedSearchResult | GroupedSearchResultDict
