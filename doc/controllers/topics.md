# Topics

```python
topics_api = client.topics
```

## Class Name

`TopicsApi`

## Methods

* [Get Specific Posts from Topic](../../doc/controllers/topics.md#get-specific-posts-from-topic)
* [Get Topic](../../doc/controllers/topics.md#get-topic)
* [Remove Topic](../../doc/controllers/topics.md#remove-topic)
* [Update Topic](../../doc/controllers/topics.md#update-topic)
* [Invite to Topic](../../doc/controllers/topics.md#invite-to-topic)
* [Invite Group to Topic](../../doc/controllers/topics.md#invite-group-to-topic)
* [Bookmark Topic](../../doc/controllers/topics.md#bookmark-topic)
* [Update Topic Status](../../doc/controllers/topics.md#update-topic-status)
* [List Latest Topics](../../doc/controllers/topics.md#list-latest-topics)
* [List Top Topics](../../doc/controllers/topics.md#list-top-topics)
* [Set Notification Level](../../doc/controllers/topics.md#set-notification-level)
* [Update Topic Timestamp](../../doc/controllers/topics.md#update-topic-timestamp)
* [Create Topic Timer](../../doc/controllers/topics.md#create-topic-timer)
* [Get Topic by External Id](../../doc/controllers/topics.md#get-topic-by-external-id)


# Get Specific Posts from Topic

```python
def get_specific_posts_from_topic(self,
                                 api_key,
                                 api_username,
                                 id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Header, Required | - |
| `api_username` | `str` | Header, Required | - |
| `id` | `str` | Template, Required | - |

## Response Type

**200**: specific posts

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TPostsJsonResponse`](../../doc/models/t-posts-json-response.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

id = 'id0'

result = topics_api.get_specific_posts_from_topic(
    api_key,
    api_username,
    id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Topic

```python
def get_topic(self,
             api_key,
             api_username,
             id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Header, Required | - |
| `api_username` | `str` | Header, Required | - |
| `id` | `str` | Template, Required | - |

## Response Type

**200**: specific posts

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TJsonResponse`](../../doc/models/t-json-response.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

id = 'id0'

result = topics_api.get_topic(
    api_key,
    api_username,
    id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Remove Topic

```python
def remove_topic(self,
                api_key,
                api_username,
                id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Header, Required | - |
| `api_username` | `str` | Header, Required | - |
| `id` | `str` | Template, Required | - |

## Response Type

**200**: specific posts

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

id = 'id0'

result = topics_api.remove_topic(
    api_key,
    api_username,
    id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Topic

```python
def update_topic(self,
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
| `body` | [`TJsonRequest`](../../doc/models/t-json-request.md) | Body, Optional | - |

## Response Type

**200**: topic updated

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TJsonResponse1`](../../doc/models/t-json-response-1.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

id = 'id0'

result = topics_api.update_topic(
    api_key,
    api_username,
    id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Invite to Topic

```python
def invite_to_topic(self,
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
| `body` | [`TInviteJsonRequest`](../../doc/models/t-invite-json-request.md) | Body, Optional | - |

## Response Type

**200**: topic updated

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TInviteJsonResponse`](../../doc/models/t-invite-json-response.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

id = 'id0'

result = topics_api.invite_to_topic(
    api_key,
    api_username,
    id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Invite Group to Topic

```python
def invite_group_to_topic(self,
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
| `body` | [`TInviteGroupJsonRequest`](../../doc/models/t-invite-group-json-request.md) | Body, Optional | - |

## Response Type

**200**: invites to a PM

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TInviteGroupJsonResponse`](../../doc/models/t-invite-group-json-response.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

id = 'id0'

result = topics_api.invite_group_to_topic(
    api_key,
    api_username,
    id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Bookmark Topic

```python
def bookmark_topic(self,
                  api_key,
                  api_username,
                  id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Header, Required | - |
| `api_username` | `str` | Header, Required | - |
| `id` | `str` | Template, Required | - |

## Response Type

**200**: topic updated

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

id = 'id0'

result = topics_api.bookmark_topic(
    api_key,
    api_username,
    id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Topic Status

```python
def update_topic_status(self,
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
| `body` | [`TStatusJsonRequest`](../../doc/models/t-status-json-request.md) | Body, Optional | - |

## Response Type

**200**: topic updated

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TStatusJsonResponse`](../../doc/models/t-status-json-response.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

id = 'id0'

body = TStatusJsonRequest(
    status=Status1.PINNED_GLOBALLY,
    enabled=Enabled.TRUE,
    until='2030-12-31'
)

result = topics_api.update_topic_status(
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


# List Latest Topics

```python
def list_latest_topics(self,
                      api_key,
                      api_username,
                      order=None,
                      ascending=None,
                      per_page=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Header, Required | - |
| `api_username` | `str` | Header, Required | - |
| `order` | `str` | Query, Optional | Enum: `default`, `created`, `activity`, `views`, `posts`, `category`,<br>`likes`, `op_likes`, `posters` |
| `ascending` | `str` | Query, Optional | Defaults to `desc`, add `ascending=true` to sort asc |
| `per_page` | `int` | Query, Optional | Maximum number of topics returned, between 1-100 |

## Response Type

**200**: topic updated

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`LatestJsonResponse`](../../doc/models/latest-json-response.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

result = topics_api.list_latest_topics(
    api_key,
    api_username
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Top Topics

```python
def list_top_topics(self,
                   api_key,
                   api_username,
                   period=None,
                   per_page=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Header, Required | - |
| `api_username` | `str` | Header, Required | - |
| `period` | `str` | Query, Optional | Enum: `all`, `yearly`, `quarterly`, `monthly`, `weekly`, `daily` |
| `per_page` | `int` | Query, Optional | Maximum number of topics returned, between 1-100 |

## Response Type

**200**: response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TopJsonResponse`](../../doc/models/top-json-response.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

result = topics_api.list_top_topics(
    api_key,
    api_username
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Set Notification Level

```python
def set_notification_level(self,
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
| `body` | [`TNotificationsJsonRequest`](../../doc/models/t-notifications-json-request.md) | Body, Optional | - |

## Response Type

**200**: topic updated

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TNotificationsJsonResponse`](../../doc/models/t-notifications-json-response.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

id = 'id0'

result = topics_api.set_notification_level(
    api_key,
    api_username,
    id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Topic Timestamp

```python
def update_topic_timestamp(self,
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
| `body` | [`TChangeTimestampJsonRequest`](../../doc/models/t-change-timestamp-json-request.md) | Body, Optional | - |

## Response Type

**200**: topic updated

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TChangeTimestampJsonResponse`](../../doc/models/t-change-timestamp-json-response.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

id = 'id0'

body = TChangeTimestampJsonRequest(
    timestamp='1594291380'
)

result = topics_api.update_topic_timestamp(
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


# Create Topic Timer

```python
def create_topic_timer(self,
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
| `body` | [`TTimerJsonRequest`](../../doc/models/t-timer-json-request.md) | Body, Optional | - |

## Response Type

**200**: topic updated

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TTimerJsonResponse`](../../doc/models/t-timer-json-response.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

id = 'id0'

result = topics_api.create_topic_timer(
    api_key,
    api_username,
    id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Topic by External Id

```python
def get_topic_by_external_id(self,
                            external_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `external_id` | `str` | Template, Required | - |

## Response Type

**200**

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
external_id = 'external_id6'

result = topics_api.get_topic_by_external_id(external_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

