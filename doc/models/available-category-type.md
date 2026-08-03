
# Available Category Type

## Structure

`AvailableCategoryType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | - |
| `name` | `str` | Required | - |
| `title` | `str` | Required | - |
| `description` | `str` | Required | - |
| `icon` | `str` | Required | - |
| `available` | `bool` | Required | - |
| `visible` | `bool` | Required | - |
| `configuration_schema` | `Any` | Required | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.available_category_type import AvailableCategoryType

available_category_type = AvailableCategoryType(
    id='id2',
    name='name2',
    title='title8',
    description='description2',
    icon='icon4',
    available=False,
    visible=False,
    configuration_schema=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)
```

