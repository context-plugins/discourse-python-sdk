
# Basic Topic

*This model accepts additional fields of type Any.*

## Structure

`BasicTopic`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `title` | `str` | Optional | - |
| `fancy_title` | `str` | Optional | - |
| `slug` | `str` | Optional | - |
| `posts_count` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.basic_topic import BasicTopic

basic_topic = BasicTopic(
    id=150,
    title='title0',
    fancy_title='fancy_title4',
    slug='slug2',
    posts_count=32,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

