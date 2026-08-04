
# Site Json Response

## Structure

`SiteJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `default_archetype` | `str` | Required | - |
| `notification_types` | [`NotificationTypes`](../../doc/models/notification-types.md) | Required | - |
| `post_types` | [`PostTypes`](../../doc/models/post-types.md) | Required | - |
| `trust_levels` | [`TrustLevels`](../../doc/models/trust-levels.md) | Required | - |
| `user_tips` | [`UserTips`](../../doc/models/user-tips.md) | Optional | - |
| `groups` | [`List[Group5]`](../../doc/models/group-5.md) | Required | - |
| `filters` | `List[Any]` | Required | - |
| `homepage_choices` | `List[Any]` | Required | - |
| `periods` | `List[Any]` | Required | - |
| `top_menu_items` | `List[Any]` | Required | - |
| `anonymous_top_menu_items` | `List[Any]` | Required | - |
| `uncategorized_category_id` | `int` | Required | - |
| `user_field_max_length` | `int` | Required | - |
| `post_action_types` | [`List[PostActionType]`](../../doc/models/post-action-type.md) | Required | - |
| `topic_flag_types` | [`List[TopicFlagType]`](../../doc/models/topic-flag-type.md) | Required | - |
| `can_create_tag` | `bool` | Required | - |
| `can_tag_topics` | `bool` | Required | - |
| `can_tag_pms` | `bool` | Required | - |
| `tags_filter_regexp` | `str` | Required | - |
| `top_tags` | [`List[TopTag]`](../../doc/models/top-tag.md) | Required | - |
| `wizard_required` | `bool` | Optional | - |
| `can_associate_groups` | `bool` | Optional | - |
| `email_configured` | `bool` | Required | - |
| `upcoming_changes_with_css` | `List[str]` | Optional | - |
| `topic_featured_link_allowed_category_ids` | `List[Any]` | Required | - |
| `user_themes` | [`List[UserTheme]`](../../doc/models/user-theme.md) | Required | - |
| `user_color_schemes` | [`List[UserColorScheme]`](../../doc/models/user-color-scheme.md) | Required | - |
| `default_light_color_scheme` | `Any` | Required | - |
| `default_dark_color_scheme` | `Any` | Required | - |
| `censored_regexp` | `List[Any]` | Required | - |
| `custom_emoji_translation` | `Any` | Required | - |
| `watched_words_replace` | `str` | Required | - |
| `watched_words_link` | `str` | Required | - |
| `markdown_additional_options` | `Any` | Optional | - |
| `hashtag_configurations` | `Any` | Optional | - |
| `hashtag_icons` | `Any` | Optional | - |
| `displayed_about_plugin_stat_groups` | `List[Any]` | Optional | - |
| `categories` | [`List[Category4]`](../../doc/models/category-4.md) | Required | - |
| `archetypes` | [`List[Archetype]`](../../doc/models/archetype.md) | Required | - |
| `user_fields` | `List[Any]` | Required | - |
| `auth_providers` | `List[Any]` | Required | - |
| `whispers_allowed_groups_names` | `List[Any]` | Optional | - |
| `denied_emojis` | `List[Any]` | Optional | - |
| `valid_flag_applies_to_types` | `List[Any]` | Optional | - |
| `navigation_menu_site_top_tags` | `List[Any]` | Optional | - |
| `full_name_required_for_signup` | `bool` | Required | - |
| `full_name_visible_in_signup` | `bool` | Required | - |
| `admin_config_login_routes` | `List[Any]` | Optional | - |
| `access_control` | [`AccessControl`](../../doc/models/access-control.md) | Optional | - |
| `permanent_upcoming_change_names` | `List[str]` | Optional | - |
| `category_types` | [`List[CategoryType]`](../../doc/models/category-type.md) | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.archetype import Archetype
from discourse.models.category_4 import Category4
from discourse.models.group_5 import Group5
from discourse.models.notification_types import NotificationTypes
from discourse.models.post_action_type import PostActionType
from discourse.models.post_types import PostTypes
from discourse.models.required_tag_group import RequiredTagGroup
from discourse.models.site_json_response import SiteJsonResponse
from discourse.models.top_tag import TopTag
from discourse.models.topic_flag_type import TopicFlagType
from discourse.models.trust_levels import TrustLevels
from discourse.models.user_color_scheme import UserColorScheme
from discourse.models.user_theme import UserTheme
from discourse.models.user_tips import UserTips

site_json_response = SiteJsonResponse(
    default_archetype='default_archetype8',
    notification_types=NotificationTypes(
        mentioned=10,
        replied=148,
        quoted=16,
        edited=82,
        liked=92,
        private_message=206,
        invited_to_private_message=86,
        invitee_accepted=52,
        posted=254,
        watching_category_or_tag=26,
        moved_post=192,
        linked=214,
        granted_badge=110,
        invited_to_topic=200,
        custom=104,
        group_mentioned=70,
        group_message_summary=72,
        watching_first_post=92,
        topic_reminder=128,
        liked_consolidated=110,
        linked_consolidated=94,
        post_approved=8,
        code_review_commit_approved=90,
        membership_request_accepted=54,
        membership_request_consolidated=38,
        bookmark_reminder=230,
        reaction=190,
        votes_released=170,
        event_reminder=38,
        event_invitation=142,
        chat_mention=90,
        chat_message=52,
        chat_invitation=182,
        chat_group_mention=62,
        new_features=44,
        admin_problems=196,
        chat_quoted=4,
        chat_watched_thread=54,
        upcoming_change_available=186
    ),
    post_types=PostTypes(
        regular=174,
        moderator_action=126,
        small_action=86,
        whisper=152
    ),
    trust_levels=TrustLevels(
        newuser=196,
        basic=160,
        member=18,
        regular=28,
        leader=70
    ),
    groups=[
        Group5(
            id=152,
            name='name6',
            flair_url='flair_url6',
            flair_bg_color='flair_bg_color0',
            flair_color='flair_color0',
            automatic=False,
            full_name='full_name2',
            display_name='display_name6'
        )
    ],
    filters=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    homepage_choices=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    periods=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    top_menu_items=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    anonymous_top_menu_items=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    uncategorized_category_id=56,
    user_field_max_length=228,
    post_action_types=[
        PostActionType(
            id=90,
            name_key='name_key2',
            name='name8',
            description='description8',
            short_description='short_description4',
            is_flag=False,
            require_message=False,
            enabled=False,
            applies_to=[
                jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            ],
            is_used=False,
            auto_action_type=False,
            position=120,
            system=False
        )
    ],
    topic_flag_types=[
        TopicFlagType(
            id=12,
            name_key='name_key8',
            name='name4',
            description='description4',
            short_description='short_description0',
            is_flag=False,
            require_message=False,
            enabled=False,
            applies_to=[
                jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            ],
            is_used=False,
            auto_action_type=False,
            position=42,
            system=False
        )
    ],
    can_create_tag=False,
    can_tag_topics=False,
    can_tag_pms=False,
    tags_filter_regexp='tags_filter_regexp8',
    top_tags=[
        TopTag(
            id=22,
            name='name8',
            slug='slug2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    email_configured=False,
    topic_featured_link_allowed_category_ids=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    user_themes=[
        UserTheme(
            theme_id=108,
            name='name6',
            default=False,
            color_scheme_id=124,
            dark_color_scheme_id=240,
            only_theme_color_schemes=False
        )
    ],
    user_color_schemes=[
        UserColorScheme(
            id=24,
            name='name8',
            is_dark=False,
            colors=[
                jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            ],
            theme_id=250
        )
    ],
    default_light_color_scheme=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    default_dark_color_scheme=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    censored_regexp=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    custom_emoji_translation=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    watched_words_replace='watched_words_replace6',
    watched_words_link='watched_words_link8',
    categories=[
        Category4(
            id=16,
            name='name8',
            color='color2',
            text_color='text_color0',
            slug='slug2',
            topic_count=172,
            post_count=244,
            position=46,
            topic_url='topic_url0',
            read_restricted=False,
            permission=54,
            notification_level=112,
            topic_template='topic_template6',
            topic_title_placeholder='topic_title_placeholder4',
            has_children=False,
            subcategory_count=74,
            sort_order='sort_order8',
            sort_ascending='sort_ascending8',
            show_subcategory_list=False,
            num_featured_topics=140,
            default_view='default_view2',
            subcategory_list_style='subcategory_list_style4',
            default_top_period='default_top_period2',
            default_list_filter='default_list_filter6',
            minimum_required_tags=172,
            navigate_to_first_post_after_read=False,
            allowed_tags=[
                jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            ],
            allowed_tag_groups=[
                jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            ],
            allow_global_tags=False,
            required_tag_groups=[
                RequiredTagGroup(
                    name='name4',
                    min_count=58
                )
            ],
            read_only_banner='read_only_banner2',
            uploaded_logo='uploaded_logo6',
            uploaded_logo_dark='uploaded_logo_dark4',
            uploaded_background='uploaded_background2',
            uploaded_background_dark='uploaded_background_dark2',
            can_edit=False,
            style_type='style_type0',
            emoji='emoji0',
            icon='icon0',
            description='description8',
            description_text='description_text0'
        )
    ],
    archetypes=[
        Archetype(
            id='id8',
            name='name8',
            options=[
                jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            ]
        )
    ],
    user_fields=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    auth_providers=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    full_name_required_for_signup=False,
    full_name_visible_in_signup=False,
    user_tips=UserTips(
        first_notification=66,
        topic_timeline=210,
        post_menu=220,
        topic_notification_levels=254,
        suggested_topics=202
    ),
    wizard_required=False,
    can_associate_groups=False,
    upcoming_changes_with_css=[
        'upcoming_changes_with_css3'
    ],
    markdown_additional_options=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)
```

