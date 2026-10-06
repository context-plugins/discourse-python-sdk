<!-- Generated file — do not edit; regenerated with the SDK. -->

# Admin — operations

Accessor: `client.admin` · Source: `discourse/apis/admin.py` · 11 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.admin.activate_user

- **Route**: `PUT /admin/users/{id}/activate.json`
- **Signature**: `def activate_user(id_: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `AdminUsersActivateJsonResponse`
- **Returns (raw)**: `ApiResult[AdminUsersActivateJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminUsersActivateJsonResponse` | `discourse/models/admin_users_activate_json_response.py` |

### client.admin.admin_get_user

- **Route**: `GET /admin/users/{id}.json`
- **Signature**: `def admin_get_user(id_: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `AdminUsersJsonResponse`
- **Returns (raw)**: `ApiResult[AdminUsersJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminUsersJsonResponse` | `discourse/models/admin_users_json_response.py` |

### client.admin.admin_list_users

- **Route**: `GET /admin/users.json`
- **Signature**: `def admin_list_users(*, order: Order3OrStr | None = None, asc: AscOrStr | None = None, page: int | None = None, show_emails: bool | None = None, stats: bool | None = None, email: str | None = None, ip: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `order` — query · `asc` — query · `page` — query · `show_emails` — query · `stats` — query · `email` — query · `ip` — query
- **Returns (parsed)**: `list[AdminUsersJsonResponse2]`
- **Returns (raw)**: `ApiResult[list[AdminUsersJsonResponse2], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Order3OrStr` | `discourse/models/enums/order3.py` |
| `AscOrStr` | `discourse/models/enums/asc.py` |
| `AdminUsersJsonResponse2` | `discourse/models/admin_users_json_response2.py` |

### client.admin.admin_list_users_flag

- **Route**: `GET /admin/users/list/{flag}.json`
- **Signature**: `def admin_list_users_flag(flag: FlagOrStr, *, order: Order3OrStr | None = None, asc: AscOrStr | None = None, page: int | None = None, show_emails: bool | None = None, stats: bool | None = None, email: str | None = None, ip: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `flag`
- **Params**: `flag` — path · `order` — query · `asc` — query · `page` — query · `show_emails` — query · `stats` — query · `email` — query · `ip` — query
- **Returns (parsed)**: `list[AdminUsersListJsonResponse]`
- **Returns (raw)**: `ApiResult[list[AdminUsersListJsonResponse], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FlagOrStr` | `discourse/models/enums/flag.py` |
| `Order3OrStr` | `discourse/models/enums/order3.py` |
| `AscOrStr` | `discourse/models/enums/asc.py` |
| `AdminUsersListJsonResponse` | `discourse/models/admin_users_list_json_response.py` |

### client.admin.anonymize_user

- **Route**: `PUT /admin/users/{id}/anonymize.json`
- **Signature**: `def anonymize_user(id_: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `AdminUsersAnonymizeJsonResponse`
- **Returns (raw)**: `ApiResult[AdminUsersAnonymizeJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminUsersAnonymizeJsonResponse` | `discourse/models/admin_users_anonymize_json_response.py` |

### client.admin.deactivate_user

- **Route**: `PUT /admin/users/{id}/deactivate.json`
- **Signature**: `def deactivate_user(id_: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `AdminUsersDeactivateJsonResponse`
- **Returns (raw)**: `ApiResult[AdminUsersDeactivateJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminUsersDeactivateJsonResponse` | `discourse/models/admin_users_deactivate_json_response.py` |

### client.admin.delete_user

- **Route**: `DELETE /admin/users/{id}.json`
- **Signature**: `def delete_user(id_: int, *, body: AdminUsersJsonRequest | AdminUsersJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `AdminUsersJsonResponse1`
- **Returns (raw)**: `ApiResult[AdminUsersJsonResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminUsersJsonRequest` | `discourse/models/admin_users_json_request.py` |
| `AdminUsersJsonRequestDict` | `discourse/models/admin_users_json_request.py` |
| `AdminUsersJsonResponse1` | `discourse/models/admin_users_json_response1.py` |

### client.admin.log_out_user

- **Route**: `POST /admin/users/{id}/log_out.json`
- **Signature**: `def log_out_user(id_: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `AdminUsersLogOutJsonResponse`
- **Returns (raw)**: `ApiResult[AdminUsersLogOutJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminUsersLogOutJsonResponse` | `discourse/models/admin_users_log_out_json_response.py` |

### client.admin.refresh_gravatar

- **Route**: `POST /user_avatar/{username}/refresh_gravatar.json`
- **Signature**: `def refresh_gravatar(username: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `username`
- **Params**: `username` — path
- **Returns (parsed)**: `UserAvatarRefreshGravatarJsonResponse`
- **Returns (raw)**: `ApiResult[UserAvatarRefreshGravatarJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserAvatarRefreshGravatarJsonResponse` | `discourse/models/user_avatar_refresh_gravatar_json_response.py` |

### client.admin.silence_user

- **Route**: `PUT /admin/users/{id}/silence.json`
- **Signature**: `def silence_user(id_: int, *, body: AdminUsersSilenceJsonRequest | AdminUsersSilenceJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `AdminUsersSilenceJsonResponse`
- **Returns (raw)**: `ApiResult[AdminUsersSilenceJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminUsersSilenceJsonRequest` | `discourse/models/admin_users_silence_json_request.py` |
| `AdminUsersSilenceJsonRequestDict` | `discourse/models/admin_users_silence_json_request.py` |
| `AdminUsersSilenceJsonResponse` | `discourse/models/admin_users_silence_json_response.py` |

### client.admin.suspend_user

- **Route**: `PUT /admin/users/{id}/suspend.json`
- **Signature**: `def suspend_user(id_: int, *, body: AdminUsersSuspendJsonRequest | AdminUsersSuspendJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `AdminUsersSuspendJsonResponse`
- **Returns (raw)**: `ApiResult[AdminUsersSuspendJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminUsersSuspendJsonRequest` | `discourse/models/admin_users_suspend_json_request.py` |
| `AdminUsersSuspendJsonRequestDict` | `discourse/models/admin_users_suspend_json_request.py` |
| `AdminUsersSuspendJsonResponse` | `discourse/models/admin_users_suspend_json_response.py` |

