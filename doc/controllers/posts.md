# Posts

```python
posts_api = client.posts
```

## Class Name

`PostsApi`

## Methods

* [List Posts](../../doc/controllers/posts.md#list-posts)
* [Create Topic Post PM](../../doc/controllers/posts.md#create-topic-post-pm)
* [Get Post](../../doc/controllers/posts.md#get-post)
* [Update Post](../../doc/controllers/posts.md#update-post)
* [Delete Post](../../doc/controllers/posts.md#delete-post)
* [Post Replies](../../doc/controllers/posts.md#post-replies)
* [Lock Post](../../doc/controllers/posts.md#lock-post)
* [Perform Post Action](../../doc/controllers/posts.md#perform-post-action)


# List Posts

```python
def list_posts(self,
              before=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `before` | `int` | Query, Optional | Load posts with an id lower than this value. Useful for pagination. |

## Response Type

**200**: latest posts

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PostsJsonResponse`](../../doc/models/posts-json-response.md).

## Example Usage

```python
result = posts_api.list_posts()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Topic Post PM

```python
def create_topic_post_pm(self,
                        api_key,
                        api_username,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Header, Required | - |
| `api_username` | `str` | Header, Required | - |
| `body` | [`PostsJsonRequest`](../../doc/models/posts-json-request.md) | Body, Optional | - |

## Response Type

**200**: post created

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PostsJsonResponse1`](../../doc/models/posts-json-response-1.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

body = PostsJsonRequest(
    raw='raw0',
    target_recipients='blake,sam',
    archetype='private_message'
)

result = posts_api.create_topic_post_pm(
    api_key,
    api_username,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Post

This endpoint can be used to get the number of likes on a post using the
`actions_summary` property in the response. `actions_summary` responses
with the id of `2` signify a `like`. If there are no `actions_summary`
items with the id of `2`, that means there are 0 likes. Other ids likely
refer to various different flag types.

```python
def get_post(self,
            id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | - |

## Response Type

**200**: single reviewable post

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PostsJsonResponse2`](../../doc/models/posts-json-response-2.md).

## Example Usage

```python
id = 'id0'

result = posts_api.get_post(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Post

```python
def update_post(self,
               api_key,
               api_username,
               id,
               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Header, Required | - |
| `api_username` | `str` | Header, Required | - |
| `id` | `str` | Template, Required | - |
| `body` | [`PostsJsonRequest1`](../../doc/models/posts-json-request-1.md) | Body, Optional | - |

## Response Type

**200**: post updated

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PostsJsonResponse3`](../../doc/models/posts-json-response-3.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

id = 'id0'

result = posts_api.update_post(
    api_key,
    api_username,
    id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Post

```python
def delete_post(self,
               api_key,
               api_username,
               id,
               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Header, Required | - |
| `api_username` | `str` | Header, Required | - |
| `id` | `int` | Template, Required | - |
| `body` | [`PostsJsonRequest2`](../../doc/models/posts-json-request-2.md) | Body, Optional | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

id = 112

body = PostsJsonRequest2(
    force_destroy=True
)

result = posts_api.delete_post(
    api_key,
    api_username,
    id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Post Replies

```python
def post_replies(self,
                id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | - |

## Response Type

**200**: post replies

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[PostsRepliesJsonResponse]`](../../doc/models/posts-replies-json-response.md).

## Example Usage

```python
id = 'id0'

result = posts_api.post_replies(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Lock Post

```python
def lock_post(self,
             api_key,
             api_username,
             id,
             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Header, Required | - |
| `api_username` | `str` | Header, Required | - |
| `id` | `str` | Template, Required | - |
| `body` | [`PostsLockedJsonRequest`](../../doc/models/posts-locked-json-request.md) | Body, Optional | - |

## Response Type

**200**: post updated

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PostsLockedJsonResponse`](../../doc/models/posts-locked-json-response.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

id = 'id0'

result = posts_api.lock_post(
    api_key,
    api_username,
    id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Perform Post Action

```python
def perform_post_action(self,
                       api_key,
                       api_username,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Header, Required | - |
| `api_username` | `str` | Header, Required | - |
| `body` | [`PostActionsJsonRequest`](../../doc/models/post-actions-json-request.md) | Body, Optional | - |

## Response Type

**200**: post updated

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PostActionsJsonResponse`](../../doc/models/post-actions-json-response.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

result = posts_api.perform_post_action(
    api_key,
    api_username
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

