from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .category import Category, CategoryDict


class CShowJsonResponse(SdkBaseModel):
    category: Category


class CShowJsonResponseDict(TypedDict):
    category: CategoryDict
