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
from ..models.post_actions_json_request import PostActionsJsonRequest, PostActionsJsonRequestDict
from ..models.post_actions_json_response import PostActionsJsonResponse
from ..models.posts_json_request import PostsJsonRequest, PostsJsonRequestDict
from ..models.posts_json_request1 import PostsJsonRequest1, PostsJsonRequest1Dict
from ..models.posts_json_request2 import PostsJsonRequest2, PostsJsonRequest2Dict
from ..models.posts_json_response import PostsJsonResponse
from ..models.posts_json_response1 import PostsJsonResponse1
from ..models.posts_json_response2 import PostsJsonResponse2
from ..models.posts_json_response3 import PostsJsonResponse3
from ..models.posts_locked_json_request import PostsLockedJsonRequest, PostsLockedJsonRequestDict
from ..models.posts_locked_json_response import PostsLockedJsonResponse
from ..models.posts_replies_json_response import PostsRepliesJsonResponse
from ..server.server import Server


class Posts:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = PostsWithRawResponse(client, server)

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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            post created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_topic_post_pm(
            api_key, api_username, body=body, request_options=request_options
        ).unwrap()

    def delete_post(
        self,
        id_: int,
        api_key: str,
        api_username: str,
        *,
        body: PostsJsonRequest2 | PostsJsonRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            id_: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_post(
            id_, api_key, api_username, body=body, request_options=request_options
        ).unwrap()

    def get_post(self, id_: str, *, request_options: RequestOptionsOrDict | None = None) -> PostsJsonResponse2:
        """This endpoint can be used to get the number of likes on a post using the ``actions_summary`` property in the
        response. ``actions_summary`` responses with the id of ``2`` signify a ``like``. If there are no
        ``actions_summary`` items with the id of ``2``, that means there are 0 likes. Other ids likely refer to various
        different flag types.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            single reviewable post

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_post(id_, request_options=request_options).unwrap()

    def list_posts(
        self, *, before: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> PostsJsonResponse:
        """Send a ``GET`` request.

        Args:
            before: Load posts with an id lower than this value. Useful for pagination.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            latest posts

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_posts(before=before, request_options=request_options).unwrap()

    def lock_post(
        self,
        id_: str,
        api_key: str,
        api_username: str,
        *,
        body: PostsLockedJsonRequest | PostsLockedJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PostsLockedJsonResponse:
        """Send a ``PUT`` request.

        Args:
            id_: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            post updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.lock_post(
            id_, api_key, api_username, body=body, request_options=request_options
        ).unwrap()

    def perform_post_action(
        self,
        api_key: str,
        api_username: str,
        *,
        body: PostActionsJsonRequest | PostActionsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PostActionsJsonResponse:
        """Send a ``POST`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            post updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.perform_post_action(
            api_key, api_username, body=body, request_options=request_options
        ).unwrap()

    def post_replies(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PostsRepliesJsonResponse]:
        """Send a ``GET`` request.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            post replies

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.post_replies(id_, request_options=request_options).unwrap()

    def update_post(
        self,
        id_: str,
        api_key: str,
        api_username: str,
        *,
        body: PostsJsonRequest1 | PostsJsonRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PostsJsonResponse3:
        """Send a ``PUT`` request.

        Args:
            id_: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            post updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_post(
            id_, api_key, api_username, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> PostsWithRawResponse:
        return self._with_raw_response


class AsyncPosts:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncPostsWithRawResponse(client, server)

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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            post created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_topic_post_pm(
                api_key, api_username, body=body, request_options=request_options
            )
        ).unwrap()

    async def delete_post(
        self,
        id_: int,
        api_key: str,
        api_username: str,
        *,
        body: PostsJsonRequest2 | PostsJsonRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            id_: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_post(
                id_, api_key, api_username, body=body, request_options=request_options
            )
        ).unwrap()

    async def get_post(self, id_: str, *, request_options: RequestOptionsOrDict | None = None) -> PostsJsonResponse2:
        """This endpoint can be used to get the number of likes on a post using the ``actions_summary`` property in the
        response. ``actions_summary`` responses with the id of ``2`` signify a ``like``. If there are no
        ``actions_summary`` items with the id of ``2``, that means there are 0 likes. Other ids likely refer to various
        different flag types.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            single reviewable post

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_post(id_, request_options=request_options)).unwrap()

    async def list_posts(
        self, *, before: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> PostsJsonResponse:
        """Send a ``GET`` request.

        Args:
            before: Load posts with an id lower than this value. Useful for pagination.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            latest posts

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.list_posts(before=before, request_options=request_options)).unwrap()

    async def lock_post(
        self,
        id_: str,
        api_key: str,
        api_username: str,
        *,
        body: PostsLockedJsonRequest | PostsLockedJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PostsLockedJsonResponse:
        """Send a ``PUT`` request.

        Args:
            id_: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            post updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.lock_post(
                id_, api_key, api_username, body=body, request_options=request_options
            )
        ).unwrap()

    async def perform_post_action(
        self,
        api_key: str,
        api_username: str,
        *,
        body: PostActionsJsonRequest | PostActionsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PostActionsJsonResponse:
        """Send a ``POST`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            post updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.perform_post_action(
                api_key, api_username, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_replies(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PostsRepliesJsonResponse]:
        """Send a ``GET`` request.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            post replies

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.post_replies(id_, request_options=request_options)).unwrap()

    async def update_post(
        self,
        id_: str,
        api_key: str,
        api_username: str,
        *,
        body: PostsJsonRequest1 | PostsJsonRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PostsJsonResponse3:
        """Send a ``PUT`` request.

        Args:
            id_: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            post updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_post(
                id_, api_key, api_username, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPostsWithRawResponse:
        return self._with_raw_response


class PostsWithRawResponse(BaseRawResponse[RawClient, Server]):
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

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

    def delete_post(
        self,
        id_: int,
        api_key: str,
        api_username: str,
        *,
        body: PostsJsonRequest2 | PostsJsonRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            id_: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/posts/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[PostsJsonRequest2 | PostsJsonRequest2Dict | None](body),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_post(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PostsJsonResponse2, RawError]:
        """This endpoint can be used to get the number of likes on a post using the ``actions_summary`` property in the
        response. ``actions_summary`` responses with the id of ``2`` signify a ``like``. If there are no
        ``actions_summary`` items with the id of ``2``, that means there are 0 likes. Other ids likely refer to various
        different flag types.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/posts/{id}.json"),
            path_params=[param[str]("id", id_)],
            decoder=json_decoder[PostsJsonResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_posts(
        self, *, before: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PostsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            before: Load posts with an id lower than this value. Useful for pagination.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/posts.json"),
            query_params=[param[int | None]("before", before)],
            decoder=json_decoder[PostsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def lock_post(
        self,
        id_: str,
        api_key: str,
        api_username: str,
        *,
        body: PostsLockedJsonRequest | PostsLockedJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PostsLockedJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            id_: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/posts/{id}/locked.json"),
            path_params=[param[str]("id", id_)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[PostsLockedJsonRequest | PostsLockedJsonRequestDict | None](body),
            decoder=json_decoder[PostsLockedJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def perform_post_action(
        self,
        api_key: str,
        api_username: str,
        *,
        body: PostActionsJsonRequest | PostActionsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PostActionsJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/post_actions.json"),
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[PostActionsJsonRequest | PostActionsJsonRequestDict | None](body),
            decoder=json_decoder[PostActionsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def post_replies(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PostsRepliesJsonResponse], RawError]:
        """Send a ``GET`` request.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/posts/{id}/replies.json"),
            path_params=[param[str]("id", id_)],
            decoder=json_decoder[list[PostsRepliesJsonResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_post(
        self,
        id_: str,
        api_key: str,
        api_username: str,
        *,
        body: PostsJsonRequest1 | PostsJsonRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PostsJsonResponse3, RawError]:
        """Send a ``PUT`` request.

        Args:
            id_: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/posts/{id}.json"),
            path_params=[param[str]("id", id_)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[PostsJsonRequest1 | PostsJsonRequest1Dict | None](body),
            decoder=json_decoder[PostsJsonResponse3],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncPostsWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

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
            decoder=async_json_decoder[PostsJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_post(
        self,
        id_: int,
        api_key: str,
        api_username: str,
        *,
        body: PostsJsonRequest2 | PostsJsonRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            id_: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/posts/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[PostsJsonRequest2 | PostsJsonRequest2Dict | None](body),
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_post(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PostsJsonResponse2, RawError]:
        """This endpoint can be used to get the number of likes on a post using the ``actions_summary`` property in the
        response. ``actions_summary`` responses with the id of ``2`` signify a ``like``. If there are no
        ``actions_summary`` items with the id of ``2``, that means there are 0 likes. Other ids likely refer to various
        different flag types.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/posts/{id}.json"),
            path_params=[param[str]("id", id_)],
            decoder=async_json_decoder[PostsJsonResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_posts(
        self, *, before: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PostsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            before: Load posts with an id lower than this value. Useful for pagination.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/posts.json"),
            query_params=[param[int | None]("before", before)],
            decoder=async_json_decoder[PostsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def lock_post(
        self,
        id_: str,
        api_key: str,
        api_username: str,
        *,
        body: PostsLockedJsonRequest | PostsLockedJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PostsLockedJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            id_: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/posts/{id}/locked.json"),
            path_params=[param[str]("id", id_)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[PostsLockedJsonRequest | PostsLockedJsonRequestDict | None](body),
            decoder=async_json_decoder[PostsLockedJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def perform_post_action(
        self,
        api_key: str,
        api_username: str,
        *,
        body: PostActionsJsonRequest | PostActionsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PostActionsJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/post_actions.json"),
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[PostActionsJsonRequest | PostActionsJsonRequestDict | None](body),
            decoder=async_json_decoder[PostActionsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def post_replies(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PostsRepliesJsonResponse], RawError]:
        """Send a ``GET`` request.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/posts/{id}/replies.json"),
            path_params=[param[str]("id", id_)],
            decoder=async_json_decoder[list[PostsRepliesJsonResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_post(
        self,
        id_: str,
        api_key: str,
        api_username: str,
        *,
        body: PostsJsonRequest1 | PostsJsonRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PostsJsonResponse3, RawError]:
        """Send a ``PUT`` request.

        Args:
            id_: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/posts/{id}.json"),
            path_params=[param[str]("id", id_)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[PostsJsonRequest1 | PostsJsonRequest1Dict | None](body),
            decoder=async_json_decoder[PostsJsonResponse3],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
