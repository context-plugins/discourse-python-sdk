from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.notifications_json_response import NotificationsJsonResponse
from ..models.notifications_mark_read_json_request import (
    NotificationsMarkReadJsonRequest,
    NotificationsMarkReadJsonRequestDict,
)
from ..models.notifications_mark_read_json_response import NotificationsMarkReadJsonResponse
from ..server.server import Server


class Notifications:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = NotificationsWithRawResponse(client, server)

    def get_notifications(self, *, request_options: RequestOptionsOrDict | None = None) -> NotificationsJsonResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            notifications

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_notifications(request_options=request_options).unwrap()

    def mark_notifications_as_read(
        self,
        *,
        body: NotificationsMarkReadJsonRequest | NotificationsMarkReadJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NotificationsMarkReadJsonResponse:
        """Send a ``PUT`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            notifications marked read

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.mark_notifications_as_read(body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> NotificationsWithRawResponse:
        return self._with_raw_response


class AsyncNotifications:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncNotificationsWithRawResponse(client, server)

    async def get_notifications(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> NotificationsJsonResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            notifications

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_notifications(request_options=request_options)).unwrap()

    async def mark_notifications_as_read(
        self,
        *,
        body: NotificationsMarkReadJsonRequest | NotificationsMarkReadJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NotificationsMarkReadJsonResponse:
        """Send a ``PUT`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            notifications marked read

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.mark_notifications_as_read(body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncNotificationsWithRawResponse:
        return self._with_raw_response


class NotificationsWithRawResponse(BaseRawResponse[RawClient, Server]):
    def get_notifications(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NotificationsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/notifications.json"),
            decoder=json_decoder[NotificationsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def mark_notifications_as_read(
        self,
        *,
        body: NotificationsMarkReadJsonRequest | NotificationsMarkReadJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NotificationsMarkReadJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/notifications/mark-read.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[NotificationsMarkReadJsonRequest | NotificationsMarkReadJsonRequestDict | None](body),
            decoder=json_decoder[NotificationsMarkReadJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNotificationsWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def get_notifications(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NotificationsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/notifications.json"),
            decoder=async_json_decoder[NotificationsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def mark_notifications_as_read(
        self,
        *,
        body: NotificationsMarkReadJsonRequest | NotificationsMarkReadJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NotificationsMarkReadJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/notifications/mark-read.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[NotificationsMarkReadJsonRequest | NotificationsMarkReadJsonRequestDict | None](body),
            decoder=async_json_decoder[NotificationsMarkReadJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
