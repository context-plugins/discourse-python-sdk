from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .category_localization import CategoryLocalization, CategoryLocalizationDict
from .permissions import Permissions, PermissionsDict


class CategoriesJsonRequest1(SdkBaseModel):
    name: str
    color: Optional[str] = UNSET
    text_color: Optional[str] = UNSET
    style_type: Optional[str] = UNSET
    emoji: Optional[str] = UNSET
    icon: Optional[str] = UNSET
    parent_category_id: Optional[int] = UNSET
    allow_badges: Optional[bool] = UNSET
    slug: Optional[str] = UNSET
    topic_featured_links_allowed: Optional[bool] = UNSET
    permissions: Optional[Permissions] = UNSET
    search_priority: Optional[int] = UNSET
    form_template_ids: Optional[list[Any]] = UNSET
    category_localizations: Optional[list[CategoryLocalization]] = UNSET


class CategoriesJsonRequest1Dict(TypedDict):
    name: str
    color: NotRequired[str]
    text_color: NotRequired[str]
    style_type: NotRequired[str]
    emoji: NotRequired[str]
    icon: NotRequired[str]
    parent_category_id: NotRequired[int]
    allow_badges: NotRequired[bool]
    slug: NotRequired[str]
    topic_featured_links_allowed: NotRequired[bool]
    permissions: NotRequired[PermissionsDict]
    search_priority: NotRequired[int]
    form_template_ids: NotRequired[list[Any]]
    category_localizations: NotRequired[list[CategoryLocalizationDict]]
