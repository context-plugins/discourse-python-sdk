
# Topic List 4

*This model accepts additional fields of type Any.*

## Structure

`TopicList4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `can_create_topic` | `bool` | Optional | - |
| `draft` | `str` | Optional | - |
| `draft_key` | `str` | Optional | - |
| `draft_sequence` | `int` | Optional | - |
| `per_page` | `int` | Optional | - |
| `topics` | [`List[Topic6]`](../../doc/models/topic-6.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.topic_list_4 import TopicList4

topic_list_4 = TopicList4(
    can_create_topic=False,
    draft='draft0',
    draft_key='draft_key8',
    draft_sequence=132,
    per_page=64,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

