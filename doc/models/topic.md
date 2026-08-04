
# Topic

## Structure

`Topic`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `title` | `str` | Required | - |
| `tags` | `List[str]` | Required | - |
| `tags_descriptions` | `Any` | Required | - |
| `slug` | `str` | Required | - |

## Example

```python
import jsonpickle

from discourse.models.topic import Topic

topic = Topic(
    id=54,
    title='title4',
    tags=[
        'tags3'
    ],
    tags_descriptions=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    slug='slug2'
)
```

