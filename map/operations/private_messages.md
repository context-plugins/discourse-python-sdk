<!-- Generated file — do not edit; regenerated with the SDK. -->

# PrivateMessages — operations

Accessor: `client.private_messages` · Source: `discourse/apis/private_messages.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.private_messages.create_topic_post_pm

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

### client.private_messages.get_user_sent_private_messages

- **Route**: `GET /topics/private-messages-sent/{username}.json`
- **Signature**: `def get_user_sent_private_messages(username: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `username`
- **Params**: `username` — path
- **Returns (parsed)**: `TopicsPrivateMessagesSentJsonResponse`
- **Returns (raw)**: `ApiResult[TopicsPrivateMessagesSentJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TopicsPrivateMessagesSentJsonResponse` | `discourse/models/topics_private_messages_sent_json_response.py` |

### client.private_messages.list_user_private_messages

- **Route**: `GET /topics/private-messages/{username}.json`
- **Signature**: `def list_user_private_messages(username: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `username`
- **Params**: `username` — path
- **Returns (parsed)**: `TopicsPrivateMessagesJsonResponse`
- **Returns (raw)**: `ApiResult[TopicsPrivateMessagesJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TopicsPrivateMessagesJsonResponse` | `discourse/models/topics_private_messages_json_response.py` |

