from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .category import Category, CategoryDict


class CategoriesJsonResponse(SdkBaseModel):
    category: Category


class CategoriesJsonResponseDict(TypedDict):
    category: Category | CategoryDict
