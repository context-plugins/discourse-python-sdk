from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UserAuthToken(SdkBaseModel):
    id: int
    client_ip: str
    location: str
    browser: str
    device: str
    os: str
    icon: str
    created_at: str
    seen_at: str
    is_active: bool


class UserAuthTokenDict(TypedDict):
    id: int
    client_ip: str
    location: str
    browser: str
    device: str
    os: str
    icon: str
    created_at: str
    seen_at: str
    is_active: bool
