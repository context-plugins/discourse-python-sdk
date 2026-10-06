from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .grouped_search_result import GroupedSearchResult, GroupedSearchResultDict
from .tag_model import TagModel, TagModelDict


class SearchJsonResponse(SdkBaseModel):
    posts: list[Any]
    users: list[Any]
    categories: list[Any]
    tags: list[TagModel]
    groups: list[Any]
    grouped_search_result: GroupedSearchResult


class SearchJsonResponseDict(TypedDict):
    posts: list[Any]
    users: list[Any]
    categories: list[Any]
    tags: list[TagModelDict]
    groups: list[Any]
    grouped_search_result: GroupedSearchResultDict
