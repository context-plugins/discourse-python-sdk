
# Tag Groups Json Response

## Structure

`TagGroupsJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tag_groups` | [`List[TagGroup]`](../../doc/models/tag-group.md) | Required | - |

## Example

```python
import jsonpickle

from discourse.models.parent_tag import ParentTag
from discourse.models.tag import Tag
from discourse.models.tag_group import TagGroup
from discourse.models.tag_groups_json_response import TagGroupsJsonResponse

tag_groups_json_response = TagGroupsJsonResponse(
    tag_groups=[
        TagGroup(
            id=140,
            name='name0',
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
                'key0': 223,
                'key1': 224,
                'key2': 225
            }
        )
    ]
)
```

