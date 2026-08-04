
# Categories Json Response

## Structure

`CategoriesJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category` | [`Category`](../../doc/models/category.md) | Required | - |

## Example

```python
import jsonpickle

from discourse.models.categories_json_response import CategoriesJsonResponse
from discourse.models.category import Category
from discourse.models.group_permission import GroupPermission
from discourse.models.required_tag_group import RequiredTagGroup

categories_json_response = CategoriesJsonResponse(
    category=Category(
        id=232,
        name='name2',
        color='color4',
        text_color='text_color4',
        style_type='style_type4',
        emoji='emoji4',
        icon='icon6',
        slug='slug4',
        topic_count=132,
        post_count=204,
        position=6,
        description='description8',
        description_text='description_text6',
        description_excerpt='description_excerpt2',
        topic_url='topic_url6',
        read_restricted=False,
        permission=14,
        notification_level=72,
        can_edit=False,
        topic_template='topic_template0',
        topic_title_placeholder='topic_title_placeholder2',
        has_children=False,
        subcategory_count=114,
        sort_order='sort_order2',
        sort_ascending='sort_ascending2',
        show_subcategory_list=False,
        num_featured_topics=180,
        default_view='default_view4',
        subcategory_list_style='subcategory_list_style8',
        default_top_period='default_top_period4',
        default_list_filter='default_list_filter0',
        minimum_required_tags=212,
        navigate_to_first_post_after_read=False,
        custom_fields=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        required_tag_groups=[
            RequiredTagGroup(
                name='name4',
                min_count=58
            )
        ],
        read_only_banner='read_only_banner4',
        available_groups=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        auto_close_hours='auto_close_hours2',
        auto_close_based_on_last_post=False,
        allow_unlimited_owner_edits_on_first_post=False,
        default_slow_mode_seconds='default_slow_mode_seconds6',
        group_permissions=[
            GroupPermission(
                permission_type=146,
                group_name='group_name4',
                group_id=230
            )
        ],
        email_in='email_in8',
        email_in_allow_strangers=False,
        mailinglist_mirror=False,
        all_topics_wiki=False,
        can_delete=False,
        allow_badges=False,
        topic_featured_link_allowed=False,
        search_priority=172,
        topic_posting_review_group_ids=[
            197
        ],
        reply_posting_review_group_ids=[
            14,
            15,
            16
        ],
        uploaded_logo='uploaded_logo0',
        uploaded_logo_dark='uploaded_logo_dark2',
        uploaded_background='uploaded_background6',
        uploaded_background_dark='uploaded_background_dark4',
        locale='locale0',
        form_template_ids=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        allowed_tags=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        allowed_tag_groups=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        allow_global_tags=False
    )
)
```

