
# Topic List 2

*This model accepts additional fields of type Any.*

## Structure

`TopicList2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `can_create_topic` | `bool` | Optional | - |
| `draft` | `str` | Optional | - |
| `draft_key` | `str` | Optional | - |
| `draft_sequence` | `int` | Optional | - |
| `per_page` | `int` | Optional | - |
| `topics` | [`List[Topic3]`](../../doc/models/topic-3.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.topic_list_2 import TopicList2

topic_list_2 = TopicList2(
    can_create_topic=False,
    draft='draft0',
    draft_key='draft_key8',
    draft_sequence=86,
    per_page=110,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

