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
from ..models.directory_items_json_response import DirectoryItemsJsonResponse
from ..models.enums.asc import AscOrStr
from ..models.enums.flag import FlagOrStr
from ..models.enums.order2 import Order2OrStr
from ..models.enums.order3 import Order3OrStr
from ..models.enums.period1 import Period1OrStr
from ..models.session_forgot_password_json_request import (
    SessionForgotPasswordJsonRequest,
    SessionForgotPasswordJsonRequestDict,
)
from ..models.session_forgot_password_json_response import SessionForgotPasswordJsonResponse
from ..models.u_by_external_json_response import UByExternalJsonResponse
from ..models.u_emails_json_response import UEmailsJsonResponse
from ..models.u_json_request import UJsonRequest, UJsonRequestDict
from ..models.u_json_response import UJsonResponse
from ..models.u_json_response1 import UJsonResponse1
from ..models.u_preferences_avatar_pick_json_request import (
    UPreferencesAvatarPickJsonRequest,
    UPreferencesAvatarPickJsonRequestDict,
)
from ..models.u_preferences_avatar_pick_json_response import UPreferencesAvatarPickJsonResponse
from ..models.u_preferences_email_json_request import UPreferencesEmailJsonRequest, UPreferencesEmailJsonRequestDict
from ..models.u_preferences_username_json_request import (
    UPreferencesUsernameJsonRequest,
    UPreferencesUsernameJsonRequestDict,
)
from ..models.user_actions_json_response import UserActionsJsonResponse
from ..models.user_avatar_refresh_gravatar_json_response import UserAvatarRefreshGravatarJsonResponse
from ..models.user_badges_json_response import UserBadgesJsonResponse
from ..models.users_json_request import UsersJsonRequest, UsersJsonRequestDict
from ..models.users_json_response import UsersJsonResponse
from ..models.users_password_reset_json_request import UsersPasswordResetJsonRequest, UsersPasswordResetJsonRequestDict
from ..server.server import Server


class Users:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = UsersWithRawResponse(client, server)

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

    def change_password(
        self,
        token: str,
        *,
        body: UsersPasswordResetJsonRequest | UsersPasswordResetJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``PUT`` request.

        Args:
            token: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.change_password(token, body=body, request_options=request_options).unwrap()

    def create_user(
        self,
        api_key: str,
        api_username: str,
        *,
        body: UsersJsonRequest | UsersJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsersJsonResponse:
        """Send a ``POST`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            user created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_user(
            api_key, api_username, body=body, request_options=request_options
        ).unwrap()

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

    def get_user(
        self, username: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UJsonResponse:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            user with primary group response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_user(
            username, api_key, api_username, request_options=request_options
        ).unwrap()

    def get_user_emails(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UEmailsJsonResponse:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_user_emails(username, request_options=request_options).unwrap()

    def get_user_external_id(
        self, external_id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UByExternalJsonResponse:
        """Send a ``GET`` request.

        Args:
            external_id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            user response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_user_external_id(
            external_id, api_key, api_username, request_options=request_options
        ).unwrap()

    def get_user_identiy_provider_external_id(
        self,
        provider: str,
        external_id: str,
        api_key: str,
        api_username: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UByExternalJsonResponse:
        """Send a ``GET`` request.

        Args:
            provider: Authentication provider name. Can be found in the provider callback URL:
                ``/auth/{provider}/callback``
            external_id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            user response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_user_identiy_provider_external_id(
            provider, external_id, api_key, api_username, request_options=request_options
        ).unwrap()

    def list_user_actions(
        self, offset: int, username: str, filter: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UserActionsJsonResponse:
        """Send a ``GET`` request.

        Args:
            offset: Value sent with the request.
            username: Value sent with the request.
            filter: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_user_actions(
            offset, username, filter, request_options=request_options
        ).unwrap()

    def list_user_badges(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UserBadgesJsonResponse:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_user_badges(username, request_options=request_options).unwrap()

    def list_users_public(
        self,
        period: Period1OrStr,
        order: Order2OrStr,
        *,
        asc: AscOrStr | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DirectoryItemsJsonResponse:
        """Send a ``GET`` request.

        Args:
            period: Value sent with the request.
            order: Value sent with the request.
            asc: Value sent with the request.
            page: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            directory items response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_users_public(
            period, order, asc=asc, page=page, request_options=request_options
        ).unwrap()

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

    def send_password_reset_email(
        self,
        *,
        body: SessionForgotPasswordJsonRequest | SessionForgotPasswordJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SessionForgotPasswordJsonResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.send_password_reset_email(body=body, request_options=request_options).unwrap()

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

    def update_avatar(
        self,
        username: str,
        *,
        body: UPreferencesAvatarPickJsonRequest | UPreferencesAvatarPickJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UPreferencesAvatarPickJsonResponse:
        """Send a ``PUT`` request.

        Args:
            username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            avatar updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_avatar(username, body=body, request_options=request_options).unwrap()

    def update_email(
        self,
        username: str,
        *,
        body: UPreferencesEmailJsonRequest | UPreferencesEmailJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``PUT`` request.

        Args:
            username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            email updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_email(username, body=body, request_options=request_options).unwrap()

    def update_user(
        self,
        username: str,
        api_key: str,
        api_username: str,
        *,
        body: UJsonRequest | UJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UJsonResponse1:
        """Send a ``PUT`` request.

        Args:
            username: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            user updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_user(
            username, api_key, api_username, body=body, request_options=request_options
        ).unwrap()

    def update_username(
        self,
        username: str,
        *,
        body: UPreferencesUsernameJsonRequest | UPreferencesUsernameJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``PUT`` request.

        Args:
            username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            username updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_username(username, body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> UsersWithRawResponse:
        return self._with_raw_response


class AsyncUsers:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncUsersWithRawResponse(client, server)

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

    async def change_password(
        self,
        token: str,
        *,
        body: UsersPasswordResetJsonRequest | UsersPasswordResetJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``PUT`` request.

        Args:
            token: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.change_password(token, body=body, request_options=request_options)
        ).unwrap()

    async def create_user(
        self,
        api_key: str,
        api_username: str,
        *,
        body: UsersJsonRequest | UsersJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsersJsonResponse:
        """Send a ``POST`` request.

        Args:
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            user created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_user(api_key, api_username, body=body, request_options=request_options)
        ).unwrap()

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

    async def get_user(
        self, username: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UJsonResponse:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            user with primary group response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_user(username, api_key, api_username, request_options=request_options)
        ).unwrap()

    async def get_user_emails(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UEmailsJsonResponse:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_user_emails(username, request_options=request_options)).unwrap()

    async def get_user_external_id(
        self, external_id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UByExternalJsonResponse:
        """Send a ``GET`` request.

        Args:
            external_id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            user response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_user_external_id(
                external_id, api_key, api_username, request_options=request_options
            )
        ).unwrap()

    async def get_user_identiy_provider_external_id(
        self,
        provider: str,
        external_id: str,
        api_key: str,
        api_username: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UByExternalJsonResponse:
        """Send a ``GET`` request.

        Args:
            provider: Authentication provider name. Can be found in the provider callback URL:
                ``/auth/{provider}/callback``
            external_id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            user response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_user_identiy_provider_external_id(
                provider, external_id, api_key, api_username, request_options=request_options
            )
        ).unwrap()

    async def list_user_actions(
        self, offset: int, username: str, filter: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UserActionsJsonResponse:
        """Send a ``GET`` request.

        Args:
            offset: Value sent with the request.
            username: Value sent with the request.
            filter: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_user_actions(offset, username, filter, request_options=request_options)
        ).unwrap()

    async def list_user_badges(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> UserBadgesJsonResponse:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.list_user_badges(username, request_options=request_options)).unwrap()

    async def list_users_public(
        self,
        period: Period1OrStr,
        order: Order2OrStr,
        *,
        asc: AscOrStr | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DirectoryItemsJsonResponse:
        """Send a ``GET`` request.

        Args:
            period: Value sent with the request.
            order: Value sent with the request.
            asc: Value sent with the request.
            page: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            directory items response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_users_public(
                period, order, asc=asc, page=page, request_options=request_options
            )
        ).unwrap()

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

    async def send_password_reset_email(
        self,
        *,
        body: SessionForgotPasswordJsonRequest | SessionForgotPasswordJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SessionForgotPasswordJsonResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.send_password_reset_email(body=body, request_options=request_options)
        ).unwrap()

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

    async def update_avatar(
        self,
        username: str,
        *,
        body: UPreferencesAvatarPickJsonRequest | UPreferencesAvatarPickJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UPreferencesAvatarPickJsonResponse:
        """Send a ``PUT`` request.

        Args:
            username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            avatar updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_avatar(username, body=body, request_options=request_options)
        ).unwrap()

    async def update_email(
        self,
        username: str,
        *,
        body: UPreferencesEmailJsonRequest | UPreferencesEmailJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``PUT`` request.

        Args:
            username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            email updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_email(username, body=body, request_options=request_options)
        ).unwrap()

    async def update_user(
        self,
        username: str,
        api_key: str,
        api_username: str,
        *,
        body: UJsonRequest | UJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UJsonResponse1:
        """Send a ``PUT`` request.

        Args:
            username: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            user updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_user(
                username, api_key, api_username, body=body, request_options=request_options
            )
        ).unwrap()

    async def update_username(
        self,
        username: str,
        *,
        body: UPreferencesUsernameJsonRequest | UPreferencesUsernameJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``PUT`` request.

        Args:
            username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            username updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_username(username, body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncUsersWithRawResponse:
        return self._with_raw_response


class UsersWithRawResponse(BaseRawResponse[RawClient, Server]):
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

    def change_password(
        self,
        token: str,
        *,
        body: UsersPasswordResetJsonRequest | UsersPasswordResetJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``PUT`` request.

        Args:
            token: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/password-reset/{token}.json"),
            path_params=[param[str]("token", token)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersPasswordResetJsonRequest | UsersPasswordResetJsonRequestDict | None](body),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_user(
        self,
        api_key: str,
        api_username: str,
        *,
        body: UsersJsonRequest | UsersJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsersJsonResponse, RawError]:
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
            url_template=self._server.default("/users.json"),
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[UsersJsonRequest | UsersJsonRequestDict | None](body),
            decoder=json_decoder[UsersJsonResponse],
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

    def get_user(
        self, username: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/u/{username}.json"),
            path_params=[param[str]("username", username)],
            headers=[param[str]("Api-Key", api_key), param[str]("Api-Username", api_username)],
            decoder=json_decoder[UJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_user_emails(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UEmailsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/u/{username}/emails.json"),
            path_params=[param[str]("username", username)],
            decoder=json_decoder[UEmailsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_user_external_id(
        self, external_id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UByExternalJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            external_id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/u/by-external/{external_id}.json"),
            path_params=[param[str]("external_id", external_id)],
            headers=[param[str]("Api-Key", api_key), param[str]("Api-Username", api_username)],
            decoder=json_decoder[UByExternalJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_user_identiy_provider_external_id(
        self,
        provider: str,
        external_id: str,
        api_key: str,
        api_username: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UByExternalJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            provider: Authentication provider name. Can be found in the provider callback URL:
                ``/auth/{provider}/callback``
            external_id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/u/by-external/{provider}/{external_id}.json"),
            path_params=[param[str]("provider", provider), param[str]("external_id", external_id)],
            headers=[param[str]("Api-Key", api_key), param[str]("Api-Username", api_username)],
            decoder=json_decoder[UByExternalJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_user_actions(
        self, offset: int, username: str, filter: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UserActionsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            offset: Value sent with the request.
            username: Value sent with the request.
            filter: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/user_actions.json"),
            query_params=[param[int]("offset", offset), param[str]("username", username), param[str]("filter", filter)],
            decoder=json_decoder[UserActionsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_user_badges(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UserBadgesJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/user-badges/{username}.json"),
            path_params=[param[str]("username", username)],
            decoder=json_decoder[UserBadgesJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_users_public(
        self,
        period: Period1OrStr,
        order: Order2OrStr,
        *,
        asc: AscOrStr | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DirectoryItemsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            period: Value sent with the request.
            order: Value sent with the request.
            asc: Value sent with the request.
            page: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/directory_items.json"),
            query_params=[
                param[Period1OrStr]("period", period),
                param[Order2OrStr]("order", order),
                param[AscOrStr | None]("asc", asc),
                param[int | None]("page", page),
            ],
            decoder=json_decoder[DirectoryItemsJsonResponse],
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

    def send_password_reset_email(
        self,
        *,
        body: SessionForgotPasswordJsonRequest | SessionForgotPasswordJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SessionForgotPasswordJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/session/forgot_password.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SessionForgotPasswordJsonRequest | SessionForgotPasswordJsonRequestDict | None](body),
            decoder=json_decoder[SessionForgotPasswordJsonResponse],
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

    def update_avatar(
        self,
        username: str,
        *,
        body: UPreferencesAvatarPickJsonRequest | UPreferencesAvatarPickJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UPreferencesAvatarPickJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/u/{username}/preferences/avatar/pick.json"),
            path_params=[param[str]("username", username)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UPreferencesAvatarPickJsonRequest | UPreferencesAvatarPickJsonRequestDict | None](body),
            decoder=json_decoder[UPreferencesAvatarPickJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_email(
        self,
        username: str,
        *,
        body: UPreferencesEmailJsonRequest | UPreferencesEmailJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``PUT`` request.

        Args:
            username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/u/{username}/preferences/email.json"),
            path_params=[param[str]("username", username)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UPreferencesEmailJsonRequest | UPreferencesEmailJsonRequestDict | None](body),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_user(
        self,
        username: str,
        api_key: str,
        api_username: str,
        *,
        body: UJsonRequest | UJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UJsonResponse1, RawError]:
        """Send a ``PUT`` request.

        Args:
            username: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/u/{username}.json"),
            path_params=[param[str]("username", username)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[UJsonRequest | UJsonRequestDict | None](body),
            decoder=json_decoder[UJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_username(
        self,
        username: str,
        *,
        body: UPreferencesUsernameJsonRequest | UPreferencesUsernameJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``PUT`` request.

        Args:
            username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/u/{username}/preferences/username.json"),
            path_params=[param[str]("username", username)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UPreferencesUsernameJsonRequest | UPreferencesUsernameJsonRequestDict | None](body),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncUsersWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
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

    async def change_password(
        self,
        token: str,
        *,
        body: UsersPasswordResetJsonRequest | UsersPasswordResetJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``PUT`` request.

        Args:
            token: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/users/password-reset/{token}.json"),
            path_params=[param[str]("token", token)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsersPasswordResetJsonRequest | UsersPasswordResetJsonRequestDict | None](body),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_user(
        self,
        api_key: str,
        api_username: str,
        *,
        body: UsersJsonRequest | UsersJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsersJsonResponse, RawError]:
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
            url_template=self._server.default("/users.json"),
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[UsersJsonRequest | UsersJsonRequestDict | None](body),
            decoder=json_decoder[UsersJsonResponse],
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

    async def get_user(
        self, username: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/u/{username}.json"),
            path_params=[param[str]("username", username)],
            headers=[param[str]("Api-Key", api_key), param[str]("Api-Username", api_username)],
            decoder=json_decoder[UJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_user_emails(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UEmailsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/u/{username}/emails.json"),
            path_params=[param[str]("username", username)],
            decoder=json_decoder[UEmailsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_user_external_id(
        self, external_id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UByExternalJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            external_id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/u/by-external/{external_id}.json"),
            path_params=[param[str]("external_id", external_id)],
            headers=[param[str]("Api-Key", api_key), param[str]("Api-Username", api_username)],
            decoder=json_decoder[UByExternalJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_user_identiy_provider_external_id(
        self,
        provider: str,
        external_id: str,
        api_key: str,
        api_username: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UByExternalJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            provider: Authentication provider name. Can be found in the provider callback URL:
                ``/auth/{provider}/callback``
            external_id: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/u/by-external/{provider}/{external_id}.json"),
            path_params=[param[str]("provider", provider), param[str]("external_id", external_id)],
            headers=[param[str]("Api-Key", api_key), param[str]("Api-Username", api_username)],
            decoder=json_decoder[UByExternalJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_user_actions(
        self, offset: int, username: str, filter: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UserActionsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            offset: Value sent with the request.
            username: Value sent with the request.
            filter: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/user_actions.json"),
            query_params=[param[int]("offset", offset), param[str]("username", username), param[str]("filter", filter)],
            decoder=json_decoder[UserActionsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_user_badges(
        self, username: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[UserBadgesJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            username: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/user-badges/{username}.json"),
            path_params=[param[str]("username", username)],
            decoder=json_decoder[UserBadgesJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_users_public(
        self,
        period: Period1OrStr,
        order: Order2OrStr,
        *,
        asc: AscOrStr | None = None,
        page: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DirectoryItemsJsonResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            period: Value sent with the request.
            order: Value sent with the request.
            asc: Value sent with the request.
            page: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/directory_items.json"),
            query_params=[
                param[Period1OrStr]("period", period),
                param[Order2OrStr]("order", order),
                param[AscOrStr | None]("asc", asc),
                param[int | None]("page", page),
            ],
            decoder=json_decoder[DirectoryItemsJsonResponse],
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

    async def send_password_reset_email(
        self,
        *,
        body: SessionForgotPasswordJsonRequest | SessionForgotPasswordJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SessionForgotPasswordJsonResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/session/forgot_password.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SessionForgotPasswordJsonRequest | SessionForgotPasswordJsonRequestDict | None](body),
            decoder=json_decoder[SessionForgotPasswordJsonResponse],
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

    async def update_avatar(
        self,
        username: str,
        *,
        body: UPreferencesAvatarPickJsonRequest | UPreferencesAvatarPickJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UPreferencesAvatarPickJsonResponse, RawError]:
        """Send a ``PUT`` request.

        Args:
            username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/u/{username}/preferences/avatar/pick.json"),
            path_params=[param[str]("username", username)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UPreferencesAvatarPickJsonRequest | UPreferencesAvatarPickJsonRequestDict | None](body),
            decoder=json_decoder[UPreferencesAvatarPickJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_email(
        self,
        username: str,
        *,
        body: UPreferencesEmailJsonRequest | UPreferencesEmailJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``PUT`` request.

        Args:
            username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/u/{username}/preferences/email.json"),
            path_params=[param[str]("username", username)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UPreferencesEmailJsonRequest | UPreferencesEmailJsonRequestDict | None](body),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_user(
        self,
        username: str,
        api_key: str,
        api_username: str,
        *,
        body: UJsonRequest | UJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UJsonResponse1, RawError]:
        """Send a ``PUT`` request.

        Args:
            username: Value sent with the request.
            api_key: Value sent with the request.
            api_username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/u/{username}.json"),
            path_params=[param[str]("username", username)],
            headers=[
                param[str]("Api-Key", api_key),
                param[str]("Api-Username", api_username),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[UJsonRequest | UJsonRequestDict | None](body),
            decoder=json_decoder[UJsonResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_username(
        self,
        username: str,
        *,
        body: UPreferencesUsernameJsonRequest | UPreferencesUsernameJsonRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``PUT`` request.

        Args:
            username: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/u/{username}/preferences/username.json"),
            path_params=[param[str]("username", username)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UPreferencesUsernameJsonRequest | UPreferencesUsernameJsonRequestDict | None](body),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )
