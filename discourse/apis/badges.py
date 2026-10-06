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
from ..models.admin_badges_json_request import AdminBadgesJsonRequest, AdminBadgesJsonRequestDict
from ..models.admin_badges_json_request1 import AdminBadgesJsonRequest1, AdminBadgesJsonRequest1Dict
from ..models.admin_badges_json_response import AdminBadgesJsonResponse
from ..models.admin_badges_json_response1 import AdminBadgesJsonResponse1
from ..models.admin_badges_json_response2 import AdminBadgesJsonResponse2
from ..models.user_badges_json_response import UserBadgesJsonResponse
from ..server.server import Server


class Badges:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = BadgesWithRawResponse(client, server)

    def admin_list_badges(self, *, request_options: RequestOptionsOrDict | None = None) -> AdminBadgesJsonResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_list_badges(request_options=request_options).unwrap()

    def create_badge(
        self,
        *,
        body: AdminBadgesJsonRequest | AdminBadgesJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminBadgesJsonResponse1:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_badge(body=body, request_options=request_options).unwrap()

    def delete_badge(self, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Send a ``DELETE`` request.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_badge(id_, request_options=request_options).unwrap()

    def list_user_badges(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UserBadgesJsonResponse:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_user_badges(username, request_options=request_options).unwrap()

    def update_badge(
        self,
        id_: int,
        *,
        body: AdminBadgesJsonRequest1 | AdminBadgesJsonRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminBadgesJsonResponse2:
        """Send a ``PUT`` request.

        Args:
            id_: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_badge(id_, body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> BadgesWithRawResponse:
        return self._with_raw_response


class AsyncBadges:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncBadgesWithRawResponse(client, server)

    async def admin_list_badges(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> AdminBadgesJsonResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.admin_list_badges(request_options=request_options)).unwrap()

    async def create_badge(
        self,
        *,
        body: AdminBadgesJsonRequest | AdminBadgesJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminBadgesJsonResponse1:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_badge(body=body, request_options=request_options)).unwrap()

    async def delete_badge(self, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Send a ``DELETE`` request.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_badge(id_, request_options=request_options)).unwrap()

    async def list_user_badges(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UserBadgesJsonResponse:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.list_user_badges(username, request_options=request_options)).unwrap()

    async def update_badge(
        self,
        id_: int,
        *,
        body: AdminBadgesJsonRequest1 | AdminBadgesJsonRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminBadgesJsonResponse2:
        """Send a ``PUT`` request.

        Args:
            id_: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.update_badge(id_, body=body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncBadgesWithRawResponse:
        return self._with_raw_response


class BadgesWithRawResponse(BaseRawResponse[RawClient, Server]):
    def admin_list_badges(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AdminBadgesJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin/badges.json"),
            decoder=json_decoder[AdminBadgesJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_badge(
        self,
        *,
        body: AdminBadgesJsonRequest | AdminBadgesJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminBadgesJsonResponse1, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin/badges.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdminBadgesJsonRequest | AdminBadgesJsonRequestDict | None](body),
            decoder=json_decoder[AdminBadgesJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_badge(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/admin/badges/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_user_badges(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UserBadgesJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/user-badges/{username}.json"),
            path_params=[param[str]("username", username)],
            decoder=json_decoder[UserBadgesJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_badge(
        self,
        id_: int,
        *,
        body: AdminBadgesJsonRequest1 | AdminBadgesJsonRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminBadgesJsonResponse2, RawError]:
        """Send a ``PUT`` request.

        Args:
            id_: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/admin/badges/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdminBadgesJsonRequest1 | AdminBadgesJsonRequest1Dict | None](body),
            decoder=json_decoder[AdminBadgesJsonResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncBadgesWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def admin_list_badges(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AdminBadgesJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin/badges.json"),
            decoder=async_json_decoder[AdminBadgesJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_badge(
        self,
        *,
        body: AdminBadgesJsonRequest | AdminBadgesJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminBadgesJsonResponse1, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin/badges.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdminBadgesJsonRequest | AdminBadgesJsonRequestDict | None](body),
            decoder=async_json_decoder[AdminBadgesJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_badge(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/admin/badges/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_user_badges(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UserBadgesJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/user-badges/{username}.json"),
            path_params=[param[str]("username", username)],
            decoder=async_json_decoder[UserBadgesJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_badge(
        self,
        id_: int,
        *,
        body: AdminBadgesJsonRequest1 | AdminBadgesJsonRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminBadgesJsonResponse2, RawError]:
        """Send a ``PUT`` request.

        Args:
            id_: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/admin/badges/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdminBadgesJsonRequest1 | AdminBadgesJsonRequest1Dict | None](body),
            decoder=async_json_decoder[AdminBadgesJsonResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
