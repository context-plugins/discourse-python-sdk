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
    raw_error_response,
)
from ..models.site_basic_info_json_response import SiteBasicInfoJsonResponse
from ..models.site_json_response import SiteJsonResponse
from ..server.server import Server


class Site:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = SiteWithRawResponse(client, server)

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

    def get_site_basic_info(self, *, request_options: RequestOptionsOrDict | None = None) -> SiteBasicInfoJsonResponse:
        """Can be used to fetch basic info about a site

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_site_basic_info(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SiteWithRawResponse:
        return self._with_raw_response


class AsyncSite:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncSiteWithRawResponse(client, server)

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

    async def get_site_basic_info(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> SiteBasicInfoJsonResponse:
        """Can be used to fetch basic info about a site

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_site_basic_info(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncSiteWithRawResponse:
        return self._with_raw_response


class SiteWithRawResponse(BaseRawResponse[RawClient, Server]):
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

    def get_site_basic_info(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SiteBasicInfoJsonResponse, RawError]:
        """Can be used to fetch basic info about a site

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/site/basic-info.json"),
            decoder=json_decoder[SiteBasicInfoJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSiteWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
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

    async def get_site_basic_info(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SiteBasicInfoJsonResponse, RawError]:
        """Can be used to fetch basic info about a site

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/site/basic-info.json"),
            decoder=async_json_decoder[SiteBasicInfoJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
