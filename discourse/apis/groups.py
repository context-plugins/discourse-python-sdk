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
from ..models.admin_groups_json_request import AdminGroupsJsonRequest, AdminGroupsJsonRequestDict
from ..models.admin_groups_json_response import AdminGroupsJsonResponse
from ..models.admin_groups_json_response1 import AdminGroupsJsonResponse1
from ..models.groups_by_id_json_response import GroupsByIdJsonResponse
from ..models.groups_json_request import GroupsJsonRequest, GroupsJsonRequestDict
from ..models.groups_json_response import GroupsJsonResponse
from ..models.groups_json_response1 import GroupsJsonResponse1
from ..models.groups_json_response2 import GroupsJsonResponse2
from ..models.groups_members_json_request import GroupsMembersJsonRequest, GroupsMembersJsonRequestDict
from ..models.groups_members_json_response import GroupsMembersJsonResponse
from ..models.groups_members_json_response1 import GroupsMembersJsonResponse1
from ..models.groups_members_json_response2 import GroupsMembersJsonResponse2
from ..server.server import Server


class Groups:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = GroupsWithRawResponse(client, server)

    def add_group_members(
        self,
        id_: int,
        *,
        body: GroupsMembersJsonRequest | GroupsMembersJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GroupsMembersJsonResponse1:
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
        return self._with_raw_response.add_group_members(id_, body=body, request_options=request_options).unwrap()

    def create_group(
        self,
        *,
        body: AdminGroupsJsonRequest | AdminGroupsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminGroupsJsonResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            group created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_group(body=body, request_options=request_options).unwrap()

    def delete_group(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> AdminGroupsJsonResponse1:
        """Send a ``DELETE`` request.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_group(id_, request_options=request_options).unwrap()

    def get_group(self, name: str, *, request_options: RequestOptionsOrDict | None = None) -> GroupsJsonResponse:
        """Send a ``GET`` request.

        Args:
            name: Use group name instead of id
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_group(name, request_options=request_options).unwrap()

    def get_group_by_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GroupsByIdJsonResponse:
        """Send a ``GET`` request.

        Args:
            id_: Use group name instead of id
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response (by id)

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_group_by_id(id_, request_options=request_options).unwrap()

    def list_group_members(
        self, name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GroupsMembersJsonResponse:
        """Send a ``GET`` request.

        Args:
            name: Use group name instead of id
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_group_members(name, request_options=request_options).unwrap()

    def list_groups(self, *, request_options: RequestOptionsOrDict | None = None) -> GroupsJsonResponse2:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_groups(request_options=request_options).unwrap()

    def remove_group_members(
        self,
        id_: int,
        *,
        body: GroupsMembersJsonRequest | GroupsMembersJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GroupsMembersJsonResponse2:
        """Send a ``DELETE`` request.

        Args:
            id_: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.remove_group_members(id_, body=body, request_options=request_options).unwrap()

    def update_group(
        self,
        id_: int,
        *,
        body: GroupsJsonRequest | GroupsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GroupsJsonResponse1:
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
        return self._with_raw_response.update_group(id_, body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> GroupsWithRawResponse:
        return self._with_raw_response


class AsyncGroups:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncGroupsWithRawResponse(client, server)

    async def add_group_members(
        self,
        id_: int,
        *,
        body: GroupsMembersJsonRequest | GroupsMembersJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GroupsMembersJsonResponse1:
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
        return (
            await self._with_raw_response.add_group_members(id_, body=body, request_options=request_options)
        ).unwrap()

    async def create_group(
        self,
        *,
        body: AdminGroupsJsonRequest | AdminGroupsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminGroupsJsonResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            group created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_group(body=body, request_options=request_options)).unwrap()

    async def delete_group(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> AdminGroupsJsonResponse1:
        """Send a ``DELETE`` request.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_group(id_, request_options=request_options)).unwrap()

    async def get_group(self, name: str, *, request_options: RequestOptionsOrDict | None = None) -> GroupsJsonResponse:
        """Send a ``GET`` request.

        Args:
            name: Use group name instead of id
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_group(name, request_options=request_options)).unwrap()

    async def get_group_by_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GroupsByIdJsonResponse:
        """Send a ``GET`` request.

        Args:
            id_: Use group name instead of id
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response (by id)

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_group_by_id(id_, request_options=request_options)).unwrap()

    async def list_group_members(
        self, name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GroupsMembersJsonResponse:
        """Send a ``GET`` request.

        Args:
            name: Use group name instead of id
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.list_group_members(name, request_options=request_options)).unwrap()

    async def list_groups(self, *, request_options: RequestOptionsOrDict | None = None) -> GroupsJsonResponse2:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.list_groups(request_options=request_options)).unwrap()

    async def remove_group_members(
        self,
        id_: int,
        *,
        body: GroupsMembersJsonRequest | GroupsMembersJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GroupsMembersJsonResponse2:
        """Send a ``DELETE`` request.

        Args:
            id_: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.remove_group_members(id_, body=body, request_options=request_options)
        ).unwrap()

    async def update_group(
        self,
        id_: int,
        *,
        body: GroupsJsonRequest | GroupsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GroupsJsonResponse1:
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
        return (await self._with_raw_response.update_group(id_, body=body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncGroupsWithRawResponse:
        return self._with_raw_response


class GroupsWithRawResponse(BaseRawResponse[RawClient, Server]):
    def add_group_members(
        self,
        id_: int,
        *,
        body: GroupsMembersJsonRequest | GroupsMembersJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GroupsMembersJsonResponse1, RawError]:
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
            url_template=self._server.default("/groups/{id}/members.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GroupsMembersJsonRequest | GroupsMembersJsonRequestDict | None](body),
            decoder=json_decoder[GroupsMembersJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_group(
        self,
        *,
        body: AdminGroupsJsonRequest | AdminGroupsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminGroupsJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin/groups.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdminGroupsJsonRequest | AdminGroupsJsonRequestDict | None](body),
            decoder=json_decoder[AdminGroupsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_group(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AdminGroupsJsonResponse1, RawError]:
        """Send a ``DELETE`` request.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/admin/groups/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=json_decoder[AdminGroupsJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_group(
        self, name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GroupsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            name: Use group name instead of id
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/groups/{name}.json"),
            path_params=[param[str]("name", name)],
            decoder=json_decoder[GroupsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_group_by_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GroupsByIdJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            id_: Use group name instead of id
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/groups/by-id/{id}.json"),
            path_params=[param[str]("id", id_)],
            decoder=json_decoder[GroupsByIdJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_group_members(
        self, name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GroupsMembersJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            name: Use group name instead of id
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/groups/{name}/members.json"),
            path_params=[param[str]("name", name)],
            decoder=json_decoder[GroupsMembersJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_groups(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GroupsJsonResponse2, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/groups.json"),
            decoder=json_decoder[GroupsJsonResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def remove_group_members(
        self,
        id_: int,
        *,
        body: GroupsMembersJsonRequest | GroupsMembersJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GroupsMembersJsonResponse2, RawError]:
        """Send a ``DELETE`` request.

        Args:
            id_: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/groups/{id}/members.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GroupsMembersJsonRequest | GroupsMembersJsonRequestDict | None](body),
            decoder=json_decoder[GroupsMembersJsonResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_group(
        self,
        id_: int,
        *,
        body: GroupsJsonRequest | GroupsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GroupsJsonResponse1, RawError]:
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
            url_template=self._server.default("/groups/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GroupsJsonRequest | GroupsJsonRequestDict | None](body),
            decoder=json_decoder[GroupsJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncGroupsWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def add_group_members(
        self,
        id_: int,
        *,
        body: GroupsMembersJsonRequest | GroupsMembersJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GroupsMembersJsonResponse1, RawError]:
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
            url_template=self._server.default("/groups/{id}/members.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GroupsMembersJsonRequest | GroupsMembersJsonRequestDict | None](body),
            decoder=async_json_decoder[GroupsMembersJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_group(
        self,
        *,
        body: AdminGroupsJsonRequest | AdminGroupsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminGroupsJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin/groups.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdminGroupsJsonRequest | AdminGroupsJsonRequestDict | None](body),
            decoder=async_json_decoder[AdminGroupsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_group(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AdminGroupsJsonResponse1, RawError]:
        """Send a ``DELETE`` request.

        Args:
            id_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/admin/groups/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=async_json_decoder[AdminGroupsJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_group(
        self, name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GroupsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            name: Use group name instead of id
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/groups/{name}.json"),
            path_params=[param[str]("name", name)],
            decoder=async_json_decoder[GroupsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_group_by_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GroupsByIdJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            id_: Use group name instead of id
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/groups/by-id/{id}.json"),
            path_params=[param[str]("id", id_)],
            decoder=async_json_decoder[GroupsByIdJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_group_members(
        self, name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GroupsMembersJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            name: Use group name instead of id
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/groups/{name}/members.json"),
            path_params=[param[str]("name", name)],
            decoder=async_json_decoder[GroupsMembersJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_groups(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GroupsJsonResponse2, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/groups.json"),
            decoder=async_json_decoder[GroupsJsonResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def remove_group_members(
        self,
        id_: int,
        *,
        body: GroupsMembersJsonRequest | GroupsMembersJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GroupsMembersJsonResponse2, RawError]:
        """Send a ``DELETE`` request.

        Args:
            id_: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/groups/{id}/members.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GroupsMembersJsonRequest | GroupsMembersJsonRequestDict | None](body),
            decoder=async_json_decoder[GroupsMembersJsonResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_group(
        self,
        id_: int,
        *,
        body: GroupsJsonRequest | GroupsJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GroupsJsonResponse1, RawError]:
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
            url_template=self._server.default("/groups/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GroupsJsonRequest | GroupsJsonRequestDict | None](body),
            decoder=async_json_decoder[GroupsJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
