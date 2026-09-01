from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UEmailsJsonResponse(SdkBaseModel):
    email: str
    secondary_emails: list[Any]
    unconfirmed_emails: list[Any]
    associated_accounts: list[Any]


class UEmailsJsonResponseDict(TypedDict):
    email: str
    secondary_emails: list[Any]
    unconfirmed_emails: list[Any]
    associated_accounts: list[Any]
