
# Tag Groups Json Request 1

*This model accepts additional fields of type Any.*

## Structure

`TagGroupsJsonRequest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.tag_groups_json_request_1 import TagGroupsJsonRequest1

tag_groups_json_request_1 = TagGroupsJsonRequest1(
    name='name4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

