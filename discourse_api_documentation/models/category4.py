from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .required_tag_group import RequiredTagGroup, RequiredTagGroupDict


class Category4(SdkBaseModel):
    id: int
    name: str
    color: str
    text_color: str
    style_type: Optional[str] = UNSET
    emoji: OptionalNullable[str] = UNSET
    icon: OptionalNullable[str] = UNSET
    slug: str
    topic_count: int
    post_count: int
    position: int
    description: OptionalNullable[str] = UNSET
    description_text: OptionalNullable[str] = UNSET
    description_excerpt: OptionalNullable[str] = UNSET
    topic_url: str
    read_restricted: bool
    permission: int | None
    notification_level: int
    topic_template: str | None
    topic_title_placeholder: str | None
    has_children: bool
    subcategory_count: int | None
    sort_order: str | None
    sort_ascending: bool | None
    show_subcategory_list: bool
    num_featured_topics: int
    default_view: str | None
    subcategory_list_style: str
    default_top_period: str
    default_list_filter: str
    minimum_required_tags: int
    navigate_to_first_post_after_read: bool
    allowed_tags: Optional[list[Any]] = UNSET
    allowed_tag_groups: Optional[list[Any]] = UNSET
    allow_global_tags: bool
    required_tag_groups: list[RequiredTagGroup]
    read_only_banner: str | None
    uploaded_logo: str | None
    uploaded_logo_dark: str | None
    uploaded_background: str | None
    uploaded_background_dark: str | None
    can_edit: bool
    custom_fields: OptionalNullable[Any] = UNSET
    parent_category_id: Optional[int] = UNSET
    form_template_ids: Optional[list[Any]] = UNSET
    category_types: Optional[Any] = UNSET


class Category4Dict(TypedDict):
    id: int
    name: str
    color: str
    text_color: str
    style_type: NotRequired[str]
    emoji: NotRequired[str | None]
    icon: NotRequired[str | None]
    slug: str
    topic_count: int
    post_count: int
    position: int
    description: NotRequired[str | None]
    description_text: NotRequired[str | None]
    description_excerpt: NotRequired[str | None]
    topic_url: str
    read_restricted: bool
    permission: int | None
    notification_level: int
    topic_template: str | None
    topic_title_placeholder: str | None
    has_children: bool
    subcategory_count: int | None
    sort_order: str | None
    sort_ascending: bool | None
    show_subcategory_list: bool
    num_featured_topics: int
    default_view: str | None
    subcategory_list_style: str
    default_top_period: str
    default_list_filter: str
    minimum_required_tags: int
    navigate_to_first_post_after_read: bool
    allowed_tags: NotRequired[list[Any]]
    allowed_tag_groups: NotRequired[list[Any]]
    allow_global_tags: bool
    required_tag_groups: list[RequiredTagGroup | RequiredTagGroupDict]
    read_only_banner: str | None
    uploaded_logo: str | None
    uploaded_logo_dark: str | None
    uploaded_background: str | None
    uploaded_background_dark: str | None
    can_edit: bool
    custom_fields: NotRequired[Any | None]
    parent_category_id: NotRequired[int]
    form_template_ids: NotRequired[list[Any]]
    category_types: NotRequired[Any]
