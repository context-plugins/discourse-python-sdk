<!-- Generated file — do not edit; regenerated with the SDK. -->

# DiscourseCalendarEvents — operations

Accessor: `client.discourse_calendar_events` · Source: `discourse/apis/discourse_calendar_events.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.discourse_calendar_events.export_events_ics

- **Route**: `GET /discourse-post-event/events.ics`
- **Signature**: `def export_events_ics(*, category_id: int | None = None, include_subcategories: IncludeSubcategoriesOrStr | None = None, attending_user: str | None = None, before: RFC3339DateTime | None = None, after: RFC3339DateTime | None = None, order: OrderOrStr | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `category_id` — query · `include_subcategories` — query · `attending_user` — query · `before` — query · `after` — query · `order` — query · `limit` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncludeSubcategoriesOrStr` | `discourse/models/enums/include_subcategories.py` |
| `OrderOrStr` | `discourse/models/enums/order.py` |

### client.discourse_calendar_events.list_events

- **Route**: `GET /discourse-post-event/events.json`
- **Signature**: `def list_events(*, include_details: IncludeDetailsOrStr | None = None, category_id: int | None = None, include_subcategories: IncludeSubcategoriesOrStr | None = None, post_id: int | None = None, attending_user: str | None = None, before: RFC3339DateTime | None = None, after: RFC3339DateTime | None = None, order: OrderOrStr | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `include_details` — query · `category_id` — query · `include_subcategories` — query · `post_id` — query · `attending_user` — query · `before` — query · `after` — query · `order` — query · `limit` — query
- **Returns (parsed)**: `DiscoursePostEventEventsJsonResponse`
- **Returns (raw)**: `ApiResult[DiscoursePostEventEventsJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncludeDetailsOrStr` | `discourse/models/enums/include_details.py` |
| `IncludeSubcategoriesOrStr` | `discourse/models/enums/include_subcategories.py` |
| `OrderOrStr` | `discourse/models/enums/order.py` |
| `DiscoursePostEventEventsJsonResponse` | `discourse/models/discourse_post_event_events_json_response.py` |

