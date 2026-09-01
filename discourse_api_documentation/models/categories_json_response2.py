from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .category2 import Category2, Category2Dict


class CategoriesJsonResponse2(SdkBaseModel):
    success: str
    category: Category2


class CategoriesJsonResponse2Dict(TypedDict):
    success: str
    category: Category2 | Category2Dict
