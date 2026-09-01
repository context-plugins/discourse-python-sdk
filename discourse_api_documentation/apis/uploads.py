from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    json_body,
    json_decoder,
    multipart_body,
    param,
    raw_error_response,
)
from ..models.enums.upload_type import UploadTypeOrStr
from ..models.uploads_abort_multipart_json_request import (
    UploadsAbortMultipartJsonRequest,
    UploadsAbortMultipartJsonRequestDict,
)
from ..models.uploads_abort_multipart_json_response import UploadsAbortMultipartJsonResponse
from ..models.uploads_batch_presign_multipart_parts_json_request import (
    UploadsBatchPresignMultipartPartsJsonRequest,
    UploadsBatchPresignMultipartPartsJsonRequestDict,
)
from ..models.uploads_batch_presign_multipart_parts_json_response import UploadsBatchPresignMultipartPartsJsonResponse
from ..models.uploads_complete_external_upload_json_request import (
    UploadsCompleteExternalUploadJsonRequest,
    UploadsCompleteExternalUploadJsonRequestDict,
)
from ..models.uploads_complete_external_upload_json_response import UploadsCompleteExternalUploadJsonResponse
from ..models.uploads_complete_multipart_json_request import (
    UploadsCompleteMultipartJsonRequest,
    UploadsCompleteMultipartJsonRequestDict,
)
from ..models.uploads_complete_multipart_json_response import UploadsCompleteMultipartJsonResponse
from ..models.uploads_create_multipart_json_request import (
    UploadsCreateMultipartJsonRequest,
    UploadsCreateMultipartJsonRequestDict,
)
from ..models.uploads_create_multipart_json_response import UploadsCreateMultipartJsonResponse
from ..models.uploads_generate_presigned_put_json_request import (
    UploadsGeneratePresignedPutJsonRequest,
    UploadsGeneratePresignedPutJsonRequestDict,
)
from ..models.uploads_generate_presigned_put_json_response import UploadsGeneratePresignedPutJsonResponse
from ..models.uploads_json_response import UploadsJsonResponse
from ..server.server import Server


class Uploads:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = UploadsWithRawResponse(client, server)

    def abort_multipart(
        self,
        *,
        body: UploadsAbortMultipartJsonRequest | UploadsAbortMultipartJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadsAbortMultipartJsonResponse:
        """This endpoint aborts the multipart upload initiated with /create-multipart. This should be used when
        cancelling the upload. It does not matter if parts were already uploaded into the external storage provider.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            external upload initialized

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.abort_multipart(body=body, request_options=request_options).unwrap()

    def batch_presign_multipart_parts(
        self,
        *,
        body: (
            UploadsBatchPresignMultipartPartsJsonRequest | UploadsBatchPresignMultipartPartsJsonRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadsBatchPresignMultipartPartsJsonResponse:
        """Multipart uploads are uploaded in chunks or parts to individual presigned URLs, similar to the one generated
        by /generate-presigned-put. The part numbers provided must be between 1 and 10000. The total number of parts
        will depend on the chunk size in bytes that you intend to use to upload each chunk. For example a 12MB file may
        have 2 5MB chunks and a final 2MB chunk, for part numbers 1, 2, and 3.

        This endpoint will return a presigned URL for each part number provided, which you can then use to send PUT
        requests for the binary chunk corresponding to that part. When the part is uploaded, the provider should return
        an ETag for the part, and this should be stored along with the part number, because this is needed to complete
        the multipart upload.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            external upload initialized

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.batch_presign_multipart_parts(
            body=body, request_options=request_options
        ).unwrap()

    def complete_external_upload(
        self,
        *,
        body: UploadsCompleteExternalUploadJsonRequest | UploadsCompleteExternalUploadJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadsCompleteExternalUploadJsonResponse:
        """Completes an external upload initialized with /get-presigned-put. The file will be moved from its temporary
        location in external storage to a final destination in the S3 bucket. An Upload record will also be created in
        the database in most cases.

        If a sha1-checksum was provided in the initial request it will also be compared with the uploaded file in
        storage to make sure the same file was uploaded. The file size will be compared for the same reason.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            external upload initialized

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.complete_external_upload(body=body, request_options=request_options).unwrap()

    def complete_multipart(
        self,
        *,
        body: UploadsCompleteMultipartJsonRequest | UploadsCompleteMultipartJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadsCompleteMultipartJsonResponse:
        """Completes the multipart upload in the external store, and copies the file from its temporary location to its
        final location in the store. All of the parts must have been uploaded to the external storage provider. An
        Upload record will be completed in most cases once the file is copied to its final location.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            external upload initialized

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.complete_multipart(body=body, request_options=request_options).unwrap()

    def create_multipart_upload(
        self,
        *,
        body: UploadsCreateMultipartJsonRequest | UploadsCreateMultipartJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadsCreateMultipartJsonResponse:
        """Creates a multipart upload in the external storage provider, storing a temporary reference to the external
        upload similar to /get-presigned-put.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            external upload initialized

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_multipart_upload(body=body, request_options=request_options).unwrap()

    def create_upload(
        self,
        upload_type: UploadTypeOrStr,
        *,
        user_id: int | None = None,
        synchronous: bool | None = None,
        file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadsJsonResponse:
        """Send a ``POST`` request.

        Args:
            upload_type: Value sent with the request.
            user_id: required if uploading an avatar
            synchronous: Use this flag to return an id and url
            file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            file uploaded

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_upload(
            upload_type, user_id=user_id, synchronous=synchronous, file=file, request_options=request_options
        ).unwrap()

    def generate_presigned_put(
        self,
        *,
        body: UploadsGeneratePresignedPutJsonRequest | UploadsGeneratePresignedPutJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadsGeneratePresignedPutJsonResponse:
        """Direct external uploads bypass the usual method of creating uploads via the POST /uploads route, and upload
        directly to an external provider, which by default is S3. This route begins the process, and will return a
        unique identifier for the external upload as well as a presigned URL which is where the file binary blob should
        be uploaded to.

        Once the upload is complete to the external service, you must call the POST /complete-external-upload route
        using the unique identifier returned by this route, which will create any required Upload record in the
        Discourse database and also move file from its temporary location to the final destination in the external
        storage service.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            external upload initialized

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.generate_presigned_put(body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> UploadsWithRawResponse:
        return self._with_raw_response


class AsyncUploads:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncUploadsWithRawResponse(client, server)

    async def abort_multipart(
        self,
        *,
        body: UploadsAbortMultipartJsonRequest | UploadsAbortMultipartJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadsAbortMultipartJsonResponse:
        """This endpoint aborts the multipart upload initiated with /create-multipart. This should be used when
        cancelling the upload. It does not matter if parts were already uploaded into the external storage provider.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            external upload initialized

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.abort_multipart(body=body, request_options=request_options)).unwrap()

    async def batch_presign_multipart_parts(
        self,
        *,
        body: (
            UploadsBatchPresignMultipartPartsJsonRequest | UploadsBatchPresignMultipartPartsJsonRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadsBatchPresignMultipartPartsJsonResponse:
        """Multipart uploads are uploaded in chunks or parts to individual presigned URLs, similar to the one generated
        by /generate-presigned-put. The part numbers provided must be between 1 and 10000. The total number of parts
        will depend on the chunk size in bytes that you intend to use to upload each chunk. For example a 12MB file may
        have 2 5MB chunks and a final 2MB chunk, for part numbers 1, 2, and 3.

        This endpoint will return a presigned URL for each part number provided, which you can then use to send PUT
        requests for the binary chunk corresponding to that part. When the part is uploaded, the provider should return
        an ETag for the part, and this should be stored along with the part number, because this is needed to complete
        the multipart upload.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            external upload initialized

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.batch_presign_multipart_parts(body=body, request_options=request_options)
        ).unwrap()

    async def complete_external_upload(
        self,
        *,
        body: UploadsCompleteExternalUploadJsonRequest | UploadsCompleteExternalUploadJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadsCompleteExternalUploadJsonResponse:
        """Completes an external upload initialized with /get-presigned-put. The file will be moved from its temporary
        location in external storage to a final destination in the S3 bucket. An Upload record will also be created in
        the database in most cases.

        If a sha1-checksum was provided in the initial request it will also be compared with the uploaded file in
        storage to make sure the same file was uploaded. The file size will be compared for the same reason.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            external upload initialized

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.complete_external_upload(body=body, request_options=request_options)
        ).unwrap()

    async def complete_multipart(
        self,
        *,
        body: UploadsCompleteMultipartJsonRequest | UploadsCompleteMultipartJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadsCompleteMultipartJsonResponse:
        """Completes the multipart upload in the external store, and copies the file from its temporary location to its
        final location in the store. All of the parts must have been uploaded to the external storage provider. An
        Upload record will be completed in most cases once the file is copied to its final location.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            external upload initialized

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.complete_multipart(body=body, request_options=request_options)).unwrap()

    async def create_multipart_upload(
        self,
        *,
        body: UploadsCreateMultipartJsonRequest | UploadsCreateMultipartJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadsCreateMultipartJsonResponse:
        """Creates a multipart upload in the external storage provider, storing a temporary reference to the external
        upload similar to /get-presigned-put.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            external upload initialized

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_multipart_upload(body=body, request_options=request_options)
        ).unwrap()

    async def create_upload(
        self,
        upload_type: UploadTypeOrStr,
        *,
        user_id: int | None = None,
        synchronous: bool | None = None,
        file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadsJsonResponse:
        """Send a ``POST`` request.

        Args:
            upload_type: Value sent with the request.
            user_id: required if uploading an avatar
            synchronous: Use this flag to return an id and url
            file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            file uploaded

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_upload(
                upload_type, user_id=user_id, synchronous=synchronous, file=file, request_options=request_options
            )
        ).unwrap()

    async def generate_presigned_put(
        self,
        *,
        body: UploadsGeneratePresignedPutJsonRequest | UploadsGeneratePresignedPutJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UploadsGeneratePresignedPutJsonResponse:
        """Direct external uploads bypass the usual method of creating uploads via the POST /uploads route, and upload
        directly to an external provider, which by default is S3. This route begins the process, and will return a
        unique identifier for the external upload as well as a presigned URL which is where the file binary blob should
        be uploaded to.

        Once the upload is complete to the external service, you must call the POST /complete-external-upload route
        using the unique identifier returned by this route, which will create any required Upload record in the
        Discourse database and also move file from its temporary location to the final destination in the external
        storage service.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            external upload initialized

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.generate_presigned_put(body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncUploadsWithRawResponse:
        return self._with_raw_response


class UploadsWithRawResponse(BaseRawResponse[RawClient, Server]):
    def abort_multipart(
        self,
        *,
        body: UploadsAbortMultipartJsonRequest | UploadsAbortMultipartJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadsAbortMultipartJsonResponse, RawError]:
        """This endpoint aborts the multipart upload initiated with /create-multipart. This should be used when
        cancelling the upload. It does not matter if parts were already uploaded into the external storage provider.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/uploads/abort-multipart.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UploadsAbortMultipartJsonRequest | UploadsAbortMultipartJsonRequestDict | None](body),
            decoder=json_decoder[UploadsAbortMultipartJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def batch_presign_multipart_parts(
        self,
        *,
        body: (
            UploadsBatchPresignMultipartPartsJsonRequest | UploadsBatchPresignMultipartPartsJsonRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadsBatchPresignMultipartPartsJsonResponse, RawError]:
        """Multipart uploads are uploaded in chunks or parts to individual presigned URLs, similar to the one generated
        by /generate-presigned-put. The part numbers provided must be between 1 and 10000. The total number of parts
        will depend on the chunk size in bytes that you intend to use to upload each chunk. For example a 12MB file may
        have 2 5MB chunks and a final 2MB chunk, for part numbers 1, 2, and 3.

        This endpoint will return a presigned URL for each part number provided, which you can then use to send PUT
        requests for the binary chunk corresponding to that part. When the part is uploaded, the provider should return
        an ETag for the part, and this should be stored along with the part number, because this is needed to complete
        the multipart upload.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/uploads/batch-presign-multipart-parts.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                UploadsBatchPresignMultipartPartsJsonRequest | UploadsBatchPresignMultipartPartsJsonRequestDict | None
            ](body),
            decoder=json_decoder[UploadsBatchPresignMultipartPartsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def complete_external_upload(
        self,
        *,
        body: UploadsCompleteExternalUploadJsonRequest | UploadsCompleteExternalUploadJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadsCompleteExternalUploadJsonResponse, RawError]:
        """Completes an external upload initialized with /get-presigned-put. The file will be moved from its temporary
        location in external storage to a final destination in the S3 bucket. An Upload record will also be created in
        the database in most cases.

        If a sha1-checksum was provided in the initial request it will also be compared with the uploaded file in
        storage to make sure the same file was uploaded. The file size will be compared for the same reason.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/uploads/complete-external-upload.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                UploadsCompleteExternalUploadJsonRequest | UploadsCompleteExternalUploadJsonRequestDict | None
            ](body),
            decoder=json_decoder[UploadsCompleteExternalUploadJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def complete_multipart(
        self,
        *,
        body: UploadsCompleteMultipartJsonRequest | UploadsCompleteMultipartJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadsCompleteMultipartJsonResponse, RawError]:
        """Completes the multipart upload in the external store, and copies the file from its temporary location to its
        final location in the store. All of the parts must have been uploaded to the external storage provider. An
        Upload record will be completed in most cases once the file is copied to its final location.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/uploads/complete-multipart.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UploadsCompleteMultipartJsonRequest | UploadsCompleteMultipartJsonRequestDict | None](body),
            decoder=json_decoder[UploadsCompleteMultipartJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_multipart_upload(
        self,
        *,
        body: UploadsCreateMultipartJsonRequest | UploadsCreateMultipartJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadsCreateMultipartJsonResponse, RawError]:
        """Creates a multipart upload in the external storage provider, storing a temporary reference to the external
        upload similar to /get-presigned-put.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/uploads/create-multipart.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UploadsCreateMultipartJsonRequest | UploadsCreateMultipartJsonRequestDict | None](body),
            decoder=json_decoder[UploadsCreateMultipartJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_upload(
        self,
        upload_type: UploadTypeOrStr,
        *,
        user_id: int | None = None,
        synchronous: bool | None = None,
        file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadsJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            upload_type: Value sent with the request.
            user_id: required if uploading an avatar
            synchronous: Use this flag to return an id and url
            file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/uploads.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                [
                    param[UploadTypeOrStr]("upload_type", upload_type),
                    param[int | None]("user_id", user_id),
                    param[bool | None]("synchronous", synchronous),
                ],
                {"file": file},
            ),
            decoder=json_decoder[UploadsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def generate_presigned_put(
        self,
        *,
        body: UploadsGeneratePresignedPutJsonRequest | UploadsGeneratePresignedPutJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadsGeneratePresignedPutJsonResponse, RawError]:
        """Direct external uploads bypass the usual method of creating uploads via the POST /uploads route, and upload
        directly to an external provider, which by default is S3. This route begins the process, and will return a
        unique identifier for the external upload as well as a presigned URL which is where the file binary blob should
        be uploaded to.

        Once the upload is complete to the external service, you must call the POST /complete-external-upload route
        using the unique identifier returned by this route, which will create any required Upload record in the
        Discourse database and also move file from its temporary location to the final destination in the external
        storage service.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/uploads/generate-presigned-put.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UploadsGeneratePresignedPutJsonRequest | UploadsGeneratePresignedPutJsonRequestDict | None](
                body
            ),
            decoder=json_decoder[UploadsGeneratePresignedPutJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncUploadsWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def abort_multipart(
        self,
        *,
        body: UploadsAbortMultipartJsonRequest | UploadsAbortMultipartJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadsAbortMultipartJsonResponse, RawError]:
        """This endpoint aborts the multipart upload initiated with /create-multipart. This should be used when
        cancelling the upload. It does not matter if parts were already uploaded into the external storage provider.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/uploads/abort-multipart.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UploadsAbortMultipartJsonRequest | UploadsAbortMultipartJsonRequestDict | None](body),
            decoder=json_decoder[UploadsAbortMultipartJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def batch_presign_multipart_parts(
        self,
        *,
        body: (
            UploadsBatchPresignMultipartPartsJsonRequest | UploadsBatchPresignMultipartPartsJsonRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadsBatchPresignMultipartPartsJsonResponse, RawError]:
        """Multipart uploads are uploaded in chunks or parts to individual presigned URLs, similar to the one generated
        by /generate-presigned-put. The part numbers provided must be between 1 and 10000. The total number of parts
        will depend on the chunk size in bytes that you intend to use to upload each chunk. For example a 12MB file may
        have 2 5MB chunks and a final 2MB chunk, for part numbers 1, 2, and 3.

        This endpoint will return a presigned URL for each part number provided, which you can then use to send PUT
        requests for the binary chunk corresponding to that part. When the part is uploaded, the provider should return
        an ETag for the part, and this should be stored along with the part number, because this is needed to complete
        the multipart upload.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/uploads/batch-presign-multipart-parts.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                UploadsBatchPresignMultipartPartsJsonRequest | UploadsBatchPresignMultipartPartsJsonRequestDict | None
            ](body),
            decoder=json_decoder[UploadsBatchPresignMultipartPartsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def complete_external_upload(
        self,
        *,
        body: UploadsCompleteExternalUploadJsonRequest | UploadsCompleteExternalUploadJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadsCompleteExternalUploadJsonResponse, RawError]:
        """Completes an external upload initialized with /get-presigned-put. The file will be moved from its temporary
        location in external storage to a final destination in the S3 bucket. An Upload record will also be created in
        the database in most cases.

        If a sha1-checksum was provided in the initial request it will also be compared with the uploaded file in
        storage to make sure the same file was uploaded. The file size will be compared for the same reason.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/uploads/complete-external-upload.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                UploadsCompleteExternalUploadJsonRequest | UploadsCompleteExternalUploadJsonRequestDict | None
            ](body),
            decoder=json_decoder[UploadsCompleteExternalUploadJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def complete_multipart(
        self,
        *,
        body: UploadsCompleteMultipartJsonRequest | UploadsCompleteMultipartJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadsCompleteMultipartJsonResponse, RawError]:
        """Completes the multipart upload in the external store, and copies the file from its temporary location to its
        final location in the store. All of the parts must have been uploaded to the external storage provider. An
        Upload record will be completed in most cases once the file is copied to its final location.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/uploads/complete-multipart.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UploadsCompleteMultipartJsonRequest | UploadsCompleteMultipartJsonRequestDict | None](body),
            decoder=json_decoder[UploadsCompleteMultipartJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_multipart_upload(
        self,
        *,
        body: UploadsCreateMultipartJsonRequest | UploadsCreateMultipartJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadsCreateMultipartJsonResponse, RawError]:
        """Creates a multipart upload in the external storage provider, storing a temporary reference to the external
        upload similar to /get-presigned-put.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/uploads/create-multipart.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UploadsCreateMultipartJsonRequest | UploadsCreateMultipartJsonRequestDict | None](body),
            decoder=json_decoder[UploadsCreateMultipartJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_upload(
        self,
        upload_type: UploadTypeOrStr,
        *,
        user_id: int | None = None,
        synchronous: bool | None = None,
        file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadsJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            upload_type: Value sent with the request.
            user_id: required if uploading an avatar
            synchronous: Use this flag to return an id and url
            file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/uploads.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                [
                    param[UploadTypeOrStr]("upload_type", upload_type),
                    param[int | None]("user_id", user_id),
                    param[bool | None]("synchronous", synchronous),
                ],
                {"file": file},
            ),
            decoder=json_decoder[UploadsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def generate_presigned_put(
        self,
        *,
        body: UploadsGeneratePresignedPutJsonRequest | UploadsGeneratePresignedPutJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UploadsGeneratePresignedPutJsonResponse, RawError]:
        """Direct external uploads bypass the usual method of creating uploads via the POST /uploads route, and upload
        directly to an external provider, which by default is S3. This route begins the process, and will return a
        unique identifier for the external upload as well as a presigned URL which is where the file binary blob should
        be uploaded to.

        Once the upload is complete to the external service, you must call the POST /complete-external-upload route
        using the unique identifier returned by this route, which will create any required Upload record in the
        Discourse database and also move file from its temporary location to the final destination in the external
        storage service.

        You must have the correct permissions and CORS settings configured in your external provider. We support AWS S3
        as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and ``enable_direct_s3_uploads`` must be set to true for this endpoint to
        function.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/uploads/generate-presigned-put.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UploadsGeneratePresignedPutJsonRequest | UploadsGeneratePresignedPutJsonRequestDict | None](
                body
            ),
            decoder=json_decoder[UploadsGeneratePresignedPutJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
