
# Category 4

## Structure

`Category4`

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
| `topic_count` | `int` | Required | - |
| `post_count` | `int` | Required | - |
| `position` | `int` | Required | - |
| `description` | `str` | Optional | - |
| `description_text` | `str` | Optional | - |
| `description_excerpt` | `str` | Optional | - |
| `topic_url` | `str` | Required | - |
| `read_restricted` | `bool` | Required | - |
| `permission` | `int` | Required | - |
| `notification_level` | `int` | Required | - |
| `topic_template` | `str` | Required | - |
| `topic_title_placeholder` | `str` | Required | - |
| `has_children` | `bool` | Required | - |
| `subcategory_count` | `int` | Required | - |
| `sort_order` | `str` | Required | - |
| `sort_ascending` | `bool` | Required | - |
| `show_subcategory_list` | `bool` | Required | - |
| `num_featured_topics` | `int` | Required | - |
| `default_view` | `str` | Required | - |
| `subcategory_list_style` | `str` | Required | - |
| `default_top_period` | `str` | Required | - |
| `default_list_filter` | `str` | Required | - |
| `minimum_required_tags` | `int` | Required | - |
| `navigate_to_first_post_after_read` | `bool` | Required | - |
| `allowed_tags` | `List[Any]` | Optional | - |
| `allowed_tag_groups` | `List[Any]` | Optional | - |
| `allow_global_tags` | `bool` | Required | - |
| `required_tag_groups` | [`List[RequiredTagGroup]`](../../doc/models/required-tag-group.md) | Required | - |
| `read_only_banner` | `str` | Required | - |
| `uploaded_logo` | `str` | Required | - |
| `uploaded_logo_dark` | `str` | Required | - |
| `uploaded_background` | `str` | Required | - |
| `uploaded_background_dark` | `str` | Required | - |
| `can_edit` | `bool` | Required | - |
| `custom_fields` | `Any` | Optional | - |
| `parent_category_id` | `int` | Optional | - |
| `form_template_ids` | `List[Any]` | Optional | - |
| `category_types` | `Any` | Optional | - |

## Example

```python
from discourse.models.category_4 import Category4
from discourse.models.required_tag_group import RequiredTagGroup

category_4 = Category4(
    id=216,
    name='name0',
    color='color4',
    text_color='text_color2',
    slug='slug6',
    topic_count=116,
    post_count=188,
    position=246,
    topic_url='topic_url8',
    read_restricted=False,
    permission=254,
    notification_level=56,
    topic_template='topic_template8',
    topic_title_placeholder='topic_title_placeholder6',
    has_children=False,
    subcategory_count=130,
    sort_order='sort_order0',
    sort_ascending=False,
    show_subcategory_list=False,
    num_featured_topics=196,
    default_view='default_view6',
    subcategory_list_style='subcategory_list_style6',
    default_top_period='default_top_period4',
    default_list_filter='default_list_filter8',
    minimum_required_tags=228,
    navigate_to_first_post_after_read=False,
    allow_global_tags=False,
    required_tag_groups=[
        RequiredTagGroup(
            name='name4',
            min_count=58
        )
    ],
    read_only_banner='read_only_banner6',
    uploaded_logo='uploaded_logo8',
    uploaded_logo_dark='uploaded_logo_dark6',
    uploaded_background='uploaded_background4',
    uploaded_background_dark='uploaded_background_dark6',
    can_edit=False,
    style_type='style_type2',
    emoji='emoji2',
    icon='icon2',
    description='description0',
    description_text='description_text8'
)
```

