from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PostsJsonRequest2(SdkBaseModel):
    force_destroy: Optional[bool] = UNSET
    """The ``SiteSetting.can_permanently_delete`` needs to be enabled first before this param can be used. Also this
    endpoint needs to be called first without ``force_destroy`` and then followed up with a second call 5 minutes later
    with ``force_destroy`` to permanently delete."""


class PostsJsonRequest2Dict(TypedDict):
    force_destroy: NotRequired[bool]
