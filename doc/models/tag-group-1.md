
# Tag Group 1

*This model accepts additional fields of type Any.*

## Structure

`TagGroup1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `name` | `str` | Required | - |
| `tags` | [`List[Tag]`](../../doc/models/tag.md) | Required | - |
| `parent_tag` | [`List[ParentTag]`](../../doc/models/parent-tag.md) | Required | - |
| `one_per_topic` | `bool` | Required | - |
| `permissions` | `Any` | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.parent_tag import ParentTag
from discourse.models.tag import Tag
from discourse.models.tag_group_1 import TagGroup1

tag_group_1 = TagGroup1(
    id=16,
    name='name8',
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
    permissions=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

