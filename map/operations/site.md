<!-- Generated file — do not edit; regenerated with the SDK. -->

# Site — operations

Accessor: `client.site` · Source: `discourse/apis/site.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.site.get_site

- **Route**: `GET /site.json`
- **Signature**: `def get_site(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `SiteJsonResponse`
- **Returns (raw)**: `ApiResult[SiteJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SiteJsonResponse` | `discourse/models/site_json_response.py` |

### client.site.get_site_basic_info

- **Route**: `GET /site/basic-info.json`
- **Signature**: `def get_site_basic_info(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `SiteBasicInfoJsonResponse`
- **Returns (raw)**: `ApiResult[SiteBasicInfoJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SiteBasicInfoJsonResponse` | `discourse/models/site_basic_info_json_response.py` |

