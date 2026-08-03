
# Search Json Response

## Structure

`SearchJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `posts` | `List[Any]` | Required | - |
| `users` | `List[Any]` | Required | - |
| `categories` | `List[Any]` | Required | - |
| `tags` | [`List[Tag]`](../../doc/models/tag.md) | Required | - |
| `groups` | `List[Any]` | Required | - |
| `grouped_search_result` | [`GroupedSearchResult`](../../doc/models/grouped-search-result.md) | Required | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.extra import Extra
from discourseapidocumentation.models.grouped_search_result import GroupedSearchResult
from discourseapidocumentation.models.search_json_response import SearchJsonResponse
from discourseapidocumentation.models.tag import Tag

search_json_response = SearchJsonResponse(
    posts=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    users=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    categories=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    tags=[
        Tag(
            id=26,
            name='name0',
            slug='slug4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    groups=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    grouped_search_result=GroupedSearchResult(
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
)
```

