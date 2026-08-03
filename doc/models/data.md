
# Data

*This model accepts additional fields of type Any.*

## Structure

`Data`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `badge_id` | `int` | Optional | - |
| `badge_name` | `str` | Optional | - |
| `badge_slug` | `str` | Optional | - |
| `badge_title` | `bool` | Optional | - |
| `username` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.data import Data

data = Data(
    badge_id=98,
    badge_name='badge_name8',
    badge_slug='badge_slug4',
    badge_title=False,
    username='username0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

