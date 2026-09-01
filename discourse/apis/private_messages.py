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
from ..models.posts_json_request import PostsJsonRequest, PostsJsonRequestDict
from ..models.posts_json_response1 import PostsJsonResponse1
from ..models.topics_private_messages_json_response import TopicsPrivateMessagesJsonResponse
from ..models.topics_private_messages_sent_json_response import TopicsPrivateMessagesSentJsonResponse
from ..server.server import Server


class PrivateMessages:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = PrivateMessagesWithRawResponse(client, server)

    def create_topic_post_pm(
        self,
        api_key: str,
        api_username: str,
        *,
        body: PostsJsonRequest | PostsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PostsJsonResponse1:
        """Send a ``POST`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            post created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_topic_post_pm(
            api_key, api_username, body=body, request_options=request_options
        ).unwrap()

    def get_user_sent_private_messages(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TopicsPrivateMessagesSentJsonResponse:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            private messages

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_user_sent_private_messages(
            username, request_options=request_options
        ).unwrap()

    def list_user_private_messages(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TopicsPrivateMessagesJsonResponse:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            private messages

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_user_private_messages(username, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> PrivateMessagesWithRawResponse:
        return self._with_raw_response


class AsyncPrivateMessages:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncPrivateMessagesWithRawResponse(client, server)

    async def create_topic_post_pm(
        self,
        api_key: str,
        api_username: str,
        *,
        body: PostsJsonRequest | PostsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PostsJsonResponse1:
        """Send a ``POST`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            post created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_topic_post_pm(
                api_key, api_username, body=body, request_options=request_options
            )
        ).unwrap()

    async def get_user_sent_private_messages(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TopicsPrivateMessagesSentJsonResponse:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            private messages

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_user_sent_private_messages(username, request_options=request_options)
        ).unwrap()

    async def list_user_private_messages(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TopicsPrivateMessagesJsonResponse:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            private messages

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_user_private_messages(username, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPrivateMessagesWithRawResponse:
        return self._with_raw_response


class PrivateMessagesWithRawResponse(BaseRawResponse[RawClient, Server]):
    def create_topic_post_pm(
        self,
        api_key: str,
        api_username: str,
        *,
        body: PostsJsonRequest | PostsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PostsJsonResponse1, RawError]:
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
            url_template=self._server.default("/posts.json"),
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[PostsJsonRequest | PostsJsonRequestDict | None](body),
            decoder=json_decoder[PostsJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_user_sent_private_messages(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TopicsPrivateMessagesSentJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/topics/private-messages-sent/{username}.json"),
            path_params=[param[str]("username", username)],
            decoder=json_decoder[TopicsPrivateMessagesSentJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_user_private_messages(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TopicsPrivateMessagesJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/topics/private-messages/{username}.json"),
            path_params=[param[str]("username", username)],
            decoder=json_decoder[TopicsPrivateMessagesJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncPrivateMessagesWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def create_topic_post_pm(
        self,
        api_key: str,
        api_username: str,
        *,
        body: PostsJsonRequest | PostsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PostsJsonResponse1, RawError]:
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
            url_template=self._server.default("/posts.json"),
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[PostsJsonRequest | PostsJsonRequestDict | None](body),
            decoder=json_decoder[PostsJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_user_sent_private_messages(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TopicsPrivateMessagesSentJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/topics/private-messages-sent/{username}.json"),
            path_params=[param[str]("username", username)],
            decoder=json_decoder[TopicsPrivateMessagesSentJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_user_private_messages(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TopicsPrivateMessagesJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/topics/private-messages/{username}.json"),
            path_params=[param[str]("username", username)],
            decoder=json_decoder[TopicsPrivateMessagesJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
