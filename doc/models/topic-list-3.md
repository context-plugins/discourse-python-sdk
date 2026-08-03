
# Topic List 3

*This model accepts additional fields of type Any.*

## Structure

`TopicList3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `can_create_topic` | `bool` | Optional | - |
| `draft` | `str` | Optional | - |
| `draft_key` | `str` | Optional | - |
| `draft_sequence` | `int` | Optional | - |
| `per_page` | `int` | Optional | - |
| `tags` | [`List[Tag4]`](../../doc/models/tag-4.md) | Optional | - |
| `topics` | [`List[Topic4]`](../../doc/models/topic-4.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.topic_list_3 import TopicList3

topic_list_3 = TopicList3(
    can_create_topic=False,
    draft='draft2',
    draft_key='draft_key0',
    draft_sequence=76,
    per_page=120,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

