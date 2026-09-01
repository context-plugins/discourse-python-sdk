from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsersJsonRequest(SdkBaseModel):
    name: str
    email: str
    password: str
    username: str
    active: Optional[bool] = UNSET
    """This param requires an admin api key in the request header or it will be ignored"""

    approved: Optional[bool] = UNSET
    user_fields: Optional[dict[str, bool]] = UNSET
    external_ids: Optional[Any] = UNSET


class UsersJsonRequestDict(TypedDict):
    name: str
    email: str
    password: str
    username: str
    active: NotRequired[bool]
    approved: NotRequired[bool]
    user_fields: NotRequired[dict[str, bool]]
    external_ids: NotRequired[Any]
