
# Tags Json Response

*This model accepts additional fields of type Any.*

## Structure

`TagsJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tags` | [`List[Tag3]`](../../doc/models/tag-3.md) | Optional | - |
| `extras` | [`Extras3`](../../doc/models/extras-3.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.extras_3 import Extras3
from discourse.models.tag_3 import Tag3
from discourse.models.tags_json_response import TagsJsonResponse

tags_json_response = TagsJsonResponse(
    tags=[
        Tag3(
            id=26,
            text='text0',
            name='name0',
            count=110,
            pm_count=76,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    extras=Extras3(
        categories=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

