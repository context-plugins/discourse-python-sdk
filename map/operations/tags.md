<!-- Generated file — do not edit; regenerated with the SDK. -->

# Tags — operations

Accessor: `client.tags` · Source: `discourse/apis/tags.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.tags.create_tag_group

- **Route**: `POST /tag_groups.json`
- **Signature**: `def create_tag_group(*, body: TagGroupsJsonRequest | TagGroupsJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TagGroupsJsonResponse1`
- **Returns (raw)**: `ApiResult[TagGroupsJsonResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TagGroupsJsonRequest` | `discourse/models/tag_groups_json_request.py` |
| `TagGroupsJsonRequestDict` | `discourse/models/tag_groups_json_request.py` |
| `TagGroupsJsonResponse1` | `discourse/models/tag_groups_json_response1.py` |

### client.tags.get_tag

- **Route**: `GET /tag/{name}.json`
- **Signature**: `def get_tag(name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `name`
- **Params**: `name` — path
- **Returns (parsed)**: `TagJsonResponse`
- **Returns (raw)**: `ApiResult[TagJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TagJsonResponse` | `discourse/models/tag_json_response.py` |

### client.tags.get_tag_group

- **Route**: `GET /tag_groups/{id}.json`
- **Signature**: `def get_tag_group(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `TagGroupsJsonResponse2`
- **Returns (raw)**: `ApiResult[TagGroupsJsonResponse2, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TagGroupsJsonResponse2` | `discourse/models/tag_groups_json_response2.py` |

### client.tags.list_tag_groups

- **Route**: `GET /tag_groups.json`
- **Signature**: `def list_tag_groups(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `TagGroupsJsonResponse`
- **Returns (raw)**: `ApiResult[TagGroupsJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TagGroupsJsonResponse` | `discourse/models/tag_groups_json_response.py` |

### client.tags.list_tags

- **Route**: `GET /tags.json`
- **Signature**: `def list_tags(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `TagsJsonResponse`
- **Returns (raw)**: `ApiResult[TagsJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TagsJsonResponse` | `discourse/models/tags_json_response.py` |

### client.tags.update_tag_group

- **Route**: `PUT /tag_groups/{id}.json`
- **Signature**: `def update_tag_group(id_: str, *, body: TagGroupsJsonRequest1 | TagGroupsJsonRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `TagGroupsJsonResponse3`
- **Returns (raw)**: `ApiResult[TagGroupsJsonResponse3, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TagGroupsJsonRequest1` | `discourse/models/tag_groups_json_request1.py` |
| `TagGroupsJsonRequest1Dict` | `discourse/models/tag_groups_json_request1.py` |
| `TagGroupsJsonResponse3` | `discourse/models/tag_groups_json_response3.py` |

