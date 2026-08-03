
# Category 2

## Structure

`Category2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `name` | `str` | Required | - |
| `color` | `str` | Required | - |
| `text_color` | `str` | Required | - |
| `style_type` | `str` | Optional | - |
| `emoji` | `str` | Optional | - |
| `icon` | `str` | Optional | - |
| `slug` | `str` | Required | - |
| `locale` | `str` | Optional | - |
| `topic_count` | `int` | Required | - |
| `post_count` | `int` | Required | - |
| `position` | `int` | Required | - |
| `description` | `str` | Required | - |
| `description_text` | `str` | Required | - |
| `description_excerpt` | `str` | Required | - |
| `topic_url` | `str` | Required | - |
| `read_restricted` | `bool` | Required | - |
| `permission` | `int` | Required | - |
| `notification_level` | `int` | Required | - |
| `can_edit` | `bool` | Required | - |
| `topic_template` | `str` | Required | - |
| `topic_title_placeholder` | `str` | Required | - |
| `form_template_ids` | `List[Any]` | Required | - |
| `has_children` | `bool` | Required | - |
| `subcategory_count` | `int` | Required | - |
| `sort_order` | `str` | Required | - |
| `sort_ascending` | `str` | Required | - |
| `show_subcategory_list` | `bool` | Required | - |
| `num_featured_topics` | `int` | Required | - |
| `default_view` | `str` | Required | - |
| `subcategory_list_style` | `str` | Required | - |
| `default_top_period` | `str` | Required | - |
| `default_list_filter` | `str` | Required | - |
| `minimum_required_tags` | `int` | Required | - |
| `navigate_to_first_post_after_read` | `bool` | Required | - |
| `custom_fields` | `Any` | Required | - |
| `allowed_tags` | `List[Any]` | Optional | - |
| `allowed_tag_groups` | `List[Any]` | Optional | - |
| `allow_global_tags` | `bool` | Optional | - |
| `required_tag_groups` | [`List[RequiredTagGroup]`](../../doc/models/required-tag-group.md) | Required | - |
| `category_setting` | [`CategorySetting`](../../doc/models/category-setting.md) | Optional | - |
| `category_localizations` | `List[Any]` | Optional | - |
| `read_only_banner` | `str` | Required | - |
| `available_groups` | `List[Any]` | Required | - |
| `auto_close_hours` | `str` | Required | - |
| `auto_close_based_on_last_post` | `bool` | Required | - |
| `allow_unlimited_owner_edits_on_first_post` | `bool` | Required | - |
| `default_slow_mode_seconds` | `str` | Required | - |
| `group_permissions` | [`List[GroupPermission]`](../../doc/models/group-permission.md) | Required | - |
| `email_in` | `str` | Required | - |
| `email_in_allow_strangers` | `bool` | Required | - |
| `mailinglist_mirror` | `bool` | Required | - |
| `all_topics_wiki` | `bool` | Required | - |
| `can_delete` | `bool` | Required | - |
| `allow_badges` | `bool` | Required | - |
| `topic_featured_link_allowed` | `bool` | Required | - |
| `search_priority` | `int` | Required | - |
| `topic_posting_review_group_ids` | `List[int]` | Required | - |
| `reply_posting_review_group_ids` | `List[int]` | Required | - |
| `uploaded_logo` | `str` | Required | - |
| `uploaded_logo_dark` | `str` | Required | - |
| `uploaded_background` | `str` | Required | - |
| `uploaded_background_dark` | `str` | Required | - |
| `category_types` | `Any` | Optional | - |
| `category_type_settings` | `Any` | Optional | - |
| `available_category_types` | [`List[AvailableCategoryType]`](../../doc/models/available-category-type.md) | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.category_2 import Category2
from discourseapidocumentation.models.group_permission import GroupPermission
from discourseapidocumentation.models.required_tag_group import RequiredTagGroup

category_2 = Category2(
    id=42,
    name='name8',
    color='color2',
    text_color='text_color0',
    slug='slug2',
    topic_count=198,
    post_count=14,
    position=72,
    description='description8',
    description_text='description_text0',
    description_excerpt='description_excerpt8',
    topic_url='topic_url0',
    read_restricted=False,
    permission=80,
    notification_level=138,
    can_edit=False,
    topic_template='topic_template6',
    topic_title_placeholder='topic_title_placeholder4',
    form_template_ids=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    has_children=False,
    subcategory_count=48,
    sort_order='sort_order8',
    sort_ascending='sort_ascending8',
    show_subcategory_list=False,
    num_featured_topics=114,
    default_view='default_view2',
    subcategory_list_style='subcategory_list_style4',
    default_top_period='default_top_period2',
    default_list_filter='default_list_filter6',
    minimum_required_tags=110,
    navigate_to_first_post_after_read=False,
    custom_fields=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    required_tag_groups=[
        RequiredTagGroup(
            name='name4',
            min_count=58
        )
    ],
    read_only_banner='read_only_banner2',
    available_groups=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    auto_close_hours='auto_close_hours8',
    auto_close_based_on_last_post=False,
    allow_unlimited_owner_edits_on_first_post=False,
    default_slow_mode_seconds='default_slow_mode_seconds2',
    group_permissions=[
        GroupPermission(
            permission_type=146,
            group_name='group_name4',
            group_id=230
        )
    ],
    email_in='email_in4',
    email_in_allow_strangers=False,
    mailinglist_mirror=False,
    all_topics_wiki=False,
    can_delete=False,
    allow_badges=False,
    topic_featured_link_allowed=False,
    search_priority=150,
    topic_posting_review_group_ids=[
        7
    ],
    reply_posting_review_group_ids=[
        80,
        81,
        82
    ],
    uploaded_logo='uploaded_logo6',
    uploaded_logo_dark='uploaded_logo_dark4',
    uploaded_background='uploaded_background2',
    uploaded_background_dark='uploaded_background_dark2',
    style_type='style_type0',
    emoji='emoji0',
    icon='icon0',
    locale='locale6',
    allowed_tags=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ]
)
```

