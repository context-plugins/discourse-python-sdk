from __future__ import annotations

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    RFC3339DateTime,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.discourse_post_event_events_json_response import DiscoursePostEventEventsJsonResponse
from ..models.enums.include_details import IncludeDetailsOrStr
from ..models.enums.include_subcategories import IncludeSubcategoriesOrStr
from ..models.enums.order import OrderOrStr
from ..server.server import Server


class DiscourseCalendarEvents:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = DiscourseCalendarEventsWithRawResponse(client, server)

    def export_events_ics(
        self,
        *,
        category_id: int | None = None,
        include_subcategories: IncludeSubcategoriesOrStr | None = None,
        attending_user: str | None = None,
        before: RFC3339DateTime | None = None,
        after: RFC3339DateTime | None = None,
        order: OrderOrStr | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``GET`` request.

        Args:
            category_id: Filter events by category ID
            include_subcategories: Include events from subcategories when filtering by category
            attending_user: Filter to events where the specified user (username) has RSVP'd as going
            before: Return events starting before this date/time (ISO 8601 format)
            after: Return events starting after this date/time (ISO 8601 format)
            order: Sort order for events by start date (default: asc)
            limit: Maximum number of events to return (default: 200)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            iCalendar file

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.export_events_ics(
            category_id=category_id,
            include_subcategories=include_subcategories,
            attending_user=attending_user,
            before=before,
            after=after,
            order=order,
            limit=limit,
            request_options=request_options,
        ).unwrap()

    def list_events(
        self,
        *,
        include_details: IncludeDetailsOrStr | None = None,
        category_id: int | None = None,
        include_subcategories: IncludeSubcategoriesOrStr | None = None,
        post_id: int | None = None,
        attending_user: str | None = None,
        before: RFC3339DateTime | None = None,
        after: RFC3339DateTime | None = None,
        order: OrderOrStr | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DiscoursePostEventEventsJsonResponse:
        """Send a ``GET`` request.

        Args:
            include_details: Include detailed event information (creator, invitees, stats, etc.)
            category_id: Filter events by category ID
            include_subcategories: Include events from subcategories when filtering by category
            post_id: Filter to events associated with a specific post ID
            attending_user: Filter to events where the specified user (username) has RSVP'd as going
            before: Return events starting before this date/time (ISO 8601 format)
            after: Return events starting after this date/time (ISO 8601 format)
            order: Sort order for events by start date (default: asc)
            limit: Maximum number of events to return (default: 200)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response (detailed)

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_events(
            include_details=include_details,
            category_id=category_id,
            include_subcategories=include_subcategories,
            post_id=post_id,
            attending_user=attending_user,
            before=before,
            after=after,
            order=order,
            limit=limit,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> DiscourseCalendarEventsWithRawResponse:
        return self._with_raw_response


class AsyncDiscourseCalendarEvents:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncDiscourseCalendarEventsWithRawResponse(client, server)

    async def export_events_ics(
        self,
        *,
        category_id: int | None = None,
        include_subcategories: IncludeSubcategoriesOrStr | None = None,
        attending_user: str | None = None,
        before: RFC3339DateTime | None = None,
        after: RFC3339DateTime | None = None,
        order: OrderOrStr | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``GET`` request.

        Args:
            category_id: Filter events by category ID
            include_subcategories: Include events from subcategories when filtering by category
            attending_user: Filter to events where the specified user (username) has RSVP'd as going
            before: Return events starting before this date/time (ISO 8601 format)
            after: Return events starting after this date/time (ISO 8601 format)
            order: Sort order for events by start date (default: asc)
            limit: Maximum number of events to return (default: 200)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            iCalendar file

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.export_events_ics(
                category_id=category_id,
                include_subcategories=include_subcategories,
                attending_user=attending_user,
                before=before,
                after=after,
                order=order,
                limit=limit,
                request_options=request_options,
            )
        ).unwrap()

    async def list_events(
        self,
        *,
        include_details: IncludeDetailsOrStr | None = None,
        category_id: int | None = None,
        include_subcategories: IncludeSubcategoriesOrStr | None = None,
        post_id: int | None = None,
        attending_user: str | None = None,
        before: RFC3339DateTime | None = None,
        after: RFC3339DateTime | None = None,
        order: OrderOrStr | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DiscoursePostEventEventsJsonResponse:
        """Send a ``GET`` request.

        Args:
            include_details: Include detailed event information (creator, invitees, stats, etc.)
            category_id: Filter events by category ID
            include_subcategories: Include events from subcategories when filtering by category
            post_id: Filter to events associated with a specific post ID
            attending_user: Filter to events where the specified user (username) has RSVP'd as going
            before: Return events starting before this date/time (ISO 8601 format)
            after: Return events starting after this date/time (ISO 8601 format)
            order: Sort order for events by start date (default: asc)
            limit: Maximum number of events to return (default: 200)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response (detailed)

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_events(
                include_details=include_details,
                category_id=category_id,
                include_subcategories=include_subcategories,
                post_id=post_id,
                attending_user=attending_user,
                before=before,
                after=after,
                order=order,
                limit=limit,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDiscourseCalendarEventsWithRawResponse:
        return self._with_raw_response


class DiscourseCalendarEventsWithRawResponse(BaseRawResponse[RawClient, Server]):
    def export_events_ics(
        self,
        *,
        category_id: int | None = None,
        include_subcategories: IncludeSubcategoriesOrStr | None = None,
        attending_user: str | None = None,
        before: RFC3339DateTime | None = None,
        after: RFC3339DateTime | None = None,
        order: OrderOrStr | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``GET`` request.

        Args:
            category_id: Filter events by category ID
            include_subcategories: Include events from subcategories when filtering by category
            attending_user: Filter to events where the specified user (username) has RSVP'd as going
            before: Return events starting before this date/time (ISO 8601 format)
            after: Return events starting after this date/time (ISO 8601 format)
            order: Sort order for events by start date (default: asc)
            limit: Maximum number of events to return (default: 200)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/discourse-post-event/events.ics"),
            query_params=[
                param[int | None]("category_id", category_id),
                param[IncludeSubcategoriesOrStr | None]("include_subcategories", include_subcategories),
                param[str | None]("attending_user", attending_user),
                param[RFC3339DateTime | None]("before", before),
                param[RFC3339DateTime | None]("after", after),
                param[OrderOrStr | None]("order", order),
                param[int | None]("limit", limit),
            ],
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_events(
        self,
        *,
        include_details: IncludeDetailsOrStr | None = None,
        category_id: int | None = None,
        include_subcategories: IncludeSubcategoriesOrStr | None = None,
        post_id: int | None = None,
        attending_user: str | None = None,
        before: RFC3339DateTime | None = None,
        after: RFC3339DateTime | None = None,
        order: OrderOrStr | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DiscoursePostEventEventsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            include_details: Include detailed event information (creator, invitees, stats, etc.)
            category_id: Filter events by category ID
            include_subcategories: Include events from subcategories when filtering by category
            post_id: Filter to events associated with a specific post ID
            attending_user: Filter to events where the specified user (username) has RSVP'd as going
            before: Return events starting before this date/time (ISO 8601 format)
            after: Return events starting after this date/time (ISO 8601 format)
            order: Sort order for events by start date (default: asc)
            limit: Maximum number of events to return (default: 200)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/discourse-post-event/events.json"),
            query_params=[
                param[IncludeDetailsOrStr | None]("include_details", include_details),
                param[int | None]("category_id", category_id),
                param[IncludeSubcategoriesOrStr | None]("include_subcategories", include_subcategories),
                param[int | None]("post_id", post_id),
                param[str | None]("attending_user", attending_user),
                param[RFC3339DateTime | None]("before", before),
                param[RFC3339DateTime | None]("after", after),
                param[OrderOrStr | None]("order", order),
                param[int | None]("limit", limit),
            ],
            decoder=json_decoder[DiscoursePostEventEventsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncDiscourseCalendarEventsWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def export_events_ics(
        self,
        *,
        category_id: int | None = None,
        include_subcategories: IncludeSubcategoriesOrStr | None = None,
        attending_user: str | None = None,
        before: RFC3339DateTime | None = None,
        after: RFC3339DateTime | None = None,
        order: OrderOrStr | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``GET`` request.

        Args:
            category_id: Filter events by category ID
            include_subcategories: Include events from subcategories when filtering by category
            attending_user: Filter to events where the specified user (username) has RSVP'd as going
            before: Return events starting before this date/time (ISO 8601 format)
            after: Return events starting after this date/time (ISO 8601 format)
            order: Sort order for events by start date (default: asc)
            limit: Maximum number of events to return (default: 200)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/discourse-post-event/events.ics"),
            query_params=[
                param[int | None]("category_id", category_id),
                param[IncludeSubcategoriesOrStr | None]("include_subcategories", include_subcategories),
                param[str | None]("attending_user", attending_user),
                param[RFC3339DateTime | None]("before", before),
                param[RFC3339DateTime | None]("after", after),
                param[OrderOrStr | None]("order", order),
                param[int | None]("limit", limit),
            ],
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_events(
        self,
        *,
        include_details: IncludeDetailsOrStr | None = None,
        category_id: int | None = None,
        include_subcategories: IncludeSubcategoriesOrStr | None = None,
        post_id: int | None = None,
        attending_user: str | None = None,
        before: RFC3339DateTime | None = None,
        after: RFC3339DateTime | None = None,
        order: OrderOrStr | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DiscoursePostEventEventsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            include_details: Include detailed event information (creator, invitees, stats, etc.)
            category_id: Filter events by category ID
            include_subcategories: Include events from subcategories when filtering by category
            post_id: Filter to events associated with a specific post ID
            attending_user: Filter to events where the specified user (username) has RSVP'd as going
            before: Return events starting before this date/time (ISO 8601 format)
            after: Return events starting after this date/time (ISO 8601 format)
            order: Sort order for events by start date (default: asc)
            limit: Maximum number of events to return (default: 200)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/discourse-post-event/events.json"),
            query_params=[
                param[IncludeDetailsOrStr | None]("include_details", include_details),
                param[int | None]("category_id", category_id),
                param[IncludeSubcategoriesOrStr | None]("include_subcategories", include_subcategories),
                param[int | None]("post_id", post_id),
                param[str | None]("attending_user", attending_user),
                param[RFC3339DateTime | None]("before", before),
                param[RFC3339DateTime | None]("after", after),
                param[OrderOrStr | None]("order", order),
                param[int | None]("limit", limit),
            ],
            decoder=async_json_decoder[DiscoursePostEventEventsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
