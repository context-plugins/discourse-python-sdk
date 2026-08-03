
# Topic List 5

*This model accepts additional fields of type Any.*

## Structure

`TopicList5`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `can_create_topic` | `bool` | Optional | - |
| `draft` | `str` | Optional | - |
| `draft_key` | `str` | Optional | - |
| `draft_sequence` | `int` | Optional | - |
| `for_period` | `str` | Optional | - |
| `per_page` | `int` | Optional | - |
| `topics` | [`List[Topic7]`](../../doc/models/topic-7.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.topic_list_5 import TopicList5

topic_list_5 = TopicList5(
    can_create_topic=False,
    draft='draft6',
    draft_key='draft_key4',
    draft_sequence=118,
    for_period='for_period6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

