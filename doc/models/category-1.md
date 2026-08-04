
# Category 1

## Structure

`Category1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `name` | `str` | Required | - |
| `color` | `str` | Required | - |
| `text_color` | `str` | Required | - |
| `style_type` | `str` | Required | - |
| `emoji` | `str` | Required | - |
| `icon` | `str` | Required | - |
| `slug` | `str` | Required | - |
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
| `topics_day` | `int` | Required | - |
| `topics_week` | `int` | Required | - |
| `topics_month` | `int` | Required | - |
| `topics_year` | `int` | Required | - |
| `topics_all_time` | `int` | Required | - |
| `is_uncategorized` | `bool` | Optional | - |
| `subcategory_ids` | `List[Any]` | Required | - |
| `subcategory_list` | `List[Any]` | Optional | - |
| `uploaded_logo` | `str` | Required | - |
| `uploaded_logo_dark` | `str` | Required | - |
| `uploaded_background` | `str` | Required | - |
| `uploaded_background_dark` | `str` | Required | - |

## Example

```python
import jsonpickle

from discourse.models.category_1 import Category1

category_1 = Category1(
    id=192,
    name='name0',
    color='color6',
    text_color='text_color2',
    style_type='style_type2',
    emoji='emoji2',
    icon='icon8',
    slug='slug6',
    topic_count=92,
    post_count=92,
    position=222,
    description='description0',
    description_text='description_text8',
    description_excerpt='description_excerpt0',
    topic_url='topic_url8',
    read_restricted=False,
    permission=230,
    notification_level=224,
    can_edit=False,
    topic_template='topic_template8',
    topic_title_placeholder='topic_title_placeholder4',
    has_children=False,
    subcategory_count=154,
    sort_order='sort_order0',
    sort_ascending='sort_ascending0',
    show_subcategory_list=False,
    num_featured_topics=220,
    default_view='default_view6',
    subcategory_list_style='subcategory_list_style6',
    default_top_period='default_top_period6',
    default_list_filter='default_list_filter2',
    minimum_required_tags=252,
    navigate_to_first_post_after_read=False,
    topics_day=226,
    topics_week=72,
    topics_month=74,
    topics_year=134,
    topics_all_time=174,
    subcategory_ids=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    uploaded_logo='uploaded_logo8',
    uploaded_logo_dark='uploaded_logo_dark4',
    uploaded_background='uploaded_background4',
    uploaded_background_dark='uploaded_background_dark6',
    is_uncategorized=False,
    subcategory_list=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ]
)
```

