<!-- Generated file — do not edit; regenerated with the SDK. -->

# Topics — operations

Accessor: `client.topics` · Source: `discourse_api_documentation/apis/topics.py` · 15 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.topics.bookmark_topic

- **Route**: `PUT /t/{id}/bookmark.json`
- **Signature**: `def bookmark_topic(id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `api_key`, `api_username`
- **Params**: `id` — path · `api_key` — header `Api-Key` · `api_username` — header `Api-Username`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.topics.create_topic_post_pm

- **Route**: `POST /posts.json`
- **Signature**: `def create_topic_post_pm(api_key: str, api_username: str, *, body: PostsJsonRequest | PostsJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `api_key`, `api_username`
- **Params**: `api_key` — header `Api-Key` · `api_username` — header `Api-Username` · `body` — JSON body
- **Returns (parsed)**: `PostsJsonResponse1`
- **Returns (raw)**: `ApiResult[PostsJsonResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PostsJsonRequest` | `discourse_api_documentation/models/posts_json_request.py` |
| `PostsJsonRequestDict` | `discourse_api_documentation/models/posts_json_request.py` |
| `PostsJsonResponse1` | `discourse_api_documentation/models/posts_json_response1.py` |

### client.topics.create_topic_timer

- **Route**: `POST /t/{id}/timer.json`
- **Signature**: `def create_topic_timer(id: str, api_key: str, api_username: str, *, body: TTimerJsonRequest | TTimerJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `api_key`, `api_username`
- **Params**: `id` — path · `api_key` — header `Api-Key` · `api_username` — header `Api-Username` · `body` — JSON body
- **Returns (parsed)**: `TTimerJsonResponse`
- **Returns (raw)**: `ApiResult[TTimerJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TTimerJsonRequest` | `discourse_api_documentation/models/t_timer_json_request.py` |
| `TTimerJsonRequestDict` | `discourse_api_documentation/models/t_timer_json_request.py` |
| `TTimerJsonResponse` | `discourse_api_documentation/models/t_timer_json_response.py` |

### client.topics.get_specific_posts_from_topic

- **Route**: `GET /t/{id}/posts.json`
- **Signature**: `def get_specific_posts_from_topic(id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `api_key`, `api_username`
- **Params**: `id` — path · `api_key` — header `Api-Key` · `api_username` — header `Api-Username`
- **Returns (parsed)**: `TPostsJsonResponse`
- **Returns (raw)**: `ApiResult[TPostsJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TPostsJsonResponse` | `discourse_api_documentation/models/t_posts_json_response.py` |

### client.topics.get_topic

- **Route**: `GET /t/{id}.json`
- **Signature**: `def get_topic(id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `api_key`, `api_username`
- **Params**: `id` — path · `api_key` — header `Api-Key` · `api_username` — header `Api-Username`
- **Returns (parsed)**: `TJsonResponse`
- **Returns (raw)**: `ApiResult[TJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TJsonResponse` | `discourse_api_documentation/models/t_json_response.py` |

### client.topics.get_topic_by_external_id

- **Route**: `GET /t/external_id/{external_id}.json`
- **Signature**: `def get_topic_by_external_id(external_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `external_id`
- **Params**: `external_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.topics.invite_group_to_topic

- **Route**: `POST /t/{id}/invite-group.json`
- **Signature**: `def invite_group_to_topic(id: str, api_key: str, api_username: str, *, body: TInviteGroupJsonRequest | TInviteGroupJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `api_key`, `api_username`
- **Params**: `id` — path · `api_key` — header `Api-Key` · `api_username` — header `Api-Username` · `body` — JSON body
- **Returns (parsed)**: `TInviteGroupJsonResponse`
- **Returns (raw)**: `ApiResult[TInviteGroupJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TInviteGroupJsonRequest` | `discourse_api_documentation/models/t_invite_group_json_request.py` |
| `TInviteGroupJsonRequestDict` | `discourse_api_documentation/models/t_invite_group_json_request.py` |
| `TInviteGroupJsonResponse` | `discourse_api_documentation/models/t_invite_group_json_response.py` |

### client.topics.invite_to_topic

- **Route**: `POST /t/{id}/invite.json`
- **Signature**: `def invite_to_topic(id: str, api_key: str, api_username: str, *, body: TInviteJsonRequest | TInviteJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `api_key`, `api_username`
- **Params**: `id` — path · `api_key` — header `Api-Key` · `api_username` — header `Api-Username` · `body` — JSON body
- **Returns (parsed)**: `TInviteJsonResponse`
- **Returns (raw)**: `ApiResult[TInviteJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TInviteJsonRequest` | `discourse_api_documentation/models/t_invite_json_request.py` |
| `TInviteJsonRequestDict` | `discourse_api_documentation/models/t_invite_json_request.py` |
| `TInviteJsonResponse` | `discourse_api_documentation/models/t_invite_json_response.py` |

### client.topics.list_latest_topics

- **Route**: `GET /latest.json`
- **Signature**: `def list_latest_topics(api_key: str, api_username: str, *, order: str | None = None, ascending: str | None = None, per_page: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `api_key`, `api_username`
- **Params**: `order` — query · `ascending` — query · `per_page` — query · `api_key` — header `Api-Key` · `api_username` — header `Api-Username`
- **Returns (parsed)**: `LatestJsonResponse`
- **Returns (raw)**: `ApiResult[LatestJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LatestJsonResponse` | `discourse_api_documentation/models/latest_json_response.py` |

### client.topics.list_top_topics

- **Route**: `GET /top.json`
- **Signature**: `def list_top_topics(api_key: str, api_username: str, *, period: str | None = None, per_page: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `api_key`, `api_username`
- **Params**: `period` — query · `per_page` — query · `api_key` — header `Api-Key` · `api_username` — header `Api-Username`
- **Returns (parsed)**: `TopJsonResponse`
- **Returns (raw)**: `ApiResult[TopJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TopJsonResponse` | `discourse_api_documentation/models/top_json_response.py` |

### client.topics.remove_topic

- **Route**: `DELETE /t/{id}.json`
- **Signature**: `def remove_topic(id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `api_key`, `api_username`
- **Params**: `id` — path · `api_key` — header `Api-Key` · `api_username` — header `Api-Username`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.topics.set_notification_level

- **Route**: `POST /t/{id}/notifications.json`
- **Signature**: `def set_notification_level(id: str, api_key: str, api_username: str, *, body: TNotificationsJsonRequest | TNotificationsJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `api_key`, `api_username`
- **Params**: `id` — path · `api_key` — header `Api-Key` · `api_username` — header `Api-Username` · `body` — JSON body
- **Returns (parsed)**: `TNotificationsJsonResponse`
- **Returns (raw)**: `ApiResult[TNotificationsJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TNotificationsJsonRequest` | `discourse_api_documentation/models/t_notifications_json_request.py` |
| `TNotificationsJsonRequestDict` | `discourse_api_documentation/models/t_notifications_json_request.py` |
| `TNotificationsJsonResponse` | `discourse_api_documentation/models/t_notifications_json_response.py` |

### client.topics.update_topic

- **Route**: `PUT /t/-/{id}.json`
- **Signature**: `def update_topic(id: str, api_key: str, api_username: str, *, body: TJsonRequest | TJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `api_key`, `api_username`
- **Params**: `id` — path · `api_key` — header `Api-Key` · `api_username` — header `Api-Username` · `body` — JSON body
- **Returns (parsed)**: `TJsonResponse1`
- **Returns (raw)**: `ApiResult[TJsonResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TJsonRequest` | `discourse_api_documentation/models/t_json_request.py` |
| `TJsonRequestDict` | `discourse_api_documentation/models/t_json_request.py` |
| `TJsonResponse1` | `discourse_api_documentation/models/t_json_response1.py` |

### client.topics.update_topic_status

- **Route**: `PUT /t/{id}/status.json`
- **Signature**: `def update_topic_status(id: str, api_key: str, api_username: str, *, body: TStatusJsonRequest | TStatusJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `api_key`, `api_username`
- **Params**: `id` — path · `api_key` — header `Api-Key` · `api_username` — header `Api-Username` · `body` — JSON body
- **Returns (parsed)**: `TStatusJsonResponse`
- **Returns (raw)**: `ApiResult[TStatusJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TStatusJsonRequest` | `discourse_api_documentation/models/t_status_json_request.py` |
| `TStatusJsonRequestDict` | `discourse_api_documentation/models/t_status_json_request.py` |
| `TStatusJsonResponse` | `discourse_api_documentation/models/t_status_json_response.py` |

### client.topics.update_topic_timestamp

- **Route**: `PUT /t/{id}/change-timestamp.json`
- **Signature**: `def update_topic_timestamp(id: str, api_key: str, api_username: str, *, body: TChangeTimestampJsonRequest | TChangeTimestampJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `api_key`, `api_username`
- **Params**: `id` — path · `api_key` — header `Api-Key` · `api_username` — header `Api-Username` · `body` — JSON body
- **Returns (parsed)**: `TChangeTimestampJsonResponse`
- **Returns (raw)**: `ApiResult[TChangeTimestampJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TChangeTimestampJsonRequest` | `discourse_api_documentation/models/t_change_timestamp_json_request.py` |
| `TChangeTimestampJsonRequestDict` | `discourse_api_documentation/models/t_change_timestamp_json_request.py` |
| `TChangeTimestampJsonResponse` | `discourse_api_documentation/models/t_change_timestamp_json_response.py` |

