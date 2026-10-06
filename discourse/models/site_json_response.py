from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .access_control import AccessControl, AccessControlDict
from .archetype import Archetype, ArchetypeDict
from .category4 import Category4, Category4Dict
from .category_type import CategoryType, CategoryTypeDict
from .group5 import Group5, Group5Dict
from .notification_types import NotificationTypes, NotificationTypesDict
from .post_action_type import PostActionType, PostActionTypeDict
from .post_types import PostTypes, PostTypesDict
from .top_tag import TopTag, TopTagDict
from .topic_flag_type import TopicFlagType, TopicFlagTypeDict
from .trust_levels import TrustLevels, TrustLevelsDict
from .user_color_scheme import UserColorScheme, UserColorSchemeDict
from .user_theme import UserTheme, UserThemeDict
from .user_tips import UserTips, UserTipsDict


class SiteJsonResponse(SdkBaseModel):
    default_archetype: str
    notification_types: NotificationTypes
    post_types: PostTypes
    trust_levels: TrustLevels
    user_tips: Optional[UserTips] = UNSET
    groups: list[Group5]
    filters: list[Any]
    homepage_choices: list[Any]
    periods: list[Any]
    top_menu_items: list[Any]
    anonymous_top_menu_items: list[Any]
    uncategorized_category_id: int
    user_field_max_length: int
    post_action_types: list[PostActionType]
    topic_flag_types: list[TopicFlagType]
    can_create_tag: bool
    can_tag_topics: bool
    can_tag_pms: bool
    tags_filter_regexp: str
    top_tags: list[TopTag]
    wizard_required: Optional[bool] = UNSET
    can_associate_groups: Optional[bool] = UNSET
    email_configured: bool
    upcoming_changes_with_css: Optional[list[str]] = UNSET
    topic_featured_link_allowed_category_ids: list[Any]
    user_themes: list[UserTheme]
    user_color_schemes: list[UserColorScheme]
    default_light_color_scheme: Any | None
    default_dark_color_scheme: Any | None
    censored_regexp: list[Any]
    custom_emoji_translation: Any
    watched_words_replace: Any | None
    watched_words_link: Any | None
    markdown_additional_options: Optional[Any] = UNSET
    hashtag_configurations: Optional[Any] = UNSET
    hashtag_icons: Optional[Any] = UNSET
    displayed_about_plugin_stat_groups: Optional[list[Any]] = UNSET
    categories: list[Category4]
    archetypes: list[Archetype]
    user_fields: list[Any]
    auth_providers: list[Any]
    whispers_allowed_groups_names: Optional[list[Any]] = UNSET
    denied_emojis: Optional[list[Any]] = UNSET
    valid_flag_applies_to_types: Optional[list[Any]] = UNSET
    navigation_menu_site_top_tags: Optional[list[Any]] = UNSET
    full_name_required_for_signup: bool
    full_name_visible_in_signup: bool
    admin_config_login_routes: Optional[list[Any]] = UNSET
    access_control: Optional[AccessControl] = UNSET
    permanent_upcoming_change_names: Optional[list[str]] = UNSET
    category_types: Optional[list[CategoryType]] = UNSET


class SiteJsonResponseDict(TypedDict):
    default_archetype: str
    notification_types: NotificationTypesDict
    post_types: PostTypesDict
    trust_levels: TrustLevelsDict
    user_tips: NotRequired[UserTipsDict]
    groups: list[Group5Dict]
    filters: list[Any]
    homepage_choices: list[Any]
    periods: list[Any]
    top_menu_items: list[Any]
    anonymous_top_menu_items: list[Any]
    uncategorized_category_id: int
    user_field_max_length: int
    post_action_types: list[PostActionTypeDict]
    topic_flag_types: list[TopicFlagTypeDict]
    can_create_tag: bool
    can_tag_topics: bool
    can_tag_pms: bool
    tags_filter_regexp: str
    top_tags: list[TopTagDict]
    wizard_required: NotRequired[bool]
    can_associate_groups: NotRequired[bool]
    email_configured: bool
    upcoming_changes_with_css: NotRequired[list[str]]
    topic_featured_link_allowed_category_ids: list[Any]
    user_themes: list[UserThemeDict]
    user_color_schemes: list[UserColorSchemeDict]
    default_light_color_scheme: Any | None
    default_dark_color_scheme: Any | None
    censored_regexp: list[Any]
    custom_emoji_translation: Any
    watched_words_replace: Any | None
    watched_words_link: Any | None
    markdown_additional_options: NotRequired[Any]
    hashtag_configurations: NotRequired[Any]
    hashtag_icons: NotRequired[Any]
    displayed_about_plugin_stat_groups: NotRequired[list[Any]]
    categories: list[Category4Dict]
    archetypes: list[ArchetypeDict]
    user_fields: list[Any]
    auth_providers: list[Any]
    whispers_allowed_groups_names: NotRequired[list[Any]]
    denied_emojis: NotRequired[list[Any]]
    valid_flag_applies_to_types: NotRequired[list[Any]]
    navigation_menu_site_top_tags: NotRequired[list[Any]]
    full_name_required_for_signup: bool
    full_name_visible_in_signup: bool
    admin_config_login_routes: NotRequired[list[Any]]
    access_control: NotRequired[AccessControlDict]
    permanent_upcoming_change_names: NotRequired[list[str]]
    category_types: NotRequired[list[CategoryTypeDict]]
