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
from ..models.c_json_response import CJsonResponse
from ..models.c_show_json_response import CShowJsonResponse
from ..models.categories_json_request import CategoriesJsonRequest, CategoriesJsonRequestDict
from ..models.categories_json_request1 import CategoriesJsonRequest1, CategoriesJsonRequest1Dict
from ..models.categories_json_response import CategoriesJsonResponse
from ..models.categories_json_response1 import CategoriesJsonResponse1
from ..models.categories_json_response2 import CategoriesJsonResponse2
from ..models.site_json_response import SiteJsonResponse
from ..server.server import Server


class Categories:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = CategoriesWithRawResponse(client, server)

    def create_category(
        self,
        *,
        body: CategoriesJsonRequest | CategoriesJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CategoriesJsonResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_category(body=body, request_options=request_options).unwrap()

    def get_category(self, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> CShowJsonResponse:
        """Send a ``GET`` request.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_category(id_, request_options=request_options).unwrap()

    def get_site(self, *, request_options: RequestOptionsOrDict | None = None) -> SiteJsonResponse:
        """Can be used to fetch all categories and subcategories

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_site(request_options=request_options).unwrap()

    def list_categories(
        self, *, include_subcategories: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> CategoriesJsonResponse1:
        """Send a ``GET`` request.

        Args:
            include_subcategories: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_categories(
            include_subcategories=include_subcategories, request_options=request_options
        ).unwrap()

    def list_category_topics(
        self, slug: str, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> CJsonResponse:
        """Send a ``GET`` request.

        Args:
            slug: Value sent with the request.
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_category_topics(slug, id_, request_options=request_options).unwrap()

    def update_category(
        self,
        id_: int,
        *,
        body: CategoriesJsonRequest1 | CategoriesJsonRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CategoriesJsonResponse2:
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
        return self._with_raw_response.update_category(id_, body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> CategoriesWithRawResponse:
        return self._with_raw_response


class AsyncCategories:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncCategoriesWithRawResponse(client, server)

    async def create_category(
        self,
        *,
        body: CategoriesJsonRequest | CategoriesJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CategoriesJsonResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_category(body=body, request_options=request_options)).unwrap()

    async def get_category(self, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> CShowJsonResponse:
        """Send a ``GET`` request.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_category(id_, request_options=request_options)).unwrap()

    async def get_site(self, *, request_options: RequestOptionsOrDict | None = None) -> SiteJsonResponse:
        """Can be used to fetch all categories and subcategories

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_site(request_options=request_options)).unwrap()

    async def list_categories(
        self, *, include_subcategories: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> CategoriesJsonResponse1:
        """Send a ``GET`` request.

        Args:
            include_subcategories: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_categories(
                include_subcategories=include_subcategories, request_options=request_options
            )
        ).unwrap()

    async def list_category_topics(
        self, slug: str, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> CJsonResponse:
        """Send a ``GET`` request.

        Args:
            slug: Value sent with the request.
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.list_category_topics(slug, id_, request_options=request_options)).unwrap()

    async def update_category(
        self,
        id_: int,
        *,
        body: CategoriesJsonRequest1 | CategoriesJsonRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CategoriesJsonResponse2:
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
        return (await self._with_raw_response.update_category(id_, body=body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncCategoriesWithRawResponse:
        return self._with_raw_response


class CategoriesWithRawResponse(BaseRawResponse[RawClient, Server]):
    def create_category(
        self,
        *,
        body: CategoriesJsonRequest | CategoriesJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CategoriesJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/categories.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CategoriesJsonRequest | CategoriesJsonRequestDict | None](body),
            decoder=json_decoder[CategoriesJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_category(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CShowJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/c/{id}/show.json"),
            path_params=[param[int]("id", id_)],
            decoder=json_decoder[CShowJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_site(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SiteJsonResponse, RawError]:
        """Can be used to fetch all categories and subcategories

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/site.json"),
            decoder=json_decoder[SiteJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_categories(
        self, *, include_subcategories: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CategoriesJsonResponse1, RawError]:
        """Send a ``GET`` request.

        Args:
            include_subcategories: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/categories.json"),
            query_params=[param[bool | None]("include_subcategories", include_subcategories)],
            decoder=json_decoder[CategoriesJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_category_topics(
        self, slug: str, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            slug: Value sent with the request.
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/c/{slug}/{id}.json"),
            path_params=[param[str]("slug", slug), param[int]("id", id_)],
            decoder=json_decoder[CJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_category(
        self,
        id_: int,
        *,
        body: CategoriesJsonRequest1 | CategoriesJsonRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CategoriesJsonResponse2, RawError]:
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
            url_template=self._server.default("/categories/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CategoriesJsonRequest1 | CategoriesJsonRequest1Dict | None](body),
            decoder=json_decoder[CategoriesJsonResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCategoriesWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def create_category(
        self,
        *,
        body: CategoriesJsonRequest | CategoriesJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CategoriesJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/categories.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CategoriesJsonRequest | CategoriesJsonRequestDict | None](body),
            decoder=async_json_decoder[CategoriesJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_category(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CShowJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/c/{id}/show.json"),
            path_params=[param[int]("id", id_)],
            decoder=async_json_decoder[CShowJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_site(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SiteJsonResponse, RawError]:
        """Can be used to fetch all categories and subcategories

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/site.json"),
            decoder=async_json_decoder[SiteJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_categories(
        self, *, include_subcategories: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CategoriesJsonResponse1, RawError]:
        """Send a ``GET`` request.

        Args:
            include_subcategories: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/categories.json"),
            query_params=[param[bool | None]("include_subcategories", include_subcategories)],
            decoder=async_json_decoder[CategoriesJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_category_topics(
        self, slug: str, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            slug: Value sent with the request.
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/c/{slug}/{id}.json"),
            path_params=[param[str]("slug", slug), param[int]("id", id_)],
            decoder=async_json_decoder[CJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_category(
        self,
        id_: int,
        *,
        body: CategoriesJsonRequest1 | CategoriesJsonRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CategoriesJsonResponse2, RawError]:
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
            url_template=self._server.default("/categories/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CategoriesJsonRequest1 | CategoriesJsonRequest1Dict | None](body),
            decoder=async_json_decoder[CategoriesJsonResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
