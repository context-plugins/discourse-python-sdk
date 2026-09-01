from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UserAvatarRefreshGravatarJsonResponse(SdkBaseModel):
    gravatar_upload_id: int | None
    gravatar_avatar_template: str | None


class UserAvatarRefreshGravatarJsonResponseDict(TypedDict):
    gravatar_upload_id: int | None
    gravatar_avatar_template: str | None
