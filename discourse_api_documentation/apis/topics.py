from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.latest_json_response import LatestJsonResponse
from ..models.posts_json_request import PostsJsonRequest, PostsJsonRequestDict
from ..models.posts_json_response1 import PostsJsonResponse1
from ..models.t_change_timestamp_json_request import TChangeTimestampJsonRequest, TChangeTimestampJsonRequestDict
from ..models.t_change_timestamp_json_response import TChangeTimestampJsonResponse
from ..models.t_invite_group_json_request import TInviteGroupJsonRequest, TInviteGroupJsonRequestDict
from ..models.t_invite_group_json_response import TInviteGroupJsonResponse
from ..models.t_invite_json_request import TInviteJsonRequest, TInviteJsonRequestDict
from ..models.t_invite_json_response import TInviteJsonResponse
from ..models.t_json_request import TJsonRequest, TJsonRequestDict
from ..models.t_json_response import TJsonResponse
from ..models.t_json_response1 import TJsonResponse1
from ..models.t_notifications_json_request import TNotificationsJsonRequest, TNotificationsJsonRequestDict
from ..models.t_notifications_json_response import TNotificationsJsonResponse
from ..models.t_posts_json_response import TPostsJsonResponse
from ..models.t_status_json_request import TStatusJsonRequest, TStatusJsonRequestDict
from ..models.t_status_json_response import TStatusJsonResponse
from ..models.t_timer_json_request import TTimerJsonRequest, TTimerJsonRequestDict
from ..models.t_timer_json_response import TTimerJsonResponse
from ..models.top_json_response import TopJsonResponse
from ..server.server import Server


class Topics:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = TopicsWithRawResponse(client, server)

    def bookmark_topic(
        self, id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            topic updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bookmark_topic(
            id, api_key, api_username, request_options=request_options
        ).unwrap()

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

    def create_topic_timer(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TTimerJsonRequest | TTimerJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TTimerJsonResponse:
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
        return self._with_raw_response.create_topic_timer(
            id, api_key, api_username, body=body, request_options=request_options
        ).unwrap()

    def get_specific_posts_from_topic(
        self, id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TPostsJsonResponse:
        """Send a ``GET`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            specific posts

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_specific_posts_from_topic(
            id, api_key, api_username, request_options=request_options
        ).unwrap()

    def get_topic(
        self, id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TJsonResponse:
        """Send a ``GET`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            specific posts

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_topic(id, api_key, api_username, request_options=request_options).unwrap()

    def get_topic_by_external_id(
        self, external_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Send a ``GET`` request.

        Args:
            external_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_topic_by_external_id(external_id, request_options=request_options).unwrap()

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

    def list_latest_topics(
        self,
        api_key: str,
        api_username: str,
        *,
        order: str | None = None,
        ascending: str | None = None,
        per_page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LatestJsonResponse:
        """Send a ``GET`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            order: Enum: ``default``, ``created``, ``activity``, ``views``, ``posts``, ``category``, ``likes``,
                ``op_likes``, ``posters``
            ascending: Defaults to ``desc``, add ``ascending=true`` to sort asc
            per_page: Maximum number of topics returned, between 1-100
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            topic updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_latest_topics(
            api_key, api_username, order=order, ascending=ascending, per_page=per_page, request_options=request_options
        ).unwrap()

    def list_top_topics(
        self,
        api_key: str,
        api_username: str,
        *,
        period: str | None = None,
        per_page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TopJsonResponse:
        """Send a ``GET`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            period: Enum: ``all``, ``yearly``, ``quarterly``, ``monthly``, ``weekly``, ``daily``
            per_page: Maximum number of topics returned, between 1-100
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_top_topics(
            api_key, api_username, period=period, per_page=per_page, request_options=request_options
        ).unwrap()

    def remove_topic(
        self, id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            specific posts

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.remove_topic(id, api_key, api_username, request_options=request_options).unwrap()

    def set_notification_level(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TNotificationsJsonRequest | TNotificationsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TNotificationsJsonResponse:
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
        return self._with_raw_response.set_notification_level(
            id, api_key, api_username, body=body, request_options=request_options
        ).unwrap()

    def update_topic(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TJsonRequest | TJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TJsonResponse1:
        """Send a ``PUT`` request.

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
        return self._with_raw_response.update_topic(
            id, api_key, api_username, body=body, request_options=request_options
        ).unwrap()

    def update_topic_status(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TStatusJsonRequest | TStatusJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TStatusJsonResponse:
        """Send a ``PUT`` request.

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
        return self._with_raw_response.update_topic_status(
            id, api_key, api_username, body=body, request_options=request_options
        ).unwrap()

    def update_topic_timestamp(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TChangeTimestampJsonRequest | TChangeTimestampJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TChangeTimestampJsonResponse:
        """Send a ``PUT`` request.

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
        return self._with_raw_response.update_topic_timestamp(
            id, api_key, api_username, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TopicsWithRawResponse:
        return self._with_raw_response


class AsyncTopics:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncTopicsWithRawResponse(client, server)

    async def bookmark_topic(
        self, id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            topic updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.bookmark_topic(id, api_key, api_username, request_options=request_options)
        ).unwrap()

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

    async def create_topic_timer(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TTimerJsonRequest | TTimerJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TTimerJsonResponse:
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
            await self._with_raw_response.create_topic_timer(
                id, api_key, api_username, body=body, request_options=request_options
            )
        ).unwrap()

    async def get_specific_posts_from_topic(
        self, id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TPostsJsonResponse:
        """Send a ``GET`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            specific posts

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_specific_posts_from_topic(
                id, api_key, api_username, request_options=request_options
            )
        ).unwrap()

    async def get_topic(
        self, id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TJsonResponse:
        """Send a ``GET`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            specific posts

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_topic(id, api_key, api_username, request_options=request_options)
        ).unwrap()

    async def get_topic_by_external_id(
        self, external_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Send a ``GET`` request.

        Args:
            external_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_topic_by_external_id(external_id, request_options=request_options)
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

    async def list_latest_topics(
        self,
        api_key: str,
        api_username: str,
        *,
        order: str | None = None,
        ascending: str | None = None,
        per_page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LatestJsonResponse:
        """Send a ``GET`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            order: Enum: ``default``, ``created``, ``activity``, ``views``, ``posts``, ``category``, ``likes``,
                ``op_likes``, ``posters``
            ascending: Defaults to ``desc``, add ``ascending=true`` to sort asc
            per_page: Maximum number of topics returned, between 1-100
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            topic updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_latest_topics(
                api_key,
                api_username,
                order=order,
                ascending=ascending,
                per_page=per_page,
                request_options=request_options,
            )
        ).unwrap()

    async def list_top_topics(
        self,
        api_key: str,
        api_username: str,
        *,
        period: str | None = None,
        per_page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TopJsonResponse:
        """Send a ``GET`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            period: Enum: ``all``, ``yearly``, ``quarterly``, ``monthly``, ``weekly``, ``daily``
            per_page: Maximum number of topics returned, between 1-100
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_top_topics(
                api_key, api_username, period=period, per_page=per_page, request_options=request_options
            )
        ).unwrap()

    async def remove_topic(
        self, id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Send a ``DELETE`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            specific posts

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.remove_topic(id, api_key, api_username, request_options=request_options)
        ).unwrap()

    async def set_notification_level(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TNotificationsJsonRequest | TNotificationsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TNotificationsJsonResponse:
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
            await self._with_raw_response.set_notification_level(
                id, api_key, api_username, body=body, request_options=request_options
            )
        ).unwrap()

    async def update_topic(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TJsonRequest | TJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TJsonResponse1:
        """Send a ``PUT`` request.

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
            await self._with_raw_response.update_topic(
                id, api_key, api_username, body=body, request_options=request_options
            )
        ).unwrap()

    async def update_topic_status(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TStatusJsonRequest | TStatusJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TStatusJsonResponse:
        """Send a ``PUT`` request.

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
            await self._with_raw_response.update_topic_status(
                id, api_key, api_username, body=body, request_options=request_options
            )
        ).unwrap()

    async def update_topic_timestamp(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TChangeTimestampJsonRequest | TChangeTimestampJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TChangeTimestampJsonResponse:
        """Send a ``PUT`` request.

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
            await self._with_raw_response.update_topic_timestamp(
                id, api_key, api_username, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTopicsWithRawResponse:
        return self._with_raw_response


class TopicsWithRawResponse(BaseRawResponse[RawClient, Server]):
    def bookmark_topic(
        self, id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/t/{id}/bookmark.json"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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

    def create_topic_timer(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TTimerJsonRequest | TTimerJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TTimerJsonResponse, RawError]:
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
            url_template=self._server.default("/t/{id}/timer.json"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[TTimerJsonRequest | TTimerJsonRequestDict | None](body),
            decoder=json_decoder[TTimerJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_specific_posts_from_topic(
        self, id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TPostsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/t/{id}/posts.json"),
            path_params=[param[str]("id", id)],
            headers=[param[str]("Api-Key", api_key), param[str]("Api-Username", api_username)],
            decoder=json_decoder[TPostsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_topic(
        self, id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/t/{id}.json"),
            path_params=[param[str]("id", id)],
            headers=[param[str]("Api-Key", api_key), param[str]("Api-Username", api_username)],
            decoder=json_decoder[TJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_topic_by_external_id(
        self, external_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``GET`` request.

        Args:
            external_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/t/external_id/{external_id}.json"),
            path_params=[param[str]("external_id", external_id)],
            decoder=empty_response,
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

    def list_latest_topics(
        self,
        api_key: str,
        api_username: str,
        *,
        order: str | None = None,
        ascending: str | None = None,
        per_page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LatestJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            order: Enum: ``default``, ``created``, ``activity``, ``views``, ``posts``, ``category``, ``likes``,
                ``op_likes``, ``posters``
            ascending: Defaults to ``desc``, add ``ascending=true`` to sort asc
            per_page: Maximum number of topics returned, between 1-100
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/latest.json"),
            query_params=[
                param[str | None]("order", order),
                param[str | None]("ascending", ascending),
                param[int | None]("per_page", per_page),
            ],
            headers=[param[str]("Api-Key", api_key), param[str]("Api-Username", api_username)],
            decoder=json_decoder[LatestJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_top_topics(
        self,
        api_key: str,
        api_username: str,
        *,
        period: str | None = None,
        per_page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TopJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            period: Enum: ``all``, ``yearly``, ``quarterly``, ``monthly``, ``weekly``, ``daily``
            per_page: Maximum number of topics returned, between 1-100
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/top.json"),
            query_params=[param[str | None]("period", period), param[int | None]("per_page", per_page)],
            headers=[param[str]("Api-Key", api_key), param[str]("Api-Username", api_username)],
            decoder=json_decoder[TopJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def remove_topic(
        self, id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/t/{id}.json"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def set_notification_level(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TNotificationsJsonRequest | TNotificationsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TNotificationsJsonResponse, RawError]:
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
            url_template=self._server.default("/t/{id}/notifications.json"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[TNotificationsJsonRequest | TNotificationsJsonRequestDict | None](body),
            decoder=json_decoder[TNotificationsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_topic(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TJsonRequest | TJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TJsonResponse1, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/t/-/{id}.json"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[TJsonRequest | TJsonRequestDict | None](body),
            decoder=json_decoder[TJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_topic_status(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TStatusJsonRequest | TStatusJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TStatusJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/t/{id}/status.json"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[TStatusJsonRequest | TStatusJsonRequestDict | None](body),
            decoder=json_decoder[TStatusJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_topic_timestamp(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TChangeTimestampJsonRequest | TChangeTimestampJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TChangeTimestampJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/t/{id}/change-timestamp.json"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[TChangeTimestampJsonRequest | TChangeTimestampJsonRequestDict | None](body),
            decoder=json_decoder[TChangeTimestampJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTopicsWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def bookmark_topic(
        self, id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/t/{id}/bookmark.json"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

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

    async def create_topic_timer(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TTimerJsonRequest | TTimerJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TTimerJsonResponse, RawError]:
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
            url_template=self._server.default("/t/{id}/timer.json"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[TTimerJsonRequest | TTimerJsonRequestDict | None](body),
            decoder=json_decoder[TTimerJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_specific_posts_from_topic(
        self, id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TPostsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/t/{id}/posts.json"),
            path_params=[param[str]("id", id)],
            headers=[param[str]("Api-Key", api_key), param[str]("Api-Username", api_username)],
            decoder=json_decoder[TPostsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_topic(
        self, id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/t/{id}.json"),
            path_params=[param[str]("id", id)],
            headers=[param[str]("Api-Key", api_key), param[str]("Api-Username", api_username)],
            decoder=json_decoder[TJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_topic_by_external_id(
        self, external_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``GET`` request.

        Args:
            external_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/t/external_id/{external_id}.json"),
            path_params=[param[str]("external_id", external_id)],
            decoder=empty_response,
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

    async def list_latest_topics(
        self,
        api_key: str,
        api_username: str,
        *,
        order: str | None = None,
        ascending: str | None = None,
        per_page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LatestJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            order: Enum: ``default``, ``created``, ``activity``, ``views``, ``posts``, ``category``, ``likes``,
                ``op_likes``, ``posters``
            ascending: Defaults to ``desc``, add ``ascending=true`` to sort asc
            per_page: Maximum number of topics returned, between 1-100
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/latest.json"),
            query_params=[
                param[str | None]("order", order),
                param[str | None]("ascending", ascending),
                param[int | None]("per_page", per_page),
            ],
            headers=[param[str]("Api-Key", api_key), param[str]("Api-Username", api_username)],
            decoder=json_decoder[LatestJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_top_topics(
        self,
        api_key: str,
        api_username: str,
        *,
        period: str | None = None,
        per_page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TopJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            period: Enum: ``all``, ``yearly``, ``quarterly``, ``monthly``, ``weekly``, ``daily``
            per_page: Maximum number of topics returned, between 1-100
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/top.json"),
            query_params=[param[str | None]("period", period), param[int | None]("per_page", per_page)],
            headers=[param[str]("Api-Key", api_key), param[str]("Api-Username", api_username)],
            decoder=json_decoder[TopJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def remove_topic(
        self, id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Send a ``DELETE`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/t/{id}.json"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def set_notification_level(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TNotificationsJsonRequest | TNotificationsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TNotificationsJsonResponse, RawError]:
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
            url_template=self._server.default("/t/{id}/notifications.json"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[TNotificationsJsonRequest | TNotificationsJsonRequestDict | None](body),
            decoder=json_decoder[TNotificationsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_topic(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TJsonRequest | TJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TJsonResponse1, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/t/-/{id}.json"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[TJsonRequest | TJsonRequestDict | None](body),
            decoder=json_decoder[TJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_topic_status(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TStatusJsonRequest | TStatusJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TStatusJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/t/{id}/status.json"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[TStatusJsonRequest | TStatusJsonRequestDict | None](body),
            decoder=json_decoder[TStatusJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_topic_timestamp(
        self,
        id: str,
        api_key: str,
        api_username: str,
        *,
        body: TChangeTimestampJsonRequest | TChangeTimestampJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TChangeTimestampJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/t/{id}/change-timestamp.json"),
            path_params=[param[str]("id", id)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[TChangeTimestampJsonRequest | TChangeTimestampJsonRequestDict | None](body),
            decoder=json_decoder[TChangeTimestampJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
