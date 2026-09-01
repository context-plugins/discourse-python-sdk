from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .directory_item import DirectoryItem, DirectoryItemDict
from .meta1 import Meta1, Meta1Dict


class DirectoryItemsJsonResponse(SdkBaseModel):
    directory_items: list[DirectoryItem]
    meta: Meta1


class DirectoryItemsJsonResponseDict(TypedDict):
    directory_items: list[DirectoryItem | DirectoryItemDict]
    meta: Meta1 | Meta1Dict
