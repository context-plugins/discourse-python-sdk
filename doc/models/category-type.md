
# Category Type

## Structure

`CategoryType`

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

from discourse.models.category_type import CategoryType

category_type = CategoryType(
    id='id6',
    name='name6',
    title='title8',
    description='description6',
    icon='icon8',
    available=False,
    visible=False,
    configuration_schema=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)
```

