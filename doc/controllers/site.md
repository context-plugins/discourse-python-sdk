# Site

```python
site_api = client.site
```

## Class Name

`SiteApi`

## Methods

* [Get Site](../../doc/controllers/site.md#get-site)
* [Get Site Basic Info](../../doc/controllers/site.md#get-site-basic-info)


# Get Site

Can be used to fetch all categories and subcategories

```python
def get_site(self)
```

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SiteJsonResponse`](../../doc/models/site-json-response.md).

## Example Usage

```python
result = site_api.get_site()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Site Basic Info

Can be used to fetch basic info about a site

```python
def get_site_basic_info(self)
```

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SiteBasicInfoJsonResponse`](../../doc/models/site-basic-info-json-response.md).

## Example Usage

```python
result = site_api.get_site_basic_info()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

