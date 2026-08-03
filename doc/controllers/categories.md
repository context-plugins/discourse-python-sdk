# Categories

```python
categories_api = client.categories
```

## Class Name

`CategoriesApi`

## Methods

* [Create Category](../../doc/controllers/categories.md#create-category)
* [List Categories](../../doc/controllers/categories.md#list-categories)
* [Update Category](../../doc/controllers/categories.md#update-category)
* [List Category Topics](../../doc/controllers/categories.md#list-category-topics)
* [Get Category](../../doc/controllers/categories.md#get-category)


# Create Category

```python
def create_category(self,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CategoriesJsonRequest`](../../doc/models/categories-json-request.md) | Body, Optional | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CategoriesJsonResponse`](../../doc/models/categories-json-response.md).

## Example Usage

```python
body = CategoriesJsonRequest(
    name='name6',
    color='49d9e9',
    text_color='f0fcfd'
)

result = categories_api.create_category(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Categories

```python
def list_categories(self,
                   include_subcategories=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `include_subcategories` | `bool` | Query, Optional | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CategoriesJsonResponse1`](../../doc/models/categories-json-response-1.md).

## Example Usage

```python
result = categories_api.list_categories()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Category

```python
def update_category(self,
                   id,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | - |
| `body` | [`CategoriesJsonRequest1`](../../doc/models/categories-json-request-1.md) | Body, Optional | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CategoriesJsonResponse2`](../../doc/models/categories-json-response-2.md).

## Example Usage

```python
id = 112

body = CategoriesJsonRequest1(
    name='name6',
    color='49d9e9',
    text_color='f0fcfd'
)

result = categories_api.update_category(
    id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Category Topics

```python
def list_category_topics(self,
                        slug,
                        id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `slug` | `str` | Template, Required | - |
| `id` | `int` | Template, Required | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CJsonResponse`](../../doc/models/c-json-response.md).

## Example Usage

```python
slug = 'slug6'

id = 112

result = categories_api.list_category_topics(
    slug,
    id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Category

```python
def get_category(self,
                id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | - |

## Response Type

**200**: response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CShowJsonResponse`](../../doc/models/c-show-json-response.md).

## Example Usage

```python
id = 112

result = categories_api.get_category(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

