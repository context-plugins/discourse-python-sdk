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
    param,
    raw_error_response,
)
from ..models.invites_create_multiple_json_request import (
    InvitesCreateMultipleJsonRequest,
    InvitesCreateMultipleJsonRequestDict,
)
from ..models.invites_create_multiple_json_response import InvitesCreateMultipleJsonResponse
from ..models.invites_json_request import InvitesJsonRequest, InvitesJsonRequestDict
from ..models.invites_json_response import InvitesJsonResponse
from ..models.t_invite_group_json_request import TInviteGroupJsonRequest, TInviteGroupJsonRequestDict
from ..models.t_invite_group_json_response import TInviteGroupJsonResponse
from ..models.t_invite_json_request import TInviteJsonRequest, TInviteJsonRequestDict
from ..models.t_invite_json_response import TInviteJsonResponse
from ..server.server import Server


class Invites:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = InvitesWithRawResponse(client, server)

    def create_invite(
        self,
        api_key: str,
        api_username: str,
        *,
        body: InvitesJsonRequest | InvitesJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InvitesJsonResponse:
        """Send a ``POST`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_invite(
            api_key, api_username, body=body, request_options=request_options
        ).unwrap()

    def create_multiple_invites(
        self,
        api_key: str,
        api_username: str,
        *,
        body: InvitesCreateMultipleJsonRequest | InvitesCreateMultipleJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InvitesCreateMultipleJsonResponse:
        """Send a ``POST`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_multiple_invites(
            api_key, api_username, body=body, request_options=request_options
        ).unwrap()

    def invite_group_to_topic(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TInviteGroupJsonRequest | TInviteGroupJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TInviteGroupJsonResponse:
        """Send a ``POST`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            invites to a PM

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.invite_group_to_topic(
            id, api_key, api_username, body=body, request_options=request_options
        ).unwrap()

    def invite_to_topic(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TInviteJsonRequest | TInviteJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TInviteJsonResponse:
        """Send a ``POST`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            topic updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.invite_to_topic(
            id, api_key, api_username, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> InvitesWithRawResponse:
        return self._with_raw_response


class AsyncInvites:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncInvitesWithRawResponse(client, server)

    async def create_invite(
        self,
        api_key: str,
        api_username: str,
        *,
        body: InvitesJsonRequest | InvitesJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InvitesJsonResponse:
        """Send a ``POST`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_invite(
                api_key, api_username, body=body, request_options=request_options
            )
        ).unwrap()

    async def create_multiple_invites(
        self,
        api_key: str,
        api_username: str,
        *,
        body: InvitesCreateMultipleJsonRequest | InvitesCreateMultipleJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InvitesCreateMultipleJsonResponse:
        """Send a ``POST`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_multiple_invites(
                api_key, api_username, body=body, request_options=request_options
            )
        ).unwrap()

    async def invite_group_to_topic(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TInviteGroupJsonRequest | TInviteGroupJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TInviteGroupJsonResponse:
        """Send a ``POST`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            invites to a PM

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.invite_group_to_topic(
                id, api_key, api_username, body=body, request_options=request_options
            )
        ).unwrap()

    async def invite_to_topic(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TInviteJsonRequest | TInviteJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TInviteJsonResponse:
        """Send a ``POST`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            topic updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.invite_to_topic(
                id, api_key, api_username, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncInvitesWithRawResponse:
        return self._with_raw_response


class InvitesWithRawResponse(BaseRawResponse[RawClient, Server]):
    def create_invite(
        self,
        api_key: str,
        api_username: str,
        *,
        body: InvitesJsonRequest | InvitesJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InvitesJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/invites.json"),
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[InvitesJsonRequest | InvitesJsonRequestDict | None](body),
            decoder=json_decoder[InvitesJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_multiple_invites(
        self,
        api_key: str,
        api_username: str,
        *,
        body: InvitesCreateMultipleJsonRequest | InvitesCreateMultipleJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InvitesCreateMultipleJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/invites/create-multiple.json"),
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[InvitesCreateMultipleJsonRequest | InvitesCreateMultipleJsonRequestDict | None](body),
            decoder=json_decoder[InvitesCreateMultipleJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def invite_group_to_topic(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TInviteGroupJsonRequest | TInviteGroupJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TInviteGroupJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/t/{id}/invite-group.json"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[TInviteGroupJsonRequest | TInviteGroupJsonRequestDict | None](body),
            decoder=json_decoder[TInviteGroupJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def invite_to_topic(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TInviteJsonRequest | TInviteJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TInviteJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/t/{id}/invite.json"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[TInviteJsonRequest | TInviteJsonRequestDict | None](body),
            decoder=json_decoder[TInviteJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncInvitesWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def create_invite(
        self,
        api_key: str,
        api_username: str,
        *,
        body: InvitesJsonRequest | InvitesJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InvitesJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/invites.json"),
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[InvitesJsonRequest | InvitesJsonRequestDict | None](body),
            decoder=json_decoder[InvitesJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_multiple_invites(
        self,
        api_key: str,
        api_username: str,
        *,
        body: InvitesCreateMultipleJsonRequest | InvitesCreateMultipleJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InvitesCreateMultipleJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/invites/create-multiple.json"),
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[InvitesCreateMultipleJsonRequest | InvitesCreateMultipleJsonRequestDict | None](body),
            decoder=json_decoder[InvitesCreateMultipleJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def invite_group_to_topic(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TInviteGroupJsonRequest | TInviteGroupJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TInviteGroupJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/t/{id}/invite-group.json"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[TInviteGroupJsonRequest | TInviteGroupJsonRequestDict | None](body),
            decoder=json_decoder[TInviteGroupJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def invite_to_topic(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TInviteJsonRequest | TInviteJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TInviteJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/t/{id}/invite.json"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[TInviteJsonRequest | TInviteJsonRequestDict | None](body),
            decoder=json_decoder[TInviteJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
