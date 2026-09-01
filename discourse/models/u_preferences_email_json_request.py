from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UPreferencesEmailJsonRequest(SdkBaseModel):
    email: EmailStr


class UPreferencesEmailJsonRequestDict(TypedDict):
    email: EmailStr
