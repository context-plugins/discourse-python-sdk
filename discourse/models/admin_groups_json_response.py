from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .basic_group import BasicGroup, BasicGroupDict


class AdminGroupsJsonResponse(SdkBaseModel):
    basic_group: BasicGroup


class AdminGroupsJsonResponseDict(TypedDict):
    basic_group: BasicGroupDict
