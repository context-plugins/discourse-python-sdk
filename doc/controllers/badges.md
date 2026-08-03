# Badges

```python
badges_api = client.badges
```

## Class Name

`BadgesApi`

## Methods

* [Admin List Badges](../../doc/controllers/badges.md#admin-list-badges)
* [Create Badge](../../doc/controllers/badges.md#create-badge)
* [Update Badge](../../doc/controllers/badges.md#update-badge)
* [Delete Badge](../../doc/controllers/badges.md#delete-badge)
* [List User Badges](../../doc/controllers/badges.md#list-user-badges)


# Admin List Badges

```python
def admin_list_badges(self)
```

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AdminBadgesJsonResponse`](../../doc/models/admin-badges-json-response.md).

## Example Usage

```python
result = badges_api.admin_list_badges()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Badge

```python
def create_badge(self,
                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AdminBadgesJsonRequest`](../../doc/models/admin-badges-json-request.md) | Body, Optional | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AdminBadgesJsonResponse1`](../../doc/models/admin-badges-json-response-1.md).

## Example Usage

```python
result = badges_api.create_badge()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Badge

```python
def update_badge(self,
                id,
                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | - |
| `body` | [`AdminBadgesJsonRequest1`](../../doc/models/admin-badges-json-request-1.md) | Body, Optional | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AdminBadgesJsonResponse2`](../../doc/models/admin-badges-json-response-2.md).

## Example Usage

```python
id = 112

result = badges_api.update_badge(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Badge

```python
def delete_badge(self,
                id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
id = 112

result = badges_api.delete_badge(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List User Badges

```python
def list_user_badges(self,
                    username)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `str` | Template, Required | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UserBadgesJsonResponse`](../../doc/models/user-badges-json-response.md).

## Example Usage

```python
username = 'username0'

result = badges_api.list_user_badges(username)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

