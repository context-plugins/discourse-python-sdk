# Tags

```python
tags_api = client.tags
```

## Class Name

`TagsApi`

## Methods

* [List Tag Groups](../../doc/controllers/tags.md#list-tag-groups)
* [Create Tag Group](../../doc/controllers/tags.md#create-tag-group)
* [Get Tag Group](../../doc/controllers/tags.md#get-tag-group)
* [Update Tag Group](../../doc/controllers/tags.md#update-tag-group)
* [List Tags](../../doc/controllers/tags.md#list-tags)
* [Get Tag](../../doc/controllers/tags.md#get-tag)


# List Tag Groups

```python
def list_tag_groups(self)
```

## Response Type

**200**: tags

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TagGroupsJsonResponse`](../../doc/models/tag-groups-json-response.md).

## Example Usage

```python
result = tags_api.list_tag_groups()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Tag Group

```python
def create_tag_group(self,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TagGroupsJsonRequest`](../../doc/models/tag-groups-json-request.md) | Body, Optional | - |

## Response Type

**200**: tag group created

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TagGroupsJsonResponse1`](../../doc/models/tag-groups-json-response-1.md).

## Example Usage

```python
result = tags_api.create_tag_group()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Tag Group

```python
def get_tag_group(self,
                 id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | - |

## Response Type

**200**: notifications

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TagGroupsJsonResponse2`](../../doc/models/tag-groups-json-response-2.md).

## Example Usage

```python
id = 'id0'

result = tags_api.get_tag_group(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Tag Group

```python
def update_tag_group(self,
                    id,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | - |
| `body` | [`TagGroupsJsonRequest1`](../../doc/models/tag-groups-json-request-1.md) | Body, Optional | - |

## Response Type

**200**: Tag group updated

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TagGroupsJsonResponse3`](../../doc/models/tag-groups-json-response-3.md).

## Example Usage

```python
id = 'id0'

result = tags_api.update_tag_group(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Tags

```python
def list_tags(self)
```

## Response Type

**200**: notifications

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TagsJsonResponse`](../../doc/models/tags-json-response.md).

## Example Usage

```python
result = tags_api.list_tags()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Tag

```python
def get_tag(self,
           name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Template, Required | - |

## Response Type

**200**: notifications

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TagJsonResponse`](../../doc/models/tag-json-response.md).

## Example Usage

```python
name = 'name0'

result = tags_api.get_tag(name)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

