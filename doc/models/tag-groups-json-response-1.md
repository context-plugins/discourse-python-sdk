
# Tag Groups Json Response 1

## Structure

`TagGroupsJsonResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tag_group` | [`TagGroup1`](../../doc/models/tag-group-1.md) | Required | - |

## Example

```python
import jsonpickle

from discourse.models.parent_tag import ParentTag
from discourse.models.tag import Tag
from discourse.models.tag_group_1 import TagGroup1
from discourse.models.tag_groups_json_response_1 import TagGroupsJsonResponse1

tag_groups_json_response_1 = TagGroupsJsonResponse1(
    tag_group=TagGroup1(
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
        permissions=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    )
)
```

