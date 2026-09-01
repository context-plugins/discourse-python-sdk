<!-- Generated file — do not edit; regenerated with the SDK. -->

# Categories — operations

Accessor: `client.categories` · Source: `discourse/apis/categories.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.categories.create_category

- **Route**: `POST /categories.json`
- **Signature**: `def create_category(*, body: CategoriesJsonRequest | CategoriesJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CategoriesJsonResponse`
- **Returns (raw)**: `ApiResult[CategoriesJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CategoriesJsonRequest` | `discourse/models/categories_json_request.py` |
| `CategoriesJsonRequestDict` | `discourse/models/categories_json_request.py` |
| `CategoriesJsonResponse` | `discourse/models/categories_json_response.py` |

### client.categories.get_category

- **Route**: `GET /c/{id}/show.json`
- **Signature**: `def get_category(id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `CShowJsonResponse`
- **Returns (raw)**: `ApiResult[CShowJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CShowJsonResponse` | `discourse/models/c_show_json_response.py` |

### client.categories.get_site

- **Route**: `GET /site.json`
- **Signature**: `def get_site(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `SiteJsonResponse`
- **Returns (raw)**: `ApiResult[SiteJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SiteJsonResponse` | `discourse/models/site_json_response.py` |

### client.categories.list_categories

- **Route**: `GET /categories.json`
- **Signature**: `def list_categories(*, include_subcategories: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `include_subcategories` — query
- **Returns (parsed)**: `CategoriesJsonResponse1`
- **Returns (raw)**: `ApiResult[CategoriesJsonResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CategoriesJsonResponse1` | `discourse/models/categories_json_response1.py` |

### client.categories.list_category_topics

- **Route**: `GET /c/{slug}/{id}.json`
- **Signature**: `def list_category_topics(slug: str, id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `slug`, `id`
- **Params**: `slug` — path · `id` — path
- **Returns (parsed)**: `CJsonResponse`
- **Returns (raw)**: `ApiResult[CJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CJsonResponse` | `discourse/models/c_json_response.py` |

### client.categories.update_category

- **Route**: `PUT /categories/{id}.json`
- **Signature**: `def update_category(id: int, *, body: CategoriesJsonRequest1 | CategoriesJsonRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `CategoriesJsonResponse2`
- **Returns (raw)**: `ApiResult[CategoriesJsonResponse2, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CategoriesJsonRequest1` | `discourse/models/categories_json_request1.py` |
| `CategoriesJsonRequest1Dict` | `discourse/models/categories_json_request1.py` |
| `CategoriesJsonResponse2` | `discourse/models/categories_json_response2.py` |

