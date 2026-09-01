from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SiteBasicInfoJsonResponse(SdkBaseModel):
    logo_url: str
    logo_small_url: str
    apple_touch_icon_url: str
    favicon_url: str
    title: str
    description: str
    header_primary_color: str
    header_background_color: str
    login_required: bool
    locale: str
    include_in_discourse_discover: bool
    mobile_logo_url: str


class SiteBasicInfoJsonResponseDict(TypedDict):
    logo_url: str
    logo_small_url: str
    apple_touch_icon_url: str
    favicon_url: str
    title: str
    description: str
    header_primary_color: str
    header_background_color: str
    login_required: bool
    locale: str
    include_in_discourse_discover: bool
    mobile_logo_url: str
