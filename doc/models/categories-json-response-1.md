
# Categories Json Response 1

## Structure

`CategoriesJsonResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category_list` | [`CategoryList`](../../doc/models/category-list.md) | Required | - |

## Example

```python
import jsonpickle

from discourse.models.categories_json_response_1 import CategoriesJsonResponse1
from discourse.models.category_1 import Category1
from discourse.models.category_list import CategoryList

categories_json_response_1 = CategoriesJsonResponse1(
    category_list=CategoryList(
        can_create_category=False,
        can_create_topic=False,
        categories=[
            Category1(
                id=16,
                name='name8',
                color='color2',
                text_color='text_color0',
                style_type='style_type0',
                emoji='emoji0',
                icon='icon0',
                slug='slug2',
                topic_count=172,
                post_count=244,
                position=46,
                description='description8',
                description_text='description_text0',
                description_excerpt='description_excerpt8',
                topic_url='topic_url0',
                read_restricted=False,
                permission=54,
                notification_level=112,
                can_edit=False,
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
                topics_day=50,
                topics_week=152,
                topics_month=6,
                topics_year=54,
                topics_all_time=162,
                subcategory_ids=[
                    jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                    jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                    jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                ],
                uploaded_logo='uploaded_logo6',
                uploaded_logo_dark='uploaded_logo_dark4',
                uploaded_background='uploaded_background2',
                uploaded_background_dark='uploaded_background_dark2',
                is_uncategorized=False,
                subcategory_list=[
                    jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                    jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                ]
            )
        ]
    )
)
```

