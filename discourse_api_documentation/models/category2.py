from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .available_category_type import AvailableCategoryType, AvailableCategoryTypeDict
from .category_setting import CategorySetting, CategorySettingDict
from .group_permission import GroupPermission, GroupPermissionDict
from .required_tag_group import RequiredTagGroup, RequiredTagGroupDict


class Category2(SdkBaseModel):
    id: int
    name: str
    color: str
    text_color: str
    style_type: Optional[str] = UNSET
    emoji: OptionalNullable[str] = UNSET
    icon: OptionalNullable[str] = UNSET
    slug: str
    locale: OptionalNullable[str] = UNSET
    topic_count: int
    post_count: int
    position: int
    description: str | None
    description_text: str | None
    description_excerpt: str | None
    topic_url: str | None
    read_restricted: bool
    permission: int | None
    notification_level: int
    can_edit: bool
    topic_template: str | None
    topic_title_placeholder: str | None
    form_template_ids: list[Any]
    has_children: bool | None
    subcategory_count: int | None
    sort_order: str | None
    sort_ascending: str | None
    show_subcategory_list: bool
    num_featured_topics: int
    default_view: str | None
    subcategory_list_style: str
    default_top_period: str
    default_list_filter: str
    minimum_required_tags: int
    navigate_to_first_post_after_read: bool
    custom_fields: Any
    allowed_tags: Optional[list[Any]] = UNSET
    allowed_tag_groups: Optional[list[Any]] = UNSET
    allow_global_tags: Optional[bool] = UNSET
    required_tag_groups: list[RequiredTagGroup]
    category_setting: Optional[CategorySetting] = UNSET
    category_localizations: Optional[list[Any]] = UNSET
    read_only_banner: str | None
    available_groups: list[Any]
    auto_close_hours: str | None
    auto_close_based_on_last_post: bool
    allow_unlimited_owner_edits_on_first_post: bool
    default_slow_mode_seconds: str | None
    group_permissions: list[GroupPermission]
    email_in: str | None
    email_in_allow_strangers: bool
    mailinglist_mirror: bool
    all_topics_wiki: bool
    can_delete: bool
    allow_badges: bool
    topic_featured_link_allowed: bool
    search_priority: int
    topic_posting_review_group_ids: list[int]
    reply_posting_review_group_ids: list[int]
    uploaded_logo: str | None
    uploaded_logo_dark: str | None
    uploaded_background: str | None
    uploaded_background_dark: str | None
    category_types: Optional[Any] = UNSET
    category_type_settings: Optional[Any] = UNSET
    available_category_types: Optional[list[AvailableCategoryType]] = UNSET


class Category2Dict(TypedDict):
    id: int
    name: str
    color: str
    text_color: str
    style_type: NotRequired[str]
    emoji: NotRequired[str | None]
    icon: NotRequired[str | None]
    slug: str
    locale: NotRequired[str | None]
    topic_count: int
    post_count: int
    position: int
    description: str | None
    description_text: str | None
    description_excerpt: str | None
    topic_url: str | None
    read_restricted: bool
    permission: int | None
    notification_level: int
    can_edit: bool
    topic_template: str | None
    topic_title_placeholder: str | None
    form_template_ids: list[Any]
    has_children: bool | None
    subcategory_count: int | None
    sort_order: str | None
    sort_ascending: str | None
    show_subcategory_list: bool
    num_featured_topics: int
    default_view: str | None
    subcategory_list_style: str
    default_top_period: str
    default_list_filter: str
    minimum_required_tags: int
    navigate_to_first_post_after_read: bool
    custom_fields: Any
    allowed_tags: NotRequired[list[Any]]
    allowed_tag_groups: NotRequired[list[Any]]
    allow_global_tags: NotRequired[bool]
    required_tag_groups: list[RequiredTagGroup | RequiredTagGroupDict]
    category_setting: NotRequired[CategorySetting | CategorySettingDict]
    category_localizations: NotRequired[list[Any]]
    read_only_banner: str | None
    available_groups: list[Any]
    auto_close_hours: str | None
    auto_close_based_on_last_post: bool
    allow_unlimited_owner_edits_on_first_post: bool
    default_slow_mode_seconds: str | None
    group_permissions: list[GroupPermission | GroupPermissionDict]
    email_in: str | None
    email_in_allow_strangers: bool
    mailinglist_mirror: bool
    all_topics_wiki: bool
    can_delete: bool
    allow_badges: bool
    topic_featured_link_allowed: bool
    search_priority: int
    topic_posting_review_group_ids: list[int]
    reply_posting_review_group_ids: list[int]
    uploaded_logo: str | None
    uploaded_logo_dark: str | None
    uploaded_background: str | None
    uploaded_background_dark: str | None
    category_types: NotRequired[Any]
    category_type_settings: NotRequired[Any]
    available_category_types: NotRequired[list[AvailableCategoryType | AvailableCategoryTypeDict]]
