
# Grouped Search Result

## Structure

`GroupedSearchResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `more_posts` | `str` | Required | - |
| `more_users` | `str` | Required | - |
| `more_categories` | `str` | Required | - |
| `term` | `str` | Required | - |
| `search_log_id` | `int` | Required | - |
| `more_full_page_results` | `str` | Required | - |
| `can_create_topic` | `bool` | Required | - |
| `error` | `str` | Required | - |
| `extra` | [`Extra`](../../doc/models/extra.md) | Optional | - |
| `post_ids` | `List[Any]` | Required | - |
| `user_ids` | `List[Any]` | Required | - |
| `category_ids` | `List[Any]` | Required | - |
| `tag_ids` | `List[Any]` | Required | - |
| `group_ids` | `List[Any]` | Required | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.extra import Extra
from discourseapidocumentation.models.grouped_search_result import GroupedSearchResult

grouped_search_result = GroupedSearchResult(
    more_posts='more_posts4',
    more_users='more_users2',
    more_categories='more_categories2',
    term='term6',
    search_log_id=80,
    more_full_page_results='more_full_page_results2',
    can_create_topic=False,
    error='error6',
    post_ids=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    user_ids=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    category_ids=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    tag_ids=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    group_ids=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    extra=Extra(
        categories='categories8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    )
)
```

