
# Tag Group

## Structure

`TagGroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `name` | `str` | Required | - |
| `tags` | [`List[Tag]`](../../doc/models/tag.md) | Required | - |
| `parent_tag` | [`List[ParentTag]`](../../doc/models/parent-tag.md) | Required | - |
| `one_per_topic` | `bool` | Required | - |
| `permissions` | `Dict[str, int]` | Required | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.parent_tag import ParentTag
from discourseapidocumentation.models.tag import Tag
from discourseapidocumentation.models.tag_group import TagGroup

tag_group = TagGroup(
    id=164,
    name='name4',
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
    parent_tag=[
        ParentTag(
            id=110,
            name='name2',
            slug='slug6'
        )
    ],
    one_per_topic=False,
    permissions={
        'key0': 247,
        'key1': 248,
        'key2': 249
    }
)
```

