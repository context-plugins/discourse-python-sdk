from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.admin_backups_json_request import AdminBackupsJsonRequest, AdminBackupsJsonRequestDict
from ..models.admin_backups_json_response import AdminBackupsJsonResponse
from ..models.admin_backups_json_response1 import AdminBackupsJsonResponse1
from ..server.server import Server


class Backups:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = BackupsWithRawResponse(client, server)

    def create_backup(
        self,
        *,
        body: AdminBackupsJsonRequest | AdminBackupsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminBackupsJsonResponse1:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_backup(body=body, request_options=request_options).unwrap()

    def download_backup(
        self, filename: str, token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Send a ``GET`` request.

        Args:
            filename: Value sent with the request.
            token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.download_backup(filename, token, request_options=request_options).unwrap()

    def get_backups(self, *, request_options: RequestOptionsOrDict | None = None) -> list[AdminBackupsJsonResponse]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_backups(request_options=request_options).unwrap()

    def send_download_backup_email(self, filename: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Send a ``PUT`` request.

        Args:
            filename: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.send_download_backup_email(filename, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> BackupsWithRawResponse:
        return self._with_raw_response


class AsyncBackups:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncBackupsWithRawResponse(client, server)

    async def create_backup(
        self,
        *,
        body: AdminBackupsJsonRequest | AdminBackupsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminBackupsJsonResponse1:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_backup(body=body, request_options=request_options)).unwrap()

    async def download_backup(
        self, filename: str, token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Send a ``GET`` request.

        Args:
            filename: Value sent with the request.
            token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.download_backup(filename, token, request_options=request_options)
        ).unwrap()

    async def get_backups(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[AdminBackupsJsonResponse]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_backups(request_options=request_options)).unwrap()

    async def send_download_backup_email(
        self, filename: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Send a ``PUT`` request.

        Args:
            filename: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.send_download_backup_email(filename, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncBackupsWithRawResponse:
        return self._with_raw_response


class BackupsWithRawResponse(BaseRawResponse[RawClient, Server]):
    def create_backup(
        self,
        *,
        body: AdminBackupsJsonRequest | AdminBackupsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminBackupsJsonResponse1, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin/backups.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdminBackupsJsonRequest | AdminBackupsJsonRequestDict | None](body),
            decoder=json_decoder[AdminBackupsJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def download_backup(
        self, filename: str, token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``GET`` request.

        Args:
            filename: Value sent with the request.
            token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin/backups/{filename}"),
            path_params=[param[str]("filename", filename)],
            query_params=[param[str]("token", token)],
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_backups(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[AdminBackupsJsonResponse], RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin/backups.json"),
            decoder=json_decoder[list[AdminBackupsJsonResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def send_download_backup_email(
        self, filename: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``PUT`` request.

        Args:
            filename: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/admin/backups/{filename}"),
            path_params=[param[str]("filename", filename)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncBackupsWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def create_backup(
        self,
        *,
        body: AdminBackupsJsonRequest | AdminBackupsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminBackupsJsonResponse1, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin/backups.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdminBackupsJsonRequest | AdminBackupsJsonRequestDict | None](body),
            decoder=async_json_decoder[AdminBackupsJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def download_backup(
        self, filename: str, token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``GET`` request.

        Args:
            filename: Value sent with the request.
            token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin/backups/{filename}"),
            path_params=[param[str]("filename", filename)],
            query_params=[param[str]("token", token)],
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_backups(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[AdminBackupsJsonResponse], RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin/backups.json"),
            decoder=async_json_decoder[list[AdminBackupsJsonResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def send_download_backup_email(
        self, filename: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``PUT`` request.

        Args:
            filename: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/admin/backups/{filename}"),
            path_params=[param[str]("filename", filename)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )
