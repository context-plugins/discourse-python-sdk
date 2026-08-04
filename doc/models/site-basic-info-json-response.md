
# Site Basic Info Json Response

## Structure

`SiteBasicInfoJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `logo_url` | `str` | Required | - |
| `logo_small_url` | `str` | Required | - |
| `apple_touch_icon_url` | `str` | Required | - |
| `favicon_url` | `str` | Required | - |
| `title` | `str` | Required | - |
| `description` | `str` | Required | - |
| `header_primary_color` | `str` | Required | - |
| `header_background_color` | `str` | Required | - |
| `login_required` | `bool` | Required | - |
| `locale` | `str` | Required | - |
| `include_in_discourse_discover` | `bool` | Required | - |
| `mobile_logo_url` | `str` | Required | - |

## Example

```python
from discourse.models.site_basic_info_json_response import SiteBasicInfoJsonResponse

site_basic_info_json_response = SiteBasicInfoJsonResponse(
    logo_url='logo_url2',
    logo_small_url='logo_small_url8',
    apple_touch_icon_url='apple_touch_icon_url8',
    favicon_url='favicon_url2',
    title='title8',
    description='description2',
    header_primary_color='header_primary_color0',
    header_background_color='header_background_color2',
    login_required=False,
    locale='locale0',
    include_in_discourse_discover=False,
    mobile_logo_url='mobile_logo_url4'
)
```

