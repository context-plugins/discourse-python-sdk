from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AvailableCategoryType(SdkBaseModel):
    id: str
    name: str
    title: str
    description: str
    icon: str
    available: bool
    visible: bool
    configuration_schema: Any


class AvailableCategoryTypeDict(TypedDict):
    id: str
    name: str
    title: str
    description: str
    icon: str
    available: bool
    visible: bool
    configuration_schema: Any
