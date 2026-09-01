from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Category1(SdkBaseModel):
    id: int
    name: str
    color: str
    text_color: str
    style_type: str
    emoji: str | None
    icon: str | None
    slug: str
    topic_count: int
    post_count: int
    position: int
    description: str | None
    description_text: str | None
    description_excerpt: str | None
    topic_url: str | None
    read_restricted: bool
    permission: int
    notification_level: int
    can_edit: bool
    topic_template: str | None
    topic_title_placeholder: str | None
    has_children: bool
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
    topics_day: int
    topics_week: int
    topics_month: int
    topics_year: int
    topics_all_time: int
    is_uncategorized: Optional[bool] = UNSET
    subcategory_ids: list[Any]
    subcategory_list: Optional[list[Any | None]] = UNSET
    uploaded_logo: str | None
    uploaded_logo_dark: str | None
    uploaded_background: str | None
    uploaded_background_dark: str | None


class Category1Dict(TypedDict):
    id: int
    name: str
    color: str
    text_color: str
    style_type: str
    emoji: str | None
    icon: str | None
    slug: str
    topic_count: int
    post_count: int
    position: int
    description: str | None
    description_text: str | None
    description_excerpt: str | None
    topic_url: str | None
    read_restricted: bool
    permission: int
    notification_level: int
    can_edit: bool
    topic_template: str | None
    topic_title_placeholder: str | None
    has_children: bool
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
    topics_day: int
    topics_week: int
    topics_month: int
    topics_year: int
    topics_all_time: int
    is_uncategorized: NotRequired[bool]
    subcategory_ids: list[Any]
    subcategory_list: NotRequired[list[Any | None]]
    uploaded_logo: str | None
    uploaded_logo_dark: str | None
    uploaded_background: str | None
    uploaded_background_dark: str | None
