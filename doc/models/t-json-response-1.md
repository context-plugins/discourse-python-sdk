
# T Json Response 1

*This model accepts additional fields of type Any.*

## Structure

`TJsonResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `basic_topic` | [`BasicTopic`](../../doc/models/basic-topic.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.basic_topic import BasicTopic
from discourse.models.t_json_response_1 import TJsonResponse1

t_json_response_1 = TJsonResponse1(
    basic_topic=BasicTopic(
        id=150,
        title='title0',
        fancy_title='fancy_title4',
        slug='slug2',
        posts_count=32,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

