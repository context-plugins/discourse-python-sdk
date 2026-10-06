<!-- Generated file — do not edit; regenerated with the SDK. -->

# Invites — operations

Accessor: `client.invites` · Source: `discourse/apis/invites.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.invites.create_invite

- **Route**: `POST /invites.json`
- **Signature**: `def create_invite(api_key: str, api_username: str, *, body: InvitesJsonRequest | InvitesJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `api_key`, `api_username`
- **Params**: `api_key` — header `Api-Key` · `api_username` — header `Api-Username` · `body` — JSON body
- **Returns (parsed)**: `InvitesJsonResponse`
- **Returns (raw)**: `ApiResult[InvitesJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InvitesJsonRequest` | `discourse/models/invites_json_request.py` |
| `InvitesJsonRequestDict` | `discourse/models/invites_json_request.py` |
| `InvitesJsonResponse` | `discourse/models/invites_json_response.py` |

### client.invites.create_multiple_invites

- **Route**: `POST /invites/create-multiple.json`
- **Signature**: `def create_multiple_invites(api_key: str, api_username: str, *, body: InvitesCreateMultipleJsonRequest | InvitesCreateMultipleJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `api_key`, `api_username`
- **Params**: `api_key` — header `Api-Key` · `api_username` — header `Api-Username` · `body` — JSON body
- **Returns (parsed)**: `InvitesCreateMultipleJsonResponse`
- **Returns (raw)**: `ApiResult[InvitesCreateMultipleJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InvitesCreateMultipleJsonRequest` | `discourse/models/invites_create_multiple_json_request.py` |
| `InvitesCreateMultipleJsonRequestDict` | `discourse/models/invites_create_multiple_json_request.py` |
| `InvitesCreateMultipleJsonResponse` | `discourse/models/invites_create_multiple_json_response.py` |

### client.invites.invite_group_to_topic

- **Route**: `POST /t/{id}/invite-group.json`
- **Signature**: `def invite_group_to_topic(id_: str, api_key: str, api_username: str, *, body: TInviteGroupJsonRequest | TInviteGroupJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`, `api_key`, `api_username`
- **Params**: `id_` — path `id` · `api_key` — header `Api-Key` · `api_username` — header `Api-Username` · `body` — JSON body
- **Returns (parsed)**: `TInviteGroupJsonResponse`
- **Returns (raw)**: `ApiResult[TInviteGroupJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TInviteGroupJsonRequest` | `discourse/models/t_invite_group_json_request.py` |
| `TInviteGroupJsonRequestDict` | `discourse/models/t_invite_group_json_request.py` |
| `TInviteGroupJsonResponse` | `discourse/models/t_invite_group_json_response.py` |

### client.invites.invite_to_topic

- **Route**: `POST /t/{id}/invite.json`
- **Signature**: `def invite_to_topic(id_: str, api_key: str, api_username: str, *, body: TInviteJsonRequest | TInviteJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`, `api_key`, `api_username`
- **Params**: `id_` — path `id` · `api_key` — header `Api-Key` · `api_username` — header `Api-Username` · `body` — JSON body
- **Returns (parsed)**: `TInviteJsonResponse`
- **Returns (raw)**: `ApiResult[TInviteJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TInviteJsonRequest` | `discourse/models/t_invite_json_request.py` |
| `TInviteJsonRequestDict` | `discourse/models/t_invite_json_request.py` |
| `TInviteJsonResponse` | `discourse/models/t_invite_json_response.py` |

