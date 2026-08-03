
# Topic List 1

*This model accepts additional fields of type Any.*

## Structure

`TopicList1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `can_create_topic` | `bool` | Optional | - |
| `draft` | `str` | Optional | - |
| `draft_key` | `str` | Optional | - |
| `draft_sequence` | `int` | Optional | - |
| `per_page` | `int` | Optional | - |
| `topics` | [`List[Topic2]`](../../doc/models/topic-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.topic_list_1 import TopicList1

topic_list_1 = TopicList1(
    can_create_topic=False,
    draft='draft8',
    draft_key='draft_key6',
    draft_sequence=36,
    per_page=160,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

