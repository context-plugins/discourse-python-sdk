from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.admin import Admin
from .apis.backups import Backups
from .apis.badges import Badges
from .apis.categories import Categories
from .apis.discourse_calendar_events import DiscourseCalendarEvents
from .apis.groups import Groups
from .apis.invites import Invites
from .apis.notifications import Notifications
from .apis.posts import Posts
from .apis.private_messages import PrivateMessages
from .apis.search import Search
from .apis.site import Site
from .apis.tags import Tags
from .apis.topics import Topics
from .apis.uploads import Uploads
from .apis.users import Users
from .base_client import DEFAULT_TIMEOUT, BaseDiscourseApiDocumentationClient
from .core import OPERATING_SYSTEM, PYTHON_RUNTIME, HttpClient, HttpxClient, RawClient, param


class DiscourseApiDocumentationClient(BaseDiscourseApiDocumentationClient[RawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_http_client: HttpClient | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout),
            global_headers=[
                param[str]("User-Agent", "DiscourseApiDocumentationClient/0.1.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "0.1.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )

    @cached_property
    def admin(self) -> Admin:
        return Admin(self._raw_client, self._server)

    @cached_property
    def backups(self) -> Backups:
        return Backups(self._raw_client, self._server)

    @cached_property
    def badges(self) -> Badges:
        return Badges(self._raw_client, self._server)

    @cached_property
    def categories(self) -> Categories:
        return Categories(self._raw_client, self._server)

    @cached_property
    def discourse_calendar_events(self) -> DiscourseCalendarEvents:
        return DiscourseCalendarEvents(self._raw_client, self._server)

    @cached_property
    def groups(self) -> Groups:
        return Groups(self._raw_client, self._server)

    @cached_property
    def invites(self) -> Invites:
        return Invites(self._raw_client, self._server)

    @cached_property
    def notifications(self) -> Notifications:
        return Notifications(self._raw_client, self._server)

    @cached_property
    def posts(self) -> Posts:
        return Posts(self._raw_client, self._server)

    @cached_property
    def private_messages(self) -> PrivateMessages:
        return PrivateMessages(self._raw_client, self._server)

    @cached_property
    def search(self) -> Search:
        return Search(self._raw_client, self._server)

    @cached_property
    def site(self) -> Site:
        return Site(self._raw_client, self._server)

    @cached_property
    def tags(self) -> Tags:
        return Tags(self._raw_client, self._server)

    @cached_property
    def topics(self) -> Topics:
        return Topics(self._raw_client, self._server)

    @cached_property
    def uploads(self) -> Uploads:
        return Uploads(self._raw_client, self._server)

    @cached_property
    def users(self) -> Users:
        return Users(self._raw_client, self._server)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = DiscourseApiDocumentationClient
