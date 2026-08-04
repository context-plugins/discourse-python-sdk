
# T Json Request

*This model accepts additional fields of type Any.*

## Structure

`TJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `topic` | [`Topic5`](../../doc/models/topic-5.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.t_json_request import TJsonRequest
from discourse.models.topic_5 import Topic5

t_json_request = TJsonRequest(
    topic=Topic5(
        title='title4',
        category_id=208,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

