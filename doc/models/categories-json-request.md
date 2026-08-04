
# Categories Json Request

## Structure

`CategoriesJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `color` | `str` | Optional | - |
| `text_color` | `str` | Optional | - |
| `style_type` | `str` | Optional | - |
| `emoji` | `str` | Optional | - |
| `icon` | `str` | Optional | - |
| `parent_category_id` | `int` | Optional | - |
| `allow_badges` | `bool` | Optional | - |
| `slug` | `str` | Optional | - |
| `topic_featured_links_allowed` | `bool` | Optional | - |
| `permissions` | [`Permissions`](../../doc/models/permissions.md) | Optional | - |
| `search_priority` | `int` | Optional | - |
| `form_template_ids` | `List[Any]` | Optional | - |
| `category_localizations` | [`List[CategoryLocalization]`](../../doc/models/category-localization.md) | Optional | - |

## Example

```python
from discourse.models.categories_json_request import CategoriesJsonRequest

categories_json_request = CategoriesJsonRequest(
    name='name6',
    color='49d9e9',
    text_color='f0fcfd',
    style_type='style_type8',
    emoji='emoji8',
    icon='icon8'
)
```

