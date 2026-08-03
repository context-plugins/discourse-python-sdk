
# Tag Groups Json Response 2

*This model accepts additional fields of type Any.*

## Structure

`TagGroupsJsonResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tag_group` | [`TagGroup2`](../../doc/models/tag-group-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.tag_group_2 import TagGroup2
from discourseapidocumentation.models.tag_groups_json_response_2 import TagGroupsJsonResponse2

tag_groups_json_response_2 = TagGroupsJsonResponse2(
    tag_group=TagGroup2(
        id=164,
        name='name4',
        tag_names=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        parent_tag_name=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        one_per_topic=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

