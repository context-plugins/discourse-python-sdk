<!-- Generated file — do not edit; regenerated with the SDK. -->

# Users — operations

Accessor: `client.users` · Source: `discourse/apis/users.py` · 25 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.users.activate_user

- **Route**: `PUT /admin/users/{id}/activate.json`
- **Signature**: `def activate_user(id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `AdminUsersActivateJsonResponse`
- **Returns (raw)**: `ApiResult[AdminUsersActivateJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminUsersActivateJsonResponse` | `discourse/models/admin_users_activate_json_response.py` |

### client.users.admin_get_user

- **Route**: `GET /admin/users/{id}.json`
- **Signature**: `def admin_get_user(id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `AdminUsersJsonResponse`
- **Returns (raw)**: `ApiResult[AdminUsersJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminUsersJsonResponse` | `discourse/models/admin_users_json_response.py` |

### client.users.admin_list_users

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

### client.users.admin_list_users_flag

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

### client.users.anonymize_user

- **Route**: `PUT /admin/users/{id}/anonymize.json`
- **Signature**: `def anonymize_user(id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `AdminUsersAnonymizeJsonResponse`
- **Returns (raw)**: `ApiResult[AdminUsersAnonymizeJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminUsersAnonymizeJsonResponse` | `discourse/models/admin_users_anonymize_json_response.py` |

### client.users.change_password

- **Route**: `PUT /users/password-reset/{token}.json`
- **Signature**: `def change_password(token: str, *, body: UsersPasswordResetJsonRequest | UsersPasswordResetJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`
- **Params**: `token` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UsersPasswordResetJsonRequest` | `discourse/models/users_password_reset_json_request.py` |
| `UsersPasswordResetJsonRequestDict` | `discourse/models/users_password_reset_json_request.py` |

### client.users.create_user

- **Route**: `POST /users.json`
- **Signature**: `def create_user(api_key: str, api_username: str, *, body: UsersJsonRequest | UsersJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `api_key`, `api_username`
- **Params**: `api_key` — header `Api-Key` · `api_username` — header `Api-Username` · `body` — JSON body
- **Returns (parsed)**: `UsersJsonResponse`
- **Returns (raw)**: `ApiResult[UsersJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UsersJsonRequest` | `discourse/models/users_json_request.py` |
| `UsersJsonRequestDict` | `discourse/models/users_json_request.py` |
| `UsersJsonResponse` | `discourse/models/users_json_response.py` |

### client.users.deactivate_user

- **Route**: `PUT /admin/users/{id}/deactivate.json`
- **Signature**: `def deactivate_user(id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `AdminUsersDeactivateJsonResponse`
- **Returns (raw)**: `ApiResult[AdminUsersDeactivateJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminUsersDeactivateJsonResponse` | `discourse/models/admin_users_deactivate_json_response.py` |

### client.users.delete_user

- **Route**: `DELETE /admin/users/{id}.json`
- **Signature**: `def delete_user(id: int, *, body: AdminUsersJsonRequest | AdminUsersJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `AdminUsersJsonResponse1`
- **Returns (raw)**: `ApiResult[AdminUsersJsonResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminUsersJsonRequest` | `discourse/models/admin_users_json_request.py` |
| `AdminUsersJsonRequestDict` | `discourse/models/admin_users_json_request.py` |
| `AdminUsersJsonResponse1` | `discourse/models/admin_users_json_response1.py` |

### client.users.get_user

- **Route**: `GET /u/{username}.json`
- **Signature**: `def get_user(username: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `username`, `api_key`, `api_username`
- **Params**: `username` — path · `api_key` — header `Api-Key` · `api_username` — header `Api-Username`
- **Returns (parsed)**: `UJsonResponse`
- **Returns (raw)**: `ApiResult[UJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UJsonResponse` | `discourse/models/u_json_response.py` |

### client.users.get_user_emails

- **Route**: `GET /u/{username}/emails.json`
- **Signature**: `def get_user_emails(username: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `username`
- **Params**: `username` — path
- **Returns (parsed)**: `UEmailsJsonResponse`
- **Returns (raw)**: `ApiResult[UEmailsJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UEmailsJsonResponse` | `discourse/models/u_emails_json_response.py` |

### client.users.get_user_external_id

- **Route**: `GET /u/by-external/{external_id}.json`
- **Signature**: `def get_user_external_id(external_id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `external_id`, `api_key`, `api_username`
- **Params**: `external_id` — path · `api_key` — header `Api-Key` · `api_username` — header `Api-Username`
- **Returns (parsed)**: `UByExternalJsonResponse`
- **Returns (raw)**: `ApiResult[UByExternalJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UByExternalJsonResponse` | `discourse/models/u_by_external_json_response.py` |

### client.users.get_user_identiy_provider_external_id

- **Route**: `GET /u/by-external/{provider}/{external_id}.json`
- **Signature**: `def get_user_identiy_provider_external_id(provider: str, external_id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `provider`, `external_id`, `api_key`, `api_username`
- **Params**: `provider` — path · `external_id` — path · `api_key` — header `Api-Key` · `api_username` — header `Api-Username`
- **Returns (parsed)**: `UByExternalJsonResponse`
- **Returns (raw)**: `ApiResult[UByExternalJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UByExternalJsonResponse` | `discourse/models/u_by_external_json_response.py` |

### client.users.list_user_actions

- **Route**: `GET /user_actions.json`
- **Signature**: `def list_user_actions(offset: int, username: str, filter: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `offset`, `username`, `filter`
- **Params**: `offset` — query · `username` — query · `filter` — query
- **Returns (parsed)**: `UserActionsJsonResponse`
- **Returns (raw)**: `ApiResult[UserActionsJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserActionsJsonResponse` | `discourse/models/user_actions_json_response.py` |

### client.users.list_user_badges

- **Route**: `GET /user-badges/{username}.json`
- **Signature**: `def list_user_badges(username: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `username`
- **Params**: `username` — path
- **Returns (parsed)**: `UserBadgesJsonResponse`
- **Returns (raw)**: `ApiResult[UserBadgesJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UserBadgesJsonResponse` | `discourse/models/user_badges_json_response.py` |

### client.users.list_users_public

- **Route**: `GET /directory_items.json`
- **Signature**: `def list_users_public(period: Period1OrStr, order: Order2OrStr, *, asc: AscOrStr | None = None, page: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `period`, `order`
- **Params**: `period` — query · `order` — query · `asc` — query · `page` — query
- **Returns (parsed)**: `DirectoryItemsJsonResponse`
- **Returns (raw)**: `ApiResult[DirectoryItemsJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Period1OrStr` | `discourse/models/enums/period1.py` |
| `Order2OrStr` | `discourse/models/enums/order2.py` |
| `AscOrStr` | `discourse/models/enums/asc.py` |
| `DirectoryItemsJsonResponse` | `discourse/models/directory_items_json_response.py` |

### client.users.log_out_user

- **Route**: `POST /admin/users/{id}/log_out.json`
- **Signature**: `def log_out_user(id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `AdminUsersLogOutJsonResponse`
- **Returns (raw)**: `ApiResult[AdminUsersLogOutJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminUsersLogOutJsonResponse` | `discourse/models/admin_users_log_out_json_response.py` |

### client.users.refresh_gravatar

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

### client.users.send_password_reset_email

- **Route**: `POST /session/forgot_password.json`
- **Signature**: `def send_password_reset_email(*, body: SessionForgotPasswordJsonRequest | SessionForgotPasswordJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SessionForgotPasswordJsonResponse`
- **Returns (raw)**: `ApiResult[SessionForgotPasswordJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SessionForgotPasswordJsonRequest` | `discourse/models/session_forgot_password_json_request.py` |
| `SessionForgotPasswordJsonRequestDict` | `discourse/models/session_forgot_password_json_request.py` |
| `SessionForgotPasswordJsonResponse` | `discourse/models/session_forgot_password_json_response.py` |

### client.users.silence_user

- **Route**: `PUT /admin/users/{id}/silence.json`
- **Signature**: `def silence_user(id: int, *, body: AdminUsersSilenceJsonRequest | AdminUsersSilenceJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `AdminUsersSilenceJsonResponse`
- **Returns (raw)**: `ApiResult[AdminUsersSilenceJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminUsersSilenceJsonRequest` | `discourse/models/admin_users_silence_json_request.py` |
| `AdminUsersSilenceJsonRequestDict` | `discourse/models/admin_users_silence_json_request.py` |
| `AdminUsersSilenceJsonResponse` | `discourse/models/admin_users_silence_json_response.py` |

### client.users.suspend_user

- **Route**: `PUT /admin/users/{id}/suspend.json`
- **Signature**: `def suspend_user(id: int, *, body: AdminUsersSuspendJsonRequest | AdminUsersSuspendJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `AdminUsersSuspendJsonResponse`
- **Returns (raw)**: `ApiResult[AdminUsersSuspendJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminUsersSuspendJsonRequest` | `discourse/models/admin_users_suspend_json_request.py` |
| `AdminUsersSuspendJsonRequestDict` | `discourse/models/admin_users_suspend_json_request.py` |
| `AdminUsersSuspendJsonResponse` | `discourse/models/admin_users_suspend_json_response.py` |

### client.users.update_avatar

- **Route**: `PUT /u/{username}/preferences/avatar/pick.json`
- **Signature**: `def update_avatar(username: str, *, body: UPreferencesAvatarPickJsonRequest | UPreferencesAvatarPickJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `username`
- **Params**: `username` — path · `body` — JSON body
- **Returns (parsed)**: `UPreferencesAvatarPickJsonResponse`
- **Returns (raw)**: `ApiResult[UPreferencesAvatarPickJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UPreferencesAvatarPickJsonRequest` | `discourse/models/u_preferences_avatar_pick_json_request.py` |
| `UPreferencesAvatarPickJsonRequestDict` | `discourse/models/u_preferences_avatar_pick_json_request.py` |
| `UPreferencesAvatarPickJsonResponse` | `discourse/models/u_preferences_avatar_pick_json_response.py` |

### client.users.update_email

- **Route**: `PUT /u/{username}/preferences/email.json`
- **Signature**: `def update_email(username: str, *, body: UPreferencesEmailJsonRequest | UPreferencesEmailJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `username`
- **Params**: `username` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UPreferencesEmailJsonRequest` | `discourse/models/u_preferences_email_json_request.py` |
| `UPreferencesEmailJsonRequestDict` | `discourse/models/u_preferences_email_json_request.py` |

### client.users.update_user

- **Route**: `PUT /u/{username}.json`
- **Signature**: `def update_user(username: str, api_key: str, api_username: str, *, body: UJsonRequest | UJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `username`, `api_key`, `api_username`
- **Params**: `username` — path · `api_key` — header `Api-Key` · `api_username` — header `Api-Username` · `body` — JSON body
- **Returns (parsed)**: `UJsonResponse1`
- **Returns (raw)**: `ApiResult[UJsonResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UJsonRequest` | `discourse/models/u_json_request.py` |
| `UJsonRequestDict` | `discourse/models/u_json_request.py` |
| `UJsonResponse1` | `discourse/models/u_json_response1.py` |

### client.users.update_username

- **Route**: `PUT /u/{username}/preferences/username.json`
- **Signature**: `def update_username(username: str, *, body: UPreferencesUsernameJsonRequest | UPreferencesUsernameJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `username`
- **Params**: `username` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UPreferencesUsernameJsonRequest` | `discourse/models/u_preferences_username_json_request.py` |
| `UPreferencesUsernameJsonRequestDict` | `discourse/models/u_preferences_username_json_request.py` |

