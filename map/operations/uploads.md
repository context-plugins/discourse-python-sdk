<!-- Generated file — do not edit; regenerated with the SDK. -->

# Uploads — operations

Accessor: `client.uploads` · Source: `discourse_api_documentation/apis/uploads.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.uploads.abort_multipart

- **Route**: `POST /uploads/abort-multipart.json`
- **Signature**: `def abort_multipart(*, body: UploadsAbortMultipartJsonRequest | UploadsAbortMultipartJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UploadsAbortMultipartJsonResponse`
- **Returns (raw)**: `ApiResult[UploadsAbortMultipartJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UploadsAbortMultipartJsonRequest` | `discourse_api_documentation/models/uploads_abort_multipart_json_request.py` |
| `UploadsAbortMultipartJsonRequestDict` | `discourse_api_documentation/models/uploads_abort_multipart_json_request.py` |
| `UploadsAbortMultipartJsonResponse` | `discourse_api_documentation/models/uploads_abort_multipart_json_response.py` |

### client.uploads.batch_presign_multipart_parts

- **Route**: `POST /uploads/batch-presign-multipart-parts.json`
- **Signature**: `def batch_presign_multipart_parts(*, body: UploadsBatchPresignMultipartPartsJsonRequest | UploadsBatchPresignMultipartPartsJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UploadsBatchPresignMultipartPartsJsonResponse`
- **Returns (raw)**: `ApiResult[UploadsBatchPresignMultipartPartsJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UploadsBatchPresignMultipartPartsJsonRequest` | `discourse_api_documentation/models/uploads_batch_presign_multipart_parts_json_request.py` |
| `UploadsBatchPresignMultipartPartsJsonRequestDict` | `discourse_api_documentation/models/uploads_batch_presign_multipart_parts_json_request.py` |
| `UploadsBatchPresignMultipartPartsJsonResponse` | `discourse_api_documentation/models/uploads_batch_presign_multipart_parts_json_response.py` |

### client.uploads.complete_external_upload

- **Route**: `POST /uploads/complete-external-upload.json`
- **Signature**: `def complete_external_upload(*, body: UploadsCompleteExternalUploadJsonRequest | UploadsCompleteExternalUploadJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UploadsCompleteExternalUploadJsonResponse`
- **Returns (raw)**: `ApiResult[UploadsCompleteExternalUploadJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UploadsCompleteExternalUploadJsonRequest` | `discourse_api_documentation/models/uploads_complete_external_upload_json_request.py` |
| `UploadsCompleteExternalUploadJsonRequestDict` | `discourse_api_documentation/models/uploads_complete_external_upload_json_request.py` |
| `UploadsCompleteExternalUploadJsonResponse` | `discourse_api_documentation/models/uploads_complete_external_upload_json_response.py` |

### client.uploads.complete_multipart

- **Route**: `POST /uploads/complete-multipart.json`
- **Signature**: `def complete_multipart(*, body: UploadsCompleteMultipartJsonRequest | UploadsCompleteMultipartJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UploadsCompleteMultipartJsonResponse`
- **Returns (raw)**: `ApiResult[UploadsCompleteMultipartJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UploadsCompleteMultipartJsonRequest` | `discourse_api_documentation/models/uploads_complete_multipart_json_request.py` |
| `UploadsCompleteMultipartJsonRequestDict` | `discourse_api_documentation/models/uploads_complete_multipart_json_request.py` |
| `UploadsCompleteMultipartJsonResponse` | `discourse_api_documentation/models/uploads_complete_multipart_json_response.py` |

### client.uploads.create_multipart_upload

- **Route**: `POST /uploads/create-multipart.json`
- **Signature**: `def create_multipart_upload(*, body: UploadsCreateMultipartJsonRequest | UploadsCreateMultipartJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UploadsCreateMultipartJsonResponse`
- **Returns (raw)**: `ApiResult[UploadsCreateMultipartJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UploadsCreateMultipartJsonRequest` | `discourse_api_documentation/models/uploads_create_multipart_json_request.py` |
| `UploadsCreateMultipartJsonRequestDict` | `discourse_api_documentation/models/uploads_create_multipart_json_request.py` |
| `UploadsCreateMultipartJsonResponse` | `discourse_api_documentation/models/uploads_create_multipart_json_response.py` |

### client.uploads.create_upload

- **Route**: `POST /uploads.json`
- **Signature**: `def create_upload(upload_type: UploadTypeOrStr, *, user_id: int | None = None, synchronous: bool | None = None, file: bytes | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `upload_type`
- **Params**: `upload_type` — multipart field · `user_id` — multipart field · `synchronous` — multipart field · `file` — multipart file
- **Returns (parsed)**: `UploadsJsonResponse`
- **Returns (raw)**: `ApiResult[UploadsJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UploadTypeOrStr` | `discourse_api_documentation/models/enums/upload_type.py` |
| `UploadsJsonResponse` | `discourse_api_documentation/models/uploads_json_response.py` |

### client.uploads.generate_presigned_put

- **Route**: `POST /uploads/generate-presigned-put.json`
- **Signature**: `def generate_presigned_put(*, body: UploadsGeneratePresignedPutJsonRequest | UploadsGeneratePresignedPutJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UploadsGeneratePresignedPutJsonResponse`
- **Returns (raw)**: `ApiResult[UploadsGeneratePresignedPutJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UploadsGeneratePresignedPutJsonRequest` | `discourse_api_documentation/models/uploads_generate_presigned_put_json_request.py` |
| `UploadsGeneratePresignedPutJsonRequestDict` | `discourse_api_documentation/models/uploads_generate_presigned_put_json_request.py` |
| `UploadsGeneratePresignedPutJsonResponse` | `discourse_api_documentation/models/uploads_generate_presigned_put_json_response.py` |

