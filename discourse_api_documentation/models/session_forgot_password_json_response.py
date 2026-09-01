from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SessionForgotPasswordJsonResponse(SdkBaseModel):
    success: str
    user_found: bool


class SessionForgotPasswordJsonResponseDict(TypedDict):
    success: str
    user_found: bool
