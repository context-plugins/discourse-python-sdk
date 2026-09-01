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
from ..models.admin_users_activate_json_response import AdminUsersActivateJsonResponse
from ..models.admin_users_anonymize_json_response import AdminUsersAnonymizeJsonResponse
from ..models.admin_users_deactivate_json_response import AdminUsersDeactivateJsonResponse
from ..models.admin_users_json_request import AdminUsersJsonRequest, AdminUsersJsonRequestDict
from ..models.admin_users_json_response import AdminUsersJsonResponse
from ..models.admin_users_json_response1 import AdminUsersJsonResponse1
from ..models.admin_users_json_response2 import AdminUsersJsonResponse2
from ..models.admin_users_list_json_response import AdminUsersListJsonResponse
from ..models.admin_users_log_out_json_response import AdminUsersLogOutJsonResponse
from ..models.admin_users_silence_json_request import AdminUsersSilenceJsonRequest, AdminUsersSilenceJsonRequestDict
from ..models.admin_users_silence_json_response import AdminUsersSilenceJsonResponse
from ..models.admin_users_suspend_json_request import AdminUsersSuspendJsonRequest, AdminUsersSuspendJsonRequestDict
from ..models.admin_users_suspend_json_response import AdminUsersSuspendJsonResponse
from ..models.enums.asc import AscOrStr
from ..models.enums.flag import FlagOrStr
from ..models.enums.order3 import Order3OrStr
from ..models.user_avatar_refresh_gravatar_json_response import UserAvatarRefreshGravatarJsonResponse
from ..server.server import Server


class Admin:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = AdminWithRawResponse(client, server)

    def activate_user(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> AdminUsersActivateJsonResponse:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.activate_user(id, request_options=request_options).unwrap()

    def admin_get_user(self, id: int, *, request_options: RequestOptionsOrDict | None = None) -> AdminUsersJsonResponse:
        """Send a ``GET`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_get_user(id, request_options=request_options).unwrap()

    def admin_list_users(
        self,
        *,
        order: Order3OrStr | None = None,
        asc: AscOrStr | None = None,
        page: int | None = None,
        show_emails: bool | None = None,
        stats: bool | None = None,
        email: str | None = None,
        ip: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[AdminUsersJsonResponse2]:
        """Send a ``GET`` request.

        Args:
            order: Value sent with the request.
            asc: Value sent with the request.
            page: Value sent with the request.
            show_emails: Include user email addresses in response. These requests will be logged in the staff action
                logs.
            stats: Include user stats information
            email: Filter to the user with this email address
            ip: Filter to users with this IP address
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            users response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_list_users(
            order=order,
            asc=asc,
            page=page,
            show_emails=show_emails,
            stats=stats,
            email=email,
            ip=ip,
            request_options=request_options,
        ).unwrap()

    def admin_list_users_flag(
        self,
        flag: FlagOrStr,
        *,
        order: Order3OrStr | None = None,
        asc: AscOrStr | None = None,
        page: int | None = None,
        show_emails: bool | None = None,
        stats: bool | None = None,
        email: str | None = None,
        ip: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[AdminUsersListJsonResponse]:
        """Send a ``GET`` request.

        Args:
            flag: Value sent with the request.
            order: Value sent with the request.
            asc: Value sent with the request.
            page: Value sent with the request.
            show_emails: Include user email addresses in response. These requests will be logged in the staff action
                logs.
            stats: Include user stats information
            email: Filter to the user with this email address
            ip: Filter to users with this IP address
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.admin_list_users_flag(
            flag,
            order=order,
            asc=asc,
            page=page,
            show_emails=show_emails,
            stats=stats,
            email=email,
            ip=ip,
            request_options=request_options,
        ).unwrap()

    def anonymize_user(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> AdminUsersAnonymizeJsonResponse:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.anonymize_user(id, request_options=request_options).unwrap()

    def deactivate_user(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> AdminUsersDeactivateJsonResponse:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.deactivate_user(id, request_options=request_options).unwrap()

    def delete_user(
        self,
        id: int,
        *,
        body: AdminUsersJsonRequest | AdminUsersJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminUsersJsonResponse1:
        """Send a ``DELETE`` request.

        Args:
            id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_user(id, body=body, request_options=request_options).unwrap()

    def log_out_user(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> AdminUsersLogOutJsonResponse:
        """Send a ``POST`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.log_out_user(id, request_options=request_options).unwrap()

    def refresh_gravatar(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UserAvatarRefreshGravatarJsonResponse:
        """Send a ``POST`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.refresh_gravatar(username, request_options=request_options).unwrap()

    def silence_user(
        self,
        id: int,
        *,
        body: AdminUsersSilenceJsonRequest | AdminUsersSilenceJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminUsersSilenceJsonResponse:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.silence_user(id, body=body, request_options=request_options).unwrap()

    def suspend_user(
        self,
        id: int,
        *,
        body: AdminUsersSuspendJsonRequest | AdminUsersSuspendJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminUsersSuspendJsonResponse:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.suspend_user(id, body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> AdminWithRawResponse:
        return self._with_raw_response


class AsyncAdmin:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncAdminWithRawResponse(client, server)

    async def activate_user(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> AdminUsersActivateJsonResponse:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.activate_user(id, request_options=request_options)).unwrap()

    async def admin_get_user(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> AdminUsersJsonResponse:
        """Send a ``GET`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.admin_get_user(id, request_options=request_options)).unwrap()

    async def admin_list_users(
        self,
        *,
        order: Order3OrStr | None = None,
        asc: AscOrStr | None = None,
        page: int | None = None,
        show_emails: bool | None = None,
        stats: bool | None = None,
        email: str | None = None,
        ip: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[AdminUsersJsonResponse2]:
        """Send a ``GET`` request.

        Args:
            order: Value sent with the request.
            asc: Value sent with the request.
            page: Value sent with the request.
            show_emails: Include user email addresses in response. These requests will be logged in the staff action
                logs.
            stats: Include user stats information
            email: Filter to the user with this email address
            ip: Filter to users with this IP address
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            users response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_list_users(
                order=order,
                asc=asc,
                page=page,
                show_emails=show_emails,
                stats=stats,
                email=email,
                ip=ip,
                request_options=request_options,
            )
        ).unwrap()

    async def admin_list_users_flag(
        self,
        flag: FlagOrStr,
        *,
        order: Order3OrStr | None = None,
        asc: AscOrStr | None = None,
        page: int | None = None,
        show_emails: bool | None = None,
        stats: bool | None = None,
        email: str | None = None,
        ip: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[AdminUsersListJsonResponse]:
        """Send a ``GET`` request.

        Args:
            flag: Value sent with the request.
            order: Value sent with the request.
            asc: Value sent with the request.
            page: Value sent with the request.
            show_emails: Include user email addresses in response. These requests will be logged in the staff action
                logs.
            stats: Include user stats information
            email: Filter to the user with this email address
            ip: Filter to users with this IP address
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.admin_list_users_flag(
                flag,
                order=order,
                asc=asc,
                page=page,
                show_emails=show_emails,
                stats=stats,
                email=email,
                ip=ip,
                request_options=request_options,
            )
        ).unwrap()

    async def anonymize_user(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> AdminUsersAnonymizeJsonResponse:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.anonymize_user(id, request_options=request_options)).unwrap()

    async def deactivate_user(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> AdminUsersDeactivateJsonResponse:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.deactivate_user(id, request_options=request_options)).unwrap()

    async def delete_user(
        self,
        id: int,
        *,
        body: AdminUsersJsonRequest | AdminUsersJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminUsersJsonResponse1:
        """Send a ``DELETE`` request.

        Args:
            id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_user(id, body=body, request_options=request_options)).unwrap()

    async def log_out_user(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> AdminUsersLogOutJsonResponse:
        """Send a ``POST`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.log_out_user(id, request_options=request_options)).unwrap()

    async def refresh_gravatar(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UserAvatarRefreshGravatarJsonResponse:
        """Send a ``POST`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.refresh_gravatar(username, request_options=request_options)).unwrap()

    async def silence_user(
        self,
        id: int,
        *,
        body: AdminUsersSilenceJsonRequest | AdminUsersSilenceJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminUsersSilenceJsonResponse:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.silence_user(id, body=body, request_options=request_options)).unwrap()

    async def suspend_user(
        self,
        id: int,
        *,
        body: AdminUsersSuspendJsonRequest | AdminUsersSuspendJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdminUsersSuspendJsonResponse:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.suspend_user(id, body=body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncAdminWithRawResponse:
        return self._with_raw_response


class AdminWithRawResponse(BaseRawResponse[RawClient, Server]):
    def activate_user(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AdminUsersActivateJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/admin/users/{id}/activate.json"),
            path_params=[param[int]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=json_decoder[AdminUsersActivateJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_get_user(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AdminUsersJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin/users/{id}.json"),
            path_params=[param[int]("id", id)],
            decoder=json_decoder[AdminUsersJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_list_users(
        self,
        *,
        order: Order3OrStr | None = None,
        asc: AscOrStr | None = None,
        page: int | None = None,
        show_emails: bool | None = None,
        stats: bool | None = None,
        email: str | None = None,
        ip: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[AdminUsersJsonResponse2], RawError]:
        """Send a ``GET`` request.

        Args:
            order: Value sent with the request.
            asc: Value sent with the request.
            page: Value sent with the request.
            show_emails: Include user email addresses in response. These requests will be logged in the staff action
                logs.
            stats: Include user stats information
            email: Filter to the user with this email address
            ip: Filter to users with this IP address
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin/users.json"),
            query_params=[
                param[Order3OrStr | None]("order", order),
                param[AscOrStr | None]("asc", asc),
                param[int | None]("page", page),
                param[bool | None]("show_emails", show_emails),
                param[bool | None]("stats", stats),
                param[str | None]("email", email),
                param[str | None]("ip", ip),
            ],
            decoder=json_decoder[list[AdminUsersJsonResponse2]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def admin_list_users_flag(
        self,
        flag: FlagOrStr,
        *,
        order: Order3OrStr | None = None,
        asc: AscOrStr | None = None,
        page: int | None = None,
        show_emails: bool | None = None,
        stats: bool | None = None,
        email: str | None = None,
        ip: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[AdminUsersListJsonResponse], RawError]:
        """Send a ``GET`` request.

        Args:
            flag: Value sent with the request.
            order: Value sent with the request.
            asc: Value sent with the request.
            page: Value sent with the request.
            show_emails: Include user email addresses in response. These requests will be logged in the staff action
                logs.
            stats: Include user stats information
            email: Filter to the user with this email address
            ip: Filter to users with this IP address
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin/users/list/{flag}.json"),
            path_params=[param[FlagOrStr]("flag", flag)],
            query_params=[
                param[Order3OrStr | None]("order", order),
                param[AscOrStr | None]("asc", asc),
                param[int | None]("page", page),
                param[bool | None]("show_emails", show_emails),
                param[bool | None]("stats", stats),
                param[str | None]("email", email),
                param[str | None]("ip", ip),
            ],
            decoder=json_decoder[list[AdminUsersListJsonResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def anonymize_user(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AdminUsersAnonymizeJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/admin/users/{id}/anonymize.json"),
            path_params=[param[int]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=json_decoder[AdminUsersAnonymizeJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def deactivate_user(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AdminUsersDeactivateJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/admin/users/{id}/deactivate.json"),
            path_params=[param[int]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=json_decoder[AdminUsersDeactivateJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_user(
        self,
        id: int,
        *,
        body: AdminUsersJsonRequest | AdminUsersJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminUsersJsonResponse1, RawError]:
        """Send a ``DELETE`` request.

        Args:
            id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/admin/users/{id}.json"),
            path_params=[param[int]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdminUsersJsonRequest | AdminUsersJsonRequestDict | None](body),
            decoder=json_decoder[AdminUsersJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def log_out_user(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AdminUsersLogOutJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin/users/{id}/log_out.json"),
            path_params=[param[int]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=json_decoder[AdminUsersLogOutJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def refresh_gravatar(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UserAvatarRefreshGravatarJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/user_avatar/{username}/refresh_gravatar.json"),
            path_params=[param[str]("username", username)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=json_decoder[UserAvatarRefreshGravatarJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def silence_user(
        self,
        id: int,
        *,
        body: AdminUsersSilenceJsonRequest | AdminUsersSilenceJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminUsersSilenceJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/admin/users/{id}/silence.json"),
            path_params=[param[int]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdminUsersSilenceJsonRequest | AdminUsersSilenceJsonRequestDict | None](body),
            decoder=json_decoder[AdminUsersSilenceJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def suspend_user(
        self,
        id: int,
        *,
        body: AdminUsersSuspendJsonRequest | AdminUsersSuspendJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminUsersSuspendJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/admin/users/{id}/suspend.json"),
            path_params=[param[int]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdminUsersSuspendJsonRequest | AdminUsersSuspendJsonRequestDict | None](body),
            decoder=json_decoder[AdminUsersSuspendJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncAdminWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def activate_user(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AdminUsersActivateJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/admin/users/{id}/activate.json"),
            path_params=[param[int]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=json_decoder[AdminUsersActivateJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_get_user(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AdminUsersJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin/users/{id}.json"),
            path_params=[param[int]("id", id)],
            decoder=json_decoder[AdminUsersJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_list_users(
        self,
        *,
        order: Order3OrStr | None = None,
        asc: AscOrStr | None = None,
        page: int | None = None,
        show_emails: bool | None = None,
        stats: bool | None = None,
        email: str | None = None,
        ip: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[AdminUsersJsonResponse2], RawError]:
        """Send a ``GET`` request.

        Args:
            order: Value sent with the request.
            asc: Value sent with the request.
            page: Value sent with the request.
            show_emails: Include user email addresses in response. These requests will be logged in the staff action
                logs.
            stats: Include user stats information
            email: Filter to the user with this email address
            ip: Filter to users with this IP address
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin/users.json"),
            query_params=[
                param[Order3OrStr | None]("order", order),
                param[AscOrStr | None]("asc", asc),
                param[int | None]("page", page),
                param[bool | None]("show_emails", show_emails),
                param[bool | None]("stats", stats),
                param[str | None]("email", email),
                param[str | None]("ip", ip),
            ],
            decoder=json_decoder[list[AdminUsersJsonResponse2]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def admin_list_users_flag(
        self,
        flag: FlagOrStr,
        *,
        order: Order3OrStr | None = None,
        asc: AscOrStr | None = None,
        page: int | None = None,
        show_emails: bool | None = None,
        stats: bool | None = None,
        email: str | None = None,
        ip: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[AdminUsersListJsonResponse], RawError]:
        """Send a ``GET`` request.

        Args:
            flag: Value sent with the request.
            order: Value sent with the request.
            asc: Value sent with the request.
            page: Value sent with the request.
            show_emails: Include user email addresses in response. These requests will be logged in the staff action
                logs.
            stats: Include user stats information
            email: Filter to the user with this email address
            ip: Filter to users with this IP address
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/admin/users/list/{flag}.json"),
            path_params=[param[FlagOrStr]("flag", flag)],
            query_params=[
                param[Order3OrStr | None]("order", order),
                param[AscOrStr | None]("asc", asc),
                param[int | None]("page", page),
                param[bool | None]("show_emails", show_emails),
                param[bool | None]("stats", stats),
                param[str | None]("email", email),
                param[str | None]("ip", ip),
            ],
            decoder=json_decoder[list[AdminUsersListJsonResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def anonymize_user(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AdminUsersAnonymizeJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/admin/users/{id}/anonymize.json"),
            path_params=[param[int]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=json_decoder[AdminUsersAnonymizeJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def deactivate_user(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AdminUsersDeactivateJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/admin/users/{id}/deactivate.json"),
            path_params=[param[int]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=json_decoder[AdminUsersDeactivateJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_user(
        self,
        id: int,
        *,
        body: AdminUsersJsonRequest | AdminUsersJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminUsersJsonResponse1, RawError]:
        """Send a ``DELETE`` request.

        Args:
            id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/admin/users/{id}.json"),
            path_params=[param[int]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdminUsersJsonRequest | AdminUsersJsonRequestDict | None](body),
            decoder=json_decoder[AdminUsersJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def log_out_user(
        self, id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AdminUsersLogOutJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/admin/users/{id}/log_out.json"),
            path_params=[param[int]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=json_decoder[AdminUsersLogOutJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def refresh_gravatar(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UserAvatarRefreshGravatarJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/user_avatar/{username}/refresh_gravatar.json"),
            path_params=[param[str]("username", username)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=json_decoder[UserAvatarRefreshGravatarJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def silence_user(
        self,
        id: int,
        *,
        body: AdminUsersSilenceJsonRequest | AdminUsersSilenceJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminUsersSilenceJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/admin/users/{id}/silence.json"),
            path_params=[param[int]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdminUsersSilenceJsonRequest | AdminUsersSilenceJsonRequestDict | None](body),
            decoder=json_decoder[AdminUsersSilenceJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def suspend_user(
        self,
        id: int,
        *,
        body: AdminUsersSuspendJsonRequest | AdminUsersSuspendJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdminUsersSuspendJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/admin/users/{id}/suspend.json"),
            path_params=[param[int]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdminUsersSuspendJsonRequest | AdminUsersSuspendJsonRequestDict | None](body),
            decoder=json_decoder[AdminUsersSuspendJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
