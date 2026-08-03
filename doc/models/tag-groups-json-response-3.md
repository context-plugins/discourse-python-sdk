
# Tag Groups Json Response 3

*This model accepts additional fields of type Any.*

## Structure

`TagGroupsJsonResponse3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `str` | Optional | - |
| `tag_group` | [`TagGroup2`](../../doc/models/tag-group-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.tag_group_2 import TagGroup2
from discourseapidocumentation.models.tag_groups_json_response_3 import TagGroupsJsonResponse3

tag_groups_json_response_3 = TagGroupsJsonResponse3(
    success='success6',
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

