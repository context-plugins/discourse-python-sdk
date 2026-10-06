<!-- Generated file — do not edit; regenerated with the SDK. -->

# Posts — operations

Accessor: `client.posts` · Source: `discourse/apis/posts.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.posts.create_topic_post_pm

- **Route**: `POST /posts.json`
- **Signature**: `def create_topic_post_pm(api_key: str, api_username: str, *, body: PostsJsonRequest | PostsJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `api_key`, `api_username`
- **Params**: `api_key` — header `Api-Key` · `api_username` — header `Api-Username` · `body` — JSON body
- **Returns (parsed)**: `PostsJsonResponse1`
- **Returns (raw)**: `ApiResult[PostsJsonResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PostsJsonRequest` | `discourse/models/posts_json_request.py` |
| `PostsJsonRequestDict` | `discourse/models/posts_json_request.py` |
| `PostsJsonResponse1` | `discourse/models/posts_json_response1.py` |

### client.posts.delete_post

- **Route**: `DELETE /posts/{id}.json`
- **Signature**: `def delete_post(id_: int, api_key: str, api_username: str, *, body: PostsJsonRequest2 | PostsJsonRequest2Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`, `api_key`, `api_username`
- **Params**: `id_` — path `id` · `api_key` — header `Api-Key` · `api_username` — header `Api-Username` · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PostsJsonRequest2` | `discourse/models/posts_json_request2.py` |
| `PostsJsonRequest2Dict` | `discourse/models/posts_json_request2.py` |

### client.posts.get_post

- **Route**: `GET /posts/{id}.json`
- **Signature**: `def get_post(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `PostsJsonResponse2`
- **Returns (raw)**: `ApiResult[PostsJsonResponse2, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PostsJsonResponse2` | `discourse/models/posts_json_response2.py` |

### client.posts.list_posts

- **Route**: `GET /posts.json`
- **Signature**: `def list_posts(*, before: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `before` — query
- **Returns (parsed)**: `PostsJsonResponse`
- **Returns (raw)**: `ApiResult[PostsJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PostsJsonResponse` | `discourse/models/posts_json_response.py` |

### client.posts.lock_post

- **Route**: `PUT /posts/{id}/locked.json`
- **Signature**: `def lock_post(id_: str, api_key: str, api_username: str, *, body: PostsLockedJsonRequest | PostsLockedJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`, `api_key`, `api_username`
- **Params**: `id_` — path `id` · `api_key` — header `Api-Key` · `api_username` — header `Api-Username` · `body` — JSON body
- **Returns (parsed)**: `PostsLockedJsonResponse`
- **Returns (raw)**: `ApiResult[PostsLockedJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PostsLockedJsonRequest` | `discourse/models/posts_locked_json_request.py` |
| `PostsLockedJsonRequestDict` | `discourse/models/posts_locked_json_request.py` |
| `PostsLockedJsonResponse` | `discourse/models/posts_locked_json_response.py` |

### client.posts.perform_post_action

- **Route**: `POST /post_actions.json`
- **Signature**: `def perform_post_action(api_key: str, api_username: str, *, body: PostActionsJsonRequest | PostActionsJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `api_key`, `api_username`
- **Params**: `api_key` — header `Api-Key` · `api_username` — header `Api-Username` · `body` — JSON body
- **Returns (parsed)**: `PostActionsJsonResponse`
- **Returns (raw)**: `ApiResult[PostActionsJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PostActionsJsonRequest` | `discourse/models/post_actions_json_request.py` |
| `PostActionsJsonRequestDict` | `discourse/models/post_actions_json_request.py` |
| `PostActionsJsonResponse` | `discourse/models/post_actions_json_response.py` |

### client.posts.post_replies

- **Route**: `GET /posts/{id}/replies.json`
- **Signature**: `def post_replies(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `list[PostsRepliesJsonResponse]`
- **Returns (raw)**: `ApiResult[list[PostsRepliesJsonResponse], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PostsRepliesJsonResponse` | `discourse/models/posts_replies_json_response.py` |

### client.posts.update_post

- **Route**: `PUT /posts/{id}.json`
- **Signature**: `def update_post(id_: str, api_key: str, api_username: str, *, body: PostsJsonRequest1 | PostsJsonRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`, `api_key`, `api_username`
- **Params**: `id_` — path `id` · `api_key` — header `Api-Key` · `api_username` — header `Api-Username` · `body` — JSON body
- **Returns (parsed)**: `PostsJsonResponse3`
- **Returns (raw)**: `ApiResult[PostsJsonResponse3, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PostsJsonRequest1` | `discourse/models/posts_json_request1.py` |
| `PostsJsonRequest1Dict` | `discourse/models/posts_json_request1.py` |
| `PostsJsonResponse3` | `discourse/models/posts_json_response3.py` |

