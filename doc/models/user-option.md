
# User Option

## Structure

`UserOption`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `int` | Required | - |
| `mailing_list_mode` | `bool` | Required | - |
| `mailing_list_mode_frequency` | `int` | Required | - |
| `email_digests` | `bool` | Required | - |
| `email_level` | `int` | Required | - |
| `email_messages_level` | `int` | Required | - |
| `external_links_in_new_tab` | `bool` | Required | - |
| `bookmark_auto_delete_preference` | `int` | Optional | - |
| `color_scheme_id` | `str` | Required | - |
| `dark_scheme_id` | `str` | Required | - |
| `dynamic_favicon` | `bool` | Required | - |
| `enable_quoting` | `bool` | Required | - |
| `enable_smart_lists` | `bool` | Required | - |
| `enable_markdown_monospace_font` | `bool` | Required | - |
| `enable_defer` | `bool` | Required | - |
| `digest_after_minutes` | `int` | Required | - |
| `automatically_unpin_topics` | `bool` | Required | - |
| `auto_track_topics_after_msecs` | `int` | Required | - |
| `notification_level_when_replying` | `int` | Required | - |
| `new_topic_duration_minutes` | `int` | Required | - |
| `email_previous_replies` | `int` | Required | - |
| `email_in_reply_to` | `bool` | Required | - |
| `like_notification_frequency` | `int` | Required | - |
| `notify_on_linked_posts` | `bool` | Required | - |
| `push_notification_level` | `str` | Required | - |
| `enable_upcoming_change_available_notifications` | `bool` | Required | - |
| `include_tl_0_in_digests` | `bool` | Required | - |
| `theme_ids` | `List[Any]` | Required | - |
| `theme_key_seq` | `int` | Required | - |
| `allow_private_messages` | `bool` | Required | - |
| `enable_allowed_pm_users` | `bool` | Required | - |
| `homepage_id` | `str` | Required | - |
| `hide_profile_and_presence` | `bool` | Required | - |
| `hide_profile` | `bool` | Required | - |
| `hide_presence` | `bool` | Required | - |
| `text_size` | `str` | Required | - |
| `text_size_seq` | `int` | Required | - |
| `title_count_mode` | `str` | Required | - |
| `timezone` | `str` | Required | - |
| `skip_new_user_tips` | `bool` | Required | - |
| `default_calendar` | `str` | Optional | - |
| `oldest_search_log_date` | `str` | Optional | - |
| `sidebar_link_to_filtered_list` | `bool` | Optional | - |
| `sidebar_show_count_of_new_items` | `bool` | Optional | - |
| `watched_precedence_over_muted` | `bool` | Optional | - |
| `seen_popups` | `str` | Optional | - |
| `topics_unread_when_closed` | `bool` | Required | - |
| `composition_mode` | `int` | Optional | - |
| `interface_color_mode` | `int` | Required | - |
| `show_original_content` | `bool` | Required | - |

## Example

```python
import jsonpickle

from discourse.models.user_option import UserOption

user_option = UserOption(
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
)
```

