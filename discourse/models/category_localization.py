from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CategoryLocalization(SdkBaseModel):
    id: Optional[int] = UNSET
    """The unique identifier for an existing localization. Must be included otherwise the record will be deleted."""

    locale: str
    """The locale for the localization, e.g., 'en', 'zh_CN'. Locale should be in the list of
    SiteSetting.content_localization_supported_locales."""

    name: str
    """The name of the category in the specified locale."""

    description: Optional[str] = UNSET
    """The description excerpt of the category in the specified locale."""


class CategoryLocalizationDict(TypedDict):
    id: NotRequired[int]
    locale: str
    name: str
    description: NotRequired[str]
