
# Category Localization

*This model accepts additional fields of type Any.*

## Structure

`CategoryLocalization`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The unique identifier for an existing localization.<br>Must be included otherwise the record will be deleted. |
| `locale` | `str` | Required | The locale for the localization, e.g., 'en',<br>'zh_CN'. Locale should be in the list of SiteSetting.content_localization_supported_locales. |
| `name` | `str` | Required | The name of the category in the specified locale. |
| `description` | `str` | Optional | The description excerpt of the category in the<br>specified locale. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.category_localization import CategoryLocalization

category_localization = CategoryLocalization(
    locale='locale8',
    name='name0',
    id=112,
    description='description0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

