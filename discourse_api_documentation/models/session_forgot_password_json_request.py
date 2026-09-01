from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SessionForgotPasswordJsonRequest(SdkBaseModel):
    login: str


class SessionForgotPasswordJsonRequestDict(TypedDict):
    login: str
