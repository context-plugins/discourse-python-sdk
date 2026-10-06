from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.admin import AsyncAdmin
from .apis.backups import AsyncBackups
from .apis.badges import AsyncBadges
from .apis.categories import AsyncCategories
from .apis.discourse_calendar_events import AsyncDiscourseCalendarEvents
from .apis.groups import AsyncGroups
from .apis.invites import AsyncInvites
from .apis.notifications import AsyncNotifications
from .apis.posts import AsyncPosts
from .apis.private_messages import AsyncPrivateMessages
from .apis.search import AsyncSearch
from .apis.site import AsyncSite
from .apis.tags import AsyncTags
from .apis.topics import AsyncTopics
from .apis.uploads import AsyncUploads
from .apis.users import AsyncUsers
from .base_client import DEFAULT_TIMEOUT, BaseDiscourseClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    AsyncHttpClient,
    AsyncHttpx2Client,
    AsyncRawClient,
    RetryOptionsOrDict,
    param,
)


class AsyncDiscourseClient(BaseDiscourseClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        retry_options: int | RetryOptionsOrDict | None = None,
        custom_async_http_client: AsyncHttpClient | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout, retry_options=retry_options)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpx2Client(timeout=timeout)
            ),
            retry_options=self._retry_options,
            global_headers=[
                param[str]("User-Agent", "DiscourseClient/0.1.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "0.1.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )

    @cached_property
    def admin(self) -> AsyncAdmin:
        return AsyncAdmin(self._raw_client, self._server)

    @cached_property
    def backups(self) -> AsyncBackups:
        return AsyncBackups(self._raw_client, self._server)

    @cached_property
    def badges(self) -> AsyncBadges:
        return AsyncBadges(self._raw_client, self._server)

    @cached_property
    def categories(self) -> AsyncCategories:
        return AsyncCategories(self._raw_client, self._server)

    @cached_property
    def discourse_calendar_events(self) -> AsyncDiscourseCalendarEvents:
        return AsyncDiscourseCalendarEvents(self._raw_client, self._server)

    @cached_property
    def groups(self) -> AsyncGroups:
        return AsyncGroups(self._raw_client, self._server)

    @cached_property
    def invites(self) -> AsyncInvites:
        return AsyncInvites(self._raw_client, self._server)

    @cached_property
    def notifications(self) -> AsyncNotifications:
        return AsyncNotifications(self._raw_client, self._server)

    @cached_property
    def posts(self) -> AsyncPosts:
        return AsyncPosts(self._raw_client, self._server)

    @cached_property
    def private_messages(self) -> AsyncPrivateMessages:
        return AsyncPrivateMessages(self._raw_client, self._server)

    @cached_property
    def search(self) -> AsyncSearch:
        return AsyncSearch(self._raw_client, self._server)

    @cached_property
    def site(self) -> AsyncSite:
        return AsyncSite(self._raw_client, self._server)

    @cached_property
    def tags(self) -> AsyncTags:
        return AsyncTags(self._raw_client, self._server)

    @cached_property
    def topics(self) -> AsyncTopics:
        return AsyncTopics(self._raw_client, self._server)

    @cached_property
    def uploads(self) -> AsyncUploads:
        return AsyncUploads(self._raw_client, self._server)

    @cached_property
    def users(self) -> AsyncUsers:
        return AsyncUsers(self._raw_client, self._server)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncDiscourseClient
