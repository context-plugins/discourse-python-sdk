
# U Json Response

## Structure

`UJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_badges` | `List[Any]` | Required | - |
| `user` | [`User8`](../../doc/models/user-8.md) | Required | - |

## Example

```python
import jsonpickle

from discourse.models.custom_fields import CustomFields
from discourse.models.featured_topic import FeaturedTopic
from discourse.models.group_7 import Group7
from discourse.models.group_user import GroupUser
from discourse.models.u_json_response import UJsonResponse
from discourse.models.user_8 import User8
from discourse.models.user_auth_token import UserAuthToken
from discourse.models.user_notification_schedule import UserNotificationSchedule
from discourse.models.user_option import UserOption

u_json_response = UJsonResponse(
    user_badges=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    user=User8(
        id=76,
        username='username0',
        name='name0',
        avatar_template='avatar_template0',
        last_posted_at='last_posted_at8',
        last_seen_at='last_seen_at6',
        created_at='created_at2',
        ignored=False,
        muted=False,
        can_ignore_user=False,
        can_mute_user=False,
        can_send_private_messages=False,
        can_send_private_message_to_user=False,
        trust_level=196,
        moderator=False,
        admin=False,
        title='title4',
        badge_count=158,
        custom_fields=CustomFields(
            first_name='first_name2'
        ),
        time_read=24,
        recent_time_read=170,
        primary_group_id=88,
        primary_group_name='primary_group_name8',
        flair_group_id=126,
        flair_name='flair_name6',
        flair_url='flair_url0',
        flair_bg_color='flair_bg_color4',
        flair_color='flair_color6',
        featured_topic=FeaturedTopic(
            id=50,
            title='title6',
            fancy_title='fancy_title0',
            slug='slug6',
            posts_count=188
        ),
        staged=False,
        can_edit=False,
        can_edit_username=False,
        can_edit_email=False,
        can_edit_name=False,
        uploaded_avatar_id=152,
        has_title_badges=False,
        pending_count=4,
        profile_view_count=24,
        second_factor_enabled=False,
        can_upload_profile_header=False,
        can_upload_user_card_background=False,
        post_count=48,
        topic_count=232,
        can_be_deleted=False,
        can_delete_all_posts=False,
        locale='locale8',
        muted_category_ids=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        regular_category_ids=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        watched_tags=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        watching_first_post_tags=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        tracked_tags=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        muted_tags=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        tracked_category_ids=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        watched_category_ids=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        watched_first_post_category_ids=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        system_avatar_upload_id='system_avatar_upload_id2',
        system_avatar_template='system_avatar_template6',
        muted_usernames=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        ignored_usernames=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        allowed_pm_usernames=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        mailing_list_posts_per_day=94,
        can_change_bio=False,
        can_change_location=False,
        can_change_website=False,
        can_change_tracking_preferences=False,
        user_api_keys='user_api_keys4',
        user_auth_tokens=[
            UserAuthToken(
                id=30,
                client_ip='client_ip2',
                location='location6',
                browser='browser2',
                device='device8',
                os='os0',
                icon='icon4',
                created_at='created_at0',
                seen_at='seen_at2',
                is_active=False
            )
        ],
        user_notification_schedule=UserNotificationSchedule(
            enabled=False,
            day_0_start_time=242,
            day_0_end_time=54,
            day_1_start_time=130,
            day_1_end_time=246,
            day_2_start_time=112,
            day_2_end_time=212,
            day_3_start_time=160,
            day_3_end_time=110,
            day_4_start_time=186,
            day_4_end_time=212,
            day_5_start_time=48,
            day_5_end_time=64,
            day_6_start_time=102,
            day_6_end_time=208
        ),
        use_logo_small_as_avatar=False,
        featured_user_badge_ids=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        invited_by='invited_by4',
        groups=[
            Group7(
                id=152,
                automatic=False,
                name='name6',
                display_name='display_name6',
                user_count=248,
                mentionable_level=236,
                messageable_level=92,
                visibility_level=196,
                primary_group=False,
                title='title2',
                grant_trust_level='grant_trust_level8',
                incoming_email='incoming_email6',
                has_messages=False,
                flair_url='flair_url6',
                flair_bg_color='flair_bg_color0',
                flair_color='flair_color0',
                bio_raw='bio_raw8',
                bio_cooked='bio_cooked2',
                bio_excerpt='bio_excerpt0',
                public_admission=False,
                public_exit=False,
                allow_membership_requests=False,
                full_name='full_name2',
                default_notification_level=112,
                membership_request_template='membership_request_template2',
                members_visibility_level=0,
                can_see_members=False,
                can_admin_group=False,
                publish_read_state=False
            )
        ],
        group_users=[
            GroupUser(
                group_id=176,
                user_id=4,
                notification_level=4,
                owner=False
            )
        ],
        user_option=UserOption(
            user_id=122,
            mailing_list_mode=False,
            mailing_list_mode_frequency=176,
            email_digests=False,
            email_level=112,
            email_messages_level=58,
            external_links_in_new_tab=False,
            color_scheme_id='color_scheme_id2',
            dark_scheme_id='dark_scheme_id6',
            dynamic_favicon=False,
            enable_quoting=False,
            enable_smart_lists=False,
            enable_markdown_monospace_font=False,
            enable_defer=False,
            digest_after_minutes=8,
            automatically_unpin_topics=False,
            auto_track_topics_after_msecs=128,
            notification_level_when_replying=80,
            new_topic_duration_minutes=210,
            email_previous_replies=154,
            email_in_reply_to=False,
            like_notification_frequency=64,
            notify_on_linked_posts=False,
            push_notification_level='push_notification_level4',
            enable_upcoming_change_available_notifications=False,
            include_tl_0_in_digests=False,
            theme_ids=[
                jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            ],
            theme_key_seq=74,
            allow_private_messages=False,
            enable_allowed_pm_users=False,
            homepage_id='homepage_id4',
            hide_profile_and_presence=False,
            hide_profile=False,
            hide_presence=False,
            text_size='text_size4',
            text_size_seq=126,
            title_count_mode='title_count_mode4',
            timezone='timezone2',
            skip_new_user_tips=False,
            topics_unread_when_closed=False,
            interface_color_mode=78,
            show_original_content=False,
            bookmark_auto_delete_preference=190,
            default_calendar='default_calendar2',
            oldest_search_log_date='oldest_search_log_date2',
            sidebar_link_to_filtered_list=False,
            sidebar_show_count_of_new_items=False
        ),
        can_ignore_users=False,
        can_mute_users=False,
        second_factor_backup_enabled=False,
        user_fields={
            'key0': 'user_fields1',
            'key1': 'user_fields0',
            'key2': 'user_fields9'
        },
        pending_posts_count=124
    )
)
```

