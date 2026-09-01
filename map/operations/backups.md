<!-- Generated file — do not edit; regenerated with the SDK. -->

# Backups — operations

Accessor: `client.backups` · Source: `discourse/apis/backups.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.backups.create_backup

- **Route**: `POST /admin/backups.json`
- **Signature**: `def create_backup(*, body: AdminBackupsJsonRequest | AdminBackupsJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AdminBackupsJsonResponse1`
- **Returns (raw)**: `ApiResult[AdminBackupsJsonResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminBackupsJsonRequest` | `discourse/models/admin_backups_json_request.py` |
| `AdminBackupsJsonRequestDict` | `discourse/models/admin_backups_json_request.py` |
| `AdminBackupsJsonResponse1` | `discourse/models/admin_backups_json_response1.py` |

### client.backups.download_backup

- **Route**: `GET /admin/backups/{filename}`
- **Signature**: `def download_backup(filename: str, token: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `filename`, `token`
- **Params**: `filename` — path · `token` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.backups.get_backups

- **Route**: `GET /admin/backups.json`
- **Signature**: `def get_backups(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[AdminBackupsJsonResponse]`
- **Returns (raw)**: `ApiResult[list[AdminBackupsJsonResponse], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdminBackupsJsonResponse` | `discourse/models/admin_backups_json_response.py` |

### client.backups.send_download_backup_email

- **Route**: `PUT /admin/backups/{filename}`
- **Signature**: `def send_download_backup_email(filename: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `filename`
- **Params**: `filename` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

