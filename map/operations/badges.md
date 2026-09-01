<!-- Generated file — do not edit; regenerated with the SDK. -->

# Badges — operations

Accessor: `client.badges` · Source: `discourse_api_documentation/apis/badges.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.badges.admin_list_badges

- **Route**: `GET /admin/badges.json`
- **Signature**: `def admin_list_badges(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `AdminBadgesJsonResponse`
- **Returns (raw)**: `ApiResult[AdminBadgesJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminBadgesJsonResponse` | `discourse_api_documentation/models/admin_badges_json_response.py` |

### client.badges.create_badge

- **Route**: `POST /admin/badges.json`
- **Signature**: `def create_badge(*, body: AdminBadgesJsonRequest | AdminBadgesJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AdminBadgesJsonResponse1`
- **Returns (raw)**: `ApiResult[AdminBadgesJsonResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminBadgesJsonRequest` | `discourse_api_documentation/models/admin_badges_json_request.py` |
| `AdminBadgesJsonRequestDict` | `discourse_api_documentation/models/admin_badges_json_request.py` |
| `AdminBadgesJsonResponse1` | `discourse_api_documentation/models/admin_badges_json_response1.py` |

### client.badges.delete_badge

- **Route**: `DELETE /admin/badges/{id}.json`
- **Signature**: `def delete_badge(id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.badges.list_user_badges

- **Route**: `GET /user-badges/{username}.json`
- **Signature**: `def list_user_badges(username: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `username`
- **Params**: `username` — path
- **Returns (parsed)**: `UserBadgesJsonResponse`
- **Returns (raw)**: `ApiResult[UserBadgesJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserBadgesJsonResponse` | `discourse_api_documentation/models/user_badges_json_response.py` |

### client.badges.update_badge

- **Route**: `PUT /admin/badges/{id}.json`
- **Signature**: `def update_badge(id: int, *, body: AdminBadgesJsonRequest1 | AdminBadgesJsonRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `AdminBadgesJsonResponse2`
- **Returns (raw)**: `ApiResult[AdminBadgesJsonResponse2, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminBadgesJsonRequest1` | `discourse_api_documentation/models/admin_badges_json_request1.py` |
| `AdminBadgesJsonRequest1Dict` | `discourse_api_documentation/models/admin_badges_json_request1.py` |
| `AdminBadgesJsonResponse2` | `discourse_api_documentation/models/admin_badges_json_response2.py` |

