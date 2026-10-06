from __future__ import annotations

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    async_json_decoder,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.search_json_response import SearchJsonResponse
from ..server.server import Server


class Search:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = SearchWithRawResponse(client, server)

    def search(
        self, *, q: str | None = None, page: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> SearchJsonResponse:
        r"""Send a ``GET`` request.

        Args:
            q: The query string needs to be url encoded and is made up of the following options: - Search term. This is
                just a string. Usually it would be the first item in the query. - ``@<username>``: Use the ``@``
                followed by the username to specify posts by this user. - ``#<category>``: Use the ``#`` followed by the
                category slug to search within this category. - ``tags:``: ``api,solved`` or for posts that have all the
                specified tags ``api+solved``. - ``before:``: ``yyyy-mm-dd`` - ``after:``: ``yyyy-mm-dd`` - ``order:``:
                ``latest``, ``likes``, ``views``, ``latest_topic`` - ``assigned:``: username (without ``@``) - ``in:``:
                ``title``, ``likes``, ``personal``, ``messages``, ``seen``, ``unseen``, ``posted``, ``created``,
                ``watching``, ``tracking``, ``bookmarks``, ``assigned``, ``unassigned``, ``first``, ``pinned``, ``wiki``
                - ``with:``: ``images`` - ``status:``: ``open``, ``closed``, ``public``, ``archived``, ``noreplies``,
                ``single_user``, ``solved``, ``unsolved`` - ``group:``: group_name or group_id - ``group_messages:``:
                group_name or group_id - ``min_posts:``: 1 - ``max_posts:``: 10 - ``min_views:``: 1 - ``max_views:``: 10
                If you are using cURL you can use the ``-G`` and the ``--data-urlencode`` flags to encode the query: ```
                curl -i -sS -X GET -G "http://localhost:3000/search.json" \ --data-urlencode 'q=wordpress @scossar #fun
                after:2020-01-01' ```
            page: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search(q=q, page=page, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SearchWithRawResponse:
        return self._with_raw_response


class AsyncSearch:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncSearchWithRawResponse(client, server)

    async def search(
        self, *, q: str | None = None, page: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> SearchJsonResponse:
        r"""Send a ``GET`` request.

        Args:
            q: The query string needs to be url encoded and is made up of the following options: - Search term. This is
                just a string. Usually it would be the first item in the query. - ``@<username>``: Use the ``@``
                followed by the username to specify posts by this user. - ``#<category>``: Use the ``#`` followed by the
                category slug to search within this category. - ``tags:``: ``api,solved`` or for posts that have all the
                specified tags ``api+solved``. - ``before:``: ``yyyy-mm-dd`` - ``after:``: ``yyyy-mm-dd`` - ``order:``:
                ``latest``, ``likes``, ``views``, ``latest_topic`` - ``assigned:``: username (without ``@``) - ``in:``:
                ``title``, ``likes``, ``personal``, ``messages``, ``seen``, ``unseen``, ``posted``, ``created``,
                ``watching``, ``tracking``, ``bookmarks``, ``assigned``, ``unassigned``, ``first``, ``pinned``, ``wiki``
                - ``with:``: ``images`` - ``status:``: ``open``, ``closed``, ``public``, ``archived``, ``noreplies``,
                ``single_user``, ``solved``, ``unsolved`` - ``group:``: group_name or group_id - ``group_messages:``:
                group_name or group_id - ``min_posts:``: 1 - ``max_posts:``: 10 - ``min_views:``: 1 - ``max_views:``: 10
                If you are using cURL you can use the ``-G`` and the ``--data-urlencode`` flags to encode the query: ```
                curl -i -sS -X GET -G "http://localhost:3000/search.json" \ --data-urlencode 'q=wordpress @scossar #fun
                after:2020-01-01' ```
            page: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.search(q=q, page=page, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncSearchWithRawResponse:
        return self._with_raw_response


class SearchWithRawResponse(BaseRawResponse[RawClient, Server]):
    def search(
        self, *, q: str | None = None, page: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SearchJsonResponse, RawError]:
        r"""Send a ``GET`` request.

        Args:
            q: The query string needs to be url encoded and is made up of the following options: - Search term. This is
                just a string. Usually it would be the first item in the query. - ``@<username>``: Use the ``@``
                followed by the username to specify posts by this user. - ``#<category>``: Use the ``#`` followed by the
                category slug to search within this category. - ``tags:``: ``api,solved`` or for posts that have all the
                specified tags ``api+solved``. - ``before:``: ``yyyy-mm-dd`` - ``after:``: ``yyyy-mm-dd`` - ``order:``:
                ``latest``, ``likes``, ``views``, ``latest_topic`` - ``assigned:``: username (without ``@``) - ``in:``:
                ``title``, ``likes``, ``personal``, ``messages``, ``seen``, ``unseen``, ``posted``, ``created``,
                ``watching``, ``tracking``, ``bookmarks``, ``assigned``, ``unassigned``, ``first``, ``pinned``, ``wiki``
                - ``with:``: ``images`` - ``status:``: ``open``, ``closed``, ``public``, ``archived``, ``noreplies``,
                ``single_user``, ``solved``, ``unsolved`` - ``group:``: group_name or group_id - ``group_messages:``:
                group_name or group_id - ``min_posts:``: 1 - ``max_posts:``: 10 - ``min_views:``: 1 - ``max_views:``: 10
                If you are using cURL you can use the ``-G`` and the ``--data-urlencode`` flags to encode the query: ```
                curl -i -sS -X GET -G "http://localhost:3000/search.json" \ --data-urlencode 'q=wordpress @scossar #fun
                after:2020-01-01' ```
            page: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search.json"),
            query_params=[param[str | None]("q", q), param[int | None]("page", page)],
            decoder=json_decoder[SearchJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSearchWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def search(
        self, *, q: str | None = None, page: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SearchJsonResponse, RawError]:
        r"""Send a ``GET`` request.

        Args:
            q: The query string needs to be url encoded and is made up of the following options: - Search term. This is
                just a string. Usually it would be the first item in the query. - ``@<username>``: Use the ``@``
                followed by the username to specify posts by this user. - ``#<category>``: Use the ``#`` followed by the
                category slug to search within this category. - ``tags:``: ``api,solved`` or for posts that have all the
                specified tags ``api+solved``. - ``before:``: ``yyyy-mm-dd`` - ``after:``: ``yyyy-mm-dd`` - ``order:``:
                ``latest``, ``likes``, ``views``, ``latest_topic`` - ``assigned:``: username (without ``@``) - ``in:``:
                ``title``, ``likes``, ``personal``, ``messages``, ``seen``, ``unseen``, ``posted``, ``created``,
                ``watching``, ``tracking``, ``bookmarks``, ``assigned``, ``unassigned``, ``first``, ``pinned``, ``wiki``
                - ``with:``: ``images`` - ``status:``: ``open``, ``closed``, ``public``, ``archived``, ``noreplies``,
                ``single_user``, ``solved``, ``unsolved`` - ``group:``: group_name or group_id - ``group_messages:``:
                group_name or group_id - ``min_posts:``: 1 - ``max_posts:``: 10 - ``min_views:``: 1 - ``max_views:``: 10
                If you are using cURL you can use the ``-G`` and the ``--data-urlencode`` flags to encode the query: ```
                curl -i -sS -X GET -G "http://localhost:3000/search.json" \ --data-urlencode 'q=wordpress @scossar #fun
                after:2020-01-01' ```
            page: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search.json"),
            query_params=[param[str | None]("q", q), param[int | None]("page", page)],
            decoder=async_json_decoder[SearchJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
