<!-- Generated file — do not edit; regenerated with the SDK. -->

# Groups — operations

Accessor: `client.groups` · Source: `discourse/apis/groups.py` · 9 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.groups.add_group_members

- **Route**: `PUT /groups/{id}/members.json`
- **Signature**: `def add_group_members(id_: int, *, body: GroupsMembersJsonRequest | GroupsMembersJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `GroupsMembersJsonResponse1`
- **Returns (raw)**: `ApiResult[GroupsMembersJsonResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GroupsMembersJsonRequest` | `discourse/models/groups_members_json_request.py` |
| `GroupsMembersJsonRequestDict` | `discourse/models/groups_members_json_request.py` |
| `GroupsMembersJsonResponse1` | `discourse/models/groups_members_json_response1.py` |

### client.groups.create_group

- **Route**: `POST /admin/groups.json`
- **Signature**: `def create_group(*, body: AdminGroupsJsonRequest | AdminGroupsJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AdminGroupsJsonResponse`
- **Returns (raw)**: `ApiResult[AdminGroupsJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminGroupsJsonRequest` | `discourse/models/admin_groups_json_request.py` |
| `AdminGroupsJsonRequestDict` | `discourse/models/admin_groups_json_request.py` |
| `AdminGroupsJsonResponse` | `discourse/models/admin_groups_json_response.py` |

### client.groups.delete_group

- **Route**: `DELETE /admin/groups/{id}.json`
- **Signature**: `def delete_group(id_: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `AdminGroupsJsonResponse1`
- **Returns (raw)**: `ApiResult[AdminGroupsJsonResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminGroupsJsonResponse1` | `discourse/models/admin_groups_json_response1.py` |

### client.groups.get_group

- **Route**: `GET /groups/{name}.json`
- **Signature**: `def get_group(name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `name`
- **Params**: `name` — path
- **Returns (parsed)**: `GroupsJsonResponse`
- **Returns (raw)**: `ApiResult[GroupsJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GroupsJsonResponse` | `discourse/models/groups_json_response.py` |

### client.groups.get_group_by_id

- **Route**: `GET /groups/by-id/{id}.json`
- **Signature**: `def get_group_by_id(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `GroupsByIdJsonResponse`
- **Returns (raw)**: `ApiResult[GroupsByIdJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GroupsByIdJsonResponse` | `discourse/models/groups_by_id_json_response.py` |

### client.groups.list_group_members

- **Route**: `GET /groups/{name}/members.json`
- **Signature**: `def list_group_members(name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `name`
- **Params**: `name` — path
- **Returns (parsed)**: `GroupsMembersJsonResponse`
- **Returns (raw)**: `ApiResult[GroupsMembersJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GroupsMembersJsonResponse` | `discourse/models/groups_members_json_response.py` |

### client.groups.list_groups

- **Route**: `GET /groups.json`
- **Signature**: `def list_groups(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `GroupsJsonResponse2`
- **Returns (raw)**: `ApiResult[GroupsJsonResponse2, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GroupsJsonResponse2` | `discourse/models/groups_json_response2.py` |

### client.groups.remove_group_members

- **Route**: `DELETE /groups/{id}/members.json`
- **Signature**: `def remove_group_members(id_: int, *, body: GroupsMembersJsonRequest | GroupsMembersJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `GroupsMembersJsonResponse2`
- **Returns (raw)**: `ApiResult[GroupsMembersJsonResponse2, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GroupsMembersJsonRequest` | `discourse/models/groups_members_json_request.py` |
| `GroupsMembersJsonRequestDict` | `discourse/models/groups_members_json_request.py` |
| `GroupsMembersJsonResponse2` | `discourse/models/groups_members_json_response2.py` |

### client.groups.update_group

- **Route**: `PUT /groups/{id}.json`
- **Signature**: `def update_group(id_: int, *, body: GroupsJsonRequest | GroupsJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `GroupsJsonResponse1`
- **Returns (raw)**: `ApiResult[GroupsJsonResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GroupsJsonRequest` | `discourse/models/groups_json_request.py` |
| `GroupsJsonRequestDict` | `discourse/models/groups_json_request.py` |
| `GroupsJsonResponse1` | `discourse/models/groups_json_response1.py` |

