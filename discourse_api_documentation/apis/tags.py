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
from ..models.tag_groups_json_request import TagGroupsJsonRequest, TagGroupsJsonRequestDict
from ..models.tag_groups_json_request1 import TagGroupsJsonRequest1, TagGroupsJsonRequest1Dict
from ..models.tag_groups_json_response import TagGroupsJsonResponse
from ..models.tag_groups_json_response1 import TagGroupsJsonResponse1
from ..models.tag_groups_json_response2 import TagGroupsJsonResponse2
from ..models.tag_groups_json_response3 import TagGroupsJsonResponse3
from ..models.tag_json_response import TagJsonResponse
from ..models.tags_json_response import TagsJsonResponse
from ..server.server import Server


class Tags:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = TagsWithRawResponse(client, server)

    def create_tag_group(
        self,
        *,
        body: TagGroupsJsonRequest | TagGroupsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TagGroupsJsonResponse1:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            tag group created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_tag_group(body=body, request_options=request_options).unwrap()

    def get_tag(self, name: str, *, request_options: RequestOptionsOrDict | None = None) -> TagJsonResponse:
        """Send a ``GET`` request.

        Args:
            name: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            notifications

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_tag(name, request_options=request_options).unwrap()

    def get_tag_group(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> TagGroupsJsonResponse2:
        """Send a ``GET`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            notifications

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_tag_group(id, request_options=request_options).unwrap()

    def list_tag_groups(self, *, request_options: RequestOptionsOrDict | None = None) -> TagGroupsJsonResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            tags

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_tag_groups(request_options=request_options).unwrap()

    def list_tags(self, *, request_options: RequestOptionsOrDict | None = None) -> TagsJsonResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            notifications

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_tags(request_options=request_options).unwrap()

    def update_tag_group(
        self,
        id: str,
        *,
        body: TagGroupsJsonRequest1 | TagGroupsJsonRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TagGroupsJsonResponse3:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Tag group updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_tag_group(id, body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> TagsWithRawResponse:
        return self._with_raw_response


class AsyncTags:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncTagsWithRawResponse(client, server)

    async def create_tag_group(
        self,
        *,
        body: TagGroupsJsonRequest | TagGroupsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TagGroupsJsonResponse1:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            tag group created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_tag_group(body=body, request_options=request_options)).unwrap()

    async def get_tag(self, name: str, *, request_options: RequestOptionsOrDict | None = None) -> TagJsonResponse:
        """Send a ``GET`` request.

        Args:
            name: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            notifications

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_tag(name, request_options=request_options)).unwrap()

    async def get_tag_group(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TagGroupsJsonResponse2:
        """Send a ``GET`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            notifications

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_tag_group(id, request_options=request_options)).unwrap()

    async def list_tag_groups(self, *, request_options: RequestOptionsOrDict | None = None) -> TagGroupsJsonResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            tags

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.list_tag_groups(request_options=request_options)).unwrap()

    async def list_tags(self, *, request_options: RequestOptionsOrDict | None = None) -> TagsJsonResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            notifications

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.list_tags(request_options=request_options)).unwrap()

    async def update_tag_group(
        self,
        id: str,
        *,
        body: TagGroupsJsonRequest1 | TagGroupsJsonRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TagGroupsJsonResponse3:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Tag group updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.update_tag_group(id, body=body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncTagsWithRawResponse:
        return self._with_raw_response


class TagsWithRawResponse(BaseRawResponse[RawClient, Server]):
    def create_tag_group(
        self,
        *,
        body: TagGroupsJsonRequest | TagGroupsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TagGroupsJsonResponse1, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/tag_groups.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TagGroupsJsonRequest | TagGroupsJsonRequestDict | None](body),
            decoder=json_decoder[TagGroupsJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_tag(
        self, name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TagJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            name: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tag/{name}.json"),
            path_params=[param[str]("name", name)],
            decoder=json_decoder[TagJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_tag_group(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TagGroupsJsonResponse2, RawError]:
        """Send a ``GET`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tag_groups/{id}.json"),
            path_params=[param[str]("id", id)],
            decoder=json_decoder[TagGroupsJsonResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_tag_groups(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TagGroupsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tag_groups.json"),
            decoder=json_decoder[TagGroupsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_tags(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TagsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tags.json"),
            decoder=json_decoder[TagsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_tag_group(
        self,
        id: str,
        *,
        body: TagGroupsJsonRequest1 | TagGroupsJsonRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TagGroupsJsonResponse3, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/tag_groups/{id}.json"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TagGroupsJsonRequest1 | TagGroupsJsonRequest1Dict | None](body),
            decoder=json_decoder[TagGroupsJsonResponse3],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTagsWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def create_tag_group(
        self,
        *,
        body: TagGroupsJsonRequest | TagGroupsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TagGroupsJsonResponse1, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/tag_groups.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TagGroupsJsonRequest | TagGroupsJsonRequestDict | None](body),
            decoder=json_decoder[TagGroupsJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_tag(
        self, name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TagJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            name: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tag/{name}.json"),
            path_params=[param[str]("name", name)],
            decoder=json_decoder[TagJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_tag_group(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TagGroupsJsonResponse2, RawError]:
        """Send a ``GET`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tag_groups/{id}.json"),
            path_params=[param[str]("id", id)],
            decoder=json_decoder[TagGroupsJsonResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_tag_groups(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TagGroupsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tag_groups.json"),
            decoder=json_decoder[TagGroupsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_tags(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TagsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/tags.json"),
            decoder=json_decoder[TagsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_tag_group(
        self,
        id: str,
        *,
        body: TagGroupsJsonRequest1 | TagGroupsJsonRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TagGroupsJsonResponse3, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/tag_groups/{id}.json"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TagGroupsJsonRequest1 | TagGroupsJsonRequest1Dict | None](body),
            decoder=json_decoder[TagGroupsJsonResponse3],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
