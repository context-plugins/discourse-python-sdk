<!-- Generated file — do not edit; regenerated with the SDK. -->

# Notifications — operations

Accessor: `client.notifications` · Source: `discourse/apis/notifications.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.notifications.get_notifications

- **Route**: `GET /notifications.json`
- **Signature**: `def get_notifications(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `NotificationsJsonResponse`
- **Returns (raw)**: `ApiResult[NotificationsJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NotificationsJsonResponse` | `discourse/models/notifications_json_response.py` |

### client.notifications.mark_notifications_as_read

- **Route**: `PUT /notifications/mark-read.json`
- **Signature**: `def mark_notifications_as_read(*, body: NotificationsMarkReadJsonRequest | NotificationsMarkReadJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `NotificationsMarkReadJsonResponse`
- **Returns (raw)**: `ApiResult[NotificationsMarkReadJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `NotificationsMarkReadJsonRequest` | `discourse/models/notifications_mark_read_json_request.py` |
| `NotificationsMarkReadJsonRequestDict` | `discourse/models/notifications_mark_read_json_request.py` |
| `NotificationsMarkReadJsonResponse` | `discourse/models/notifications_mark_read_json_response.py` |

